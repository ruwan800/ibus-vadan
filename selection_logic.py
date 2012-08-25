vows = ["a","e","i","o","u","z","A","E","I","O","U","Z","2","3","."]

cons = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","y",
		"B","C","D","G","J","K","L","N","P","T","."]

complexReplaces = {	"aa"	: "A",
					"ae"	: "2",
					"aE"	: "3",
					"ee"	: "E",
					"ii"	: "I",
					"uu"	: "U",
					"oo"	: "O",
					"ai"	: "z",
					"x"		: "ks",
					"q"		: "kiv",
					"au"	: "Z",
					"w"		: "v"	}

simpleRplaces = {	"2"	: "a",
					"3"	: "a",
					"z"	: "x",		#TODO
					"Z"	: "x",	}	#TODO

CF1chars = ["K", "G", "C", "J", "T", "D", "N", "P", "B", "L", "S", "A", "I", "U", "E", "O", "Z" ]
CF2chars = ["2" ]
CF3chars = ["3" ]


#w replace v
#q replace kiv

def prepareText(word):

	vowText = ""
	conText = ""
	complexityFactor = 0

##creating standard complex word

	word = word.replace( "aee", "3")
	for key in complexReplaces.keys():
		word = word.replace( key, complexReplaces[ key ])
	newWord = ""
	if word[0] in vows:
		word = "."+word
	for i in range(0,len(word)):
		if word[i] in cons:
			if i+1 < len(word):
				if word[i+1] in vows:
					newWord += word[i]+word[i+1]
				else:
					newWord += word[i]+"."
			else:
				newWord += word[i]+"."
	word = newWord
	temp = word#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##calculatig complexity factor
	for char in word[:8]:
		if char in CF1chars:
			complexity = 1
		elif char in CF2chars:
			complexity = 2
		elif char in CF3chars:
			complexity = 3
		else:
			complexity = 0
		if complexityFactor == 0:
			complexityFactor = complexity
		else:
			complexityFactor = (complexityFactor*4)+complexity

##converting std compex word into ever simple word
	for key in simpleRplaces.keys():
		word = word.replace( key, simpleRplaces[ key ])
	word = word.lower()

##seperate vowel part and cosonent part
	for x in range( 0, len(word), 2):
		conText += word[x]
	for x in range( 1, len(word), 2):
		vowText += word[x]
	
	print(temp,conText,vowText,complexityFactor)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	return conText, vowText, complexityFactor

