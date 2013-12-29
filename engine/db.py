#!/usr/bin/python
#
# ibus-vadan - Input method for Sinhala based on I-Bus
#
# Copyright (C) 2012 ruwan Jayasinghe <ruwan800@gmail.com>
#               2012 Kasun Madhusanka <ruwan800@gmail.com>
# 
# ibus-vadan is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ibus-vadan is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


import sqlite3
from prepare import prepare
from advanced import advanced

db_file = '/var/lib/ibus-vadan/vadan.sqlite'

class initDb:

	def __init__(self,db):

		self.conn = sqlite3.connect(db)
		self.suggestions = []
		self.newWord = None

	def execute(self,SQL,params=None):
		try:
			cursor = self.conn.cursor()
			cursor.execute(SQL,params)
			self.conn.commit()
			results = cursor.fetchall()
			cursor.close()
		except  Exception as error:
			results = []
		if not results:
			results = []
		return results

	def closeDb(self):
		self.conn.close()

	def suggest(self, text):
		self.suggestions = []
		self.newWord = None
		suffWord = advanced.getWordWithSuffix( text)
		if suffWord :
			wordList = prepare.suggest( suffWord)
			self.getExactWords( wordList)
		wordList = prepare.suggest( text)
		self.getExactWords( wordList)
		self.getSimilarWords( wordList)
		if len(self.suggestions) < 5 :
			self.newWord = advanced.getTransWord( text)
			self.suggestions.append(self.newWord)
		return self.suggestions[:7]
		

	def getExactWords(self, wordList):		
		#first we trying to get the exact match of  both consonents and vowels
		tempSuggestions = []
		for wordData in wordList:
			cons, vows, complexityFactor = wordData
			SQL = "SELECT word,CF FROM vadan WHERE con = ? AND vow = ? ORDER BY frequency DESC"
			result = self.execute(SQL,[cons,vows])
			if result:
				for word,CF in result:
					if CF == complexityFactor:
						self.suggestions.append(word)
					else:
						tempSuggestions.append(word)
			if 5 < len(self.suggestions):
				break
		self.suggestions.extend(tempSuggestions)


	def getSimilarWords(self, wordList):
		#matching extra word addings
		if 5 < len(self.suggestions):
			return None

		#now we trying to match both consonents and vowels but not word length
		cons, vows, complexityFactor = wordList[0]
		SQL = "SELECT word FROM vadan WHERE con LIKE ? AND vow LIKE ? ORDER BY frequency DESC LIMIT 5"
		self.getDbResult(SQL,[cons+"%",vows+"%"])
		if  5 < len(self.suggestions):
			return None

		#now we trying to match consonents only
		SQL = "SELECT word FROM vadan WHERE con = ? ORDER BY frequency DESC LIMIT 5"
		self.getDbResult(SQL,[cons])
		if 5 < len(self.suggestions):
			return None

		#at last we try to match consonents only in any length
		SQL = "SELECT word FROM vadan WHERE con LIKE ? ORDER BY frequency DESC LIMIT 5"
		self.getDbResult(SQL,[cons+"%"])


	def getDbResult(self, SQL,params):
		result = self.execute(SQL,params)
		if result:
			result = [ word for word, in result ]
			for item in self.suggestions:
				if item in result:
					result.remove(item)
			self.suggestions.extend(result)

	def setAdvancedTables(self):
		SQL = "SELECT * FROM suffixes"
		suffixTable = self.execute(SQL)
		SQL = "SELECT * FROM trans_list"
		transTable = self.execute(SQL)
		advanced.setTables(suffixTable,transTable)

	def updateDb(self, text):
		return
		if text == self.newWord :
			if not (advanced.suffixTable or advanced.transTable):
				self.setAdvancedTables()
			con,vow = advanced.newWordPartials(self.newWord)
			SQL = "INSERT INTO vadan (con,vow,word) values ( ?, ?, ? )"
			self.execute(SQL,[con,vow,text])
		else:
			SQL = "UPDATE vadan SET frequency = frequency+1 WHERE word = ?"
			self.execute(SQL,text)


Db = initDb(db_file)
