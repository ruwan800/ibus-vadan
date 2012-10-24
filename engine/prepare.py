#!/usr/bin/python
#
# ibus-vadan - Input method for Sinhala based on I-Bus
#
# Copyright (C) 2012 ruwan Jayasinghe <ruwan800@gmail.com>
#               2012 Kasun Madhusanka <kasunmbx@gmail.com>
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

import tables

class initPrepare:

	vowels					= []
	consonents				= []
	primaryReplaces			= []
	secondaryReplaces		= []
	finalReplaces			= []
	complexityFactors		= []
	wordList 				= []
	word = None

	def __init__(self):
		
		self.vowels 	= tables.vowels
		temp = tables.primaryReplaces
		temp = [ dict([(x[0],x[1]) for x in temp if len(x[0])==i]) for i in range (5,0,-1) ]
		self.primaryReplaces = temp
		temp = tables.secondaryReplaces
		temp = [ dict([(x[0],x[1:3]) for x in temp if x[3]==str(i)]) for i in range (1,6) ]
		self.secondaryReplaces = temp
		temp = tables.finalReplaces
		temp = dict([ (x[0],x[1]) for x in temp ] )
		self.finalReplaces	= temp
		temp	= tables.complexityFactors
		temp = [ [(x[0]) for x in temp if x[1]==str(i)] for i in range (1,4) ]
		self.complexityFactors = temp


	def setWord(self,word):
		
		self.word = word


	def primaryPrepare(self):
		
		word = self.word
		for key in self.primaryReplaces[4].keys():
			word = word.replace(key,self.primaryReplaces[4][key])
		if word[0] in self.vowels:
			word = ".{}#".format(word)
		else:
			word = "{}#".format(word)
		temp1 = ""
		temp2 = ""
		for letter in word:
			if letter in self.vowels:
				temp2 = temp2 + letter
			else:
				if temp2 :
					if temp2 in self.vowels :
						temp1 = temp1 + temp2
						temp2 = ""
					else :
						for level in self.primaryReplaces:
							for prk in level.keys():
								if prk in temp2:
									temp1 = temp1 + level[prk]
									temp2 = ""
									break
							if not temp2:
								break
						if temp2 :
							temp1 = temp1 + temp2[0]
							temp2 = ""
				else:
					if temp1 :
						temp1 = temp1 + "."
				if letter != "#":
					temp1 = temp1 + letter
		self.word = temp1


	def secondaryPrepare( self ):

		replCount = 0
		replValues = {}
		replPoints = []
		parallels = []
		for replaceLevel in self.secondaryReplaces :
			if replaceLevel :
				for replacer in replaceLevel.keys() :
					if 3 < replCount:
						break
					if replacer in self.word:
						if not [ True for x in replValues.keys() if replacer in x]:
							replacePoint = self.word.find(replacer)
							replPoints.append(replacePoint)
							replValues[replacer] = replaceLevel[replacer]
							replCount += 1
							for i in range(self.word.count(replacer)-1):
								if 3 < replCount:
									break
								replacePoint = self.word.find(replacer,replacePoint+len(replacer))
								replPoints.append( self.word.find(replacer,replacePoint) )
								replValues[replacer] = replaceLevel[replacer]
								replCount += 1

		if replCount :
			if replCount == 1:
				parallels.append([self.word])
			else:
				replPoints = sorted(replPoints)
				replPoints[0] = 0
				replPoints.append(len(self.word))
				parallels.append([self.word[replPoints[x]:replPoints[x+1]] for x in range(len(replPoints)-1)])
			parallels.append(parallels[0])
			parallels = [[j.replace(k,replValues[k][i]) for j in parallels[i] \
															for k in replValues.keys() if k in j ] \
															for i in range(2) ]	#TODO we have a big problem here.
			#below is some solution for problem above
			if 4 < len(parallels)/2 :
				for i in [range(4,len(parallels)/2)+range(4+len(parallels)/2,len(parallels))]:
					del parallels[i]

			self.wordList = ["".join([ parallels[bool(y&(2**x))][x] for x in range(len(parallels[0]))]) \
																	for y in range(2**len(parallels[0])) ]
		else:
			self.wordList = [ self.word ]
#		print("wordList:"+str(self.wordList))####################################

	def finalPrepare(self):

	##calculatig complexity factor
		TWLi = []
		for word in self.wordList :
			complexityFactor = 0
			cx = self.complexityFactors
			for char in word[:8]:
				if char in cx[0]:
					complexity = 1
				elif char in cx[1]:
					complexity = 2
				elif char in cx[2]:
					complexity = 3
				else:
					complexity = 0
				if complexityFactor == 0:
					complexityFactor = complexity
				else:
					complexityFactor = (complexityFactor*4)+complexity

	##converting std compex word into ever simple word
			for key in self.finalReplaces.keys():
				word = word.replace( key, self.finalReplaces[ key ])
			word = word.lower()

	##seperate vowel part and cosonent part
			conText = "".join([ word[x] for x in range( 0, len(word), 2) ])
			vowText = "".join([ word[x] for x in range( 1, len(word), 2) ])

			
			TWLi.append( [conText, vowText, complexityFactor ] )
		self.wordList = TWLi
		
	def suggest( self, text):
		self.setWord( text)
		self.primaryPrepare()
		self.secondaryPrepare()
		self.finalPrepare()
		return self.wordList



prepare = initPrepare()
