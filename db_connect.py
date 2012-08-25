#!/usr/bin/python
#
# db_connect.py
# Copyright (C) 2012 ruwan <ruwan800@gmail.com>
# 
# ibus-vadan-er is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ibus-vadan-er is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.";


import sqlite3
from config import DB


class DBConnect:
	
	def __init__(self):
		self.conn = sqlite3.connect(DB.FILE)

	def execute(self,SQL):
		try:
			cursor = self.conn.cursor()
			cursor.execute(SQL)
			self.conn.commit()
			results = cursor.fetchall()
			cursor.close()
#			print("SQL::success")		########################################
		except  Exception as error:
			print("SQL::error")			########################################
			print(error)				########################################
			print(SQL)					########################################
			results = []
		if results:
			pass						#results = self.modResult(results)
		else:
			results = []
		return results

	def executemany(self,SQL,ourList):
		try:
			cursor = self.conn.cursor()
			cursor.executemany(SQL,ourList)
			self.conn.commit()
#			results = cursor.fetchall()
			cursor.close()
#			print("SQL::success")		########################################
		except  Exception as error:
			print("SQL::error")			########################################
			print(error)				########################################
			print(SQL[:10000])			########################################



	def close(self):
#		self.conn.close()
		pass


"""
	def modResult(self,result):
		if not result:
			return None
		else:
			temp1 = []
			for i in result:
				temp2 = []
				for j in i:
#					item = str(j).encode("UTF-8")
					temp2.append(item)
				temp1.append(temp2)
			return temp1
"""
###########################--not needed--#######################################
"""
		if not result:
			result = None
		elif len(result[0]) == 1:
			if len(result) == 1:
				result = str(result[0][0])
			else:
				temp = []
				for item in result:
					temp.append(str(item[0]))
				result = temp
		elif len(result) == 1:
			temp = []
			for item in result[0]:
				temp.append(str(item))
			result = temp
		else:
			temp1 = []
			for i in result:
				temp2 = []
				for j in i:
					temp2.append(str(j))
				temp1.append(temp2)
			result = temp1
		return result
"""
################################################################################

#DBConnect = DBConnect()
