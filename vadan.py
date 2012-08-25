from db_connect import DBConnect
from selection_logic import prepareText

class vadan:

	def suggest(self,word):

		cons, vows, complexityFactor = prepareText(word)
		print(cons,vows)##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
		conn = DBConnect()
		
		testA = 0	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		testB = 0	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		testC = 0 	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		testD = 0	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		
		#first we trying to get the exact match of  both consonents and vowels
		SQL = "SELECT word,CF FROM vadan WHERE con = '{}' AND vow = '{}'".format(cons,vows)
		result = conn.execute(SQL)
		suggestions = []
		tempSuggestions = []
		if result:
			for word,CF in result:
				if CF == complexityFactor:
					suggestions.append(word)
				else:
					tempSuggestions.append(word)
			suggestions.extend(tempSuggestions)
		testA = len(suggestions)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#		print("AAAAAAAAAAAA")#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#		for item in suggestions:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#			print(item)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		if len(suggestions) < 5:
			#matching extra word addings  TODO
			pass
			if len(suggestions) < 5:
				#now we trying to match both consonents and vowels but not word length
				SQL = "SELECT word FROM vadan WHERE con LIKE '{}%' AND vow LIKE '{}%' LIMIT 5".format(cons,vows)
				result = conn.execute(SQL)
				if result:
					result = [ word for word, in result ]
					testB = len(result)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
					for item in suggestions:
						if item in result:
							result.remove(item)
					suggestions.extend(result)
#					print("BBBBBBBBBBBBB")#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#					for item in suggestions:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#						print(item)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				if len(suggestions) < 5:
					#now we trying to match consonents only
					SQL = "SELECT word FROM vadan WHERE con LIKE '{}' LIMIT 5".format(cons)
					result = conn.execute(SQL)
					if result:
						result = [ word for word, in result ]
						testC = len(result)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
						for item in suggestions:
							if item in result:
								result.remove(item)
						suggestions.extend(result)
#						print("CCCCCCCCCCCCC")#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#						for item in suggestions:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#							print(item)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
					if len(suggestions) < 5:
						#at last we try to match consonents only in any length
						SQL = "SELECT word FROM vadan WHERE con LIKE '{}%' LIMIT 5".format(cons)
						result = conn.execute(SQL)
						if result:
							result = [ word for word, in result ]
							testD = len(result)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
							for item in suggestions:
								if item in result:
									result.remove(item)
							suggestions.extend(result)
#							print("PPPPPPPPPPPPP")#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#							for item in suggestions:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#								print(item)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


		conn.close()

		print("CV={},C*V*={},C={},C*={}".format( testA, testB, testC, testD))#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		if 5 < len(suggestions):
			suggestions = suggestions[:5]
		return suggestions


vadan = vadan()
