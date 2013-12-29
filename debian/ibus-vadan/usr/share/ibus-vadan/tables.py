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


vowels = ["a","e","i","o","u","A","E","I","O","U"]

#consonents 	= 	["b","c","d","f","g","h","j","k","l","m",
#				 "n","p","r","s","t","v","w","x","y","B","C","D","F",
#				 "G","J","K","L","N","P","T","."]

#replace key length should be less than 5 characters		
primaryReplaces   =	[ [ "aa", "A" ],
					  [ "ae", "2" ],
					  [ "aE", "3" ],
					  [ "ee", "E" ],
					  [ "ii", "I" ],
					  [ "uu", "U" ],
					  [ "oo", "O" ],
					  [ "ai", "ayi" ],
					  [ "au", "avu" ],
					  [ "eu", "evu" ],
					  [ "ei", "eyi" ],
					  [ "oa", "O" ],
					  [ "ea", "E" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "", "" ],
					  [ "aae", "3" ],
					  [ "aee", "3" ],
					  [ "W", "v" ],
					  [ "w", "v" ],
					  [ "Q", "aE" ],
					  [ "q", "ae" ],
					  [ "X", "k.s" ],
					  [ "x", "k.s" ] ]

#priority level should be equal or less than 5 and cannot be 0.
secondaryReplaces =	[ [ "e", "e", "2", "2" ],
					  [ "u", "u", "a", "2" ],
					  [ "O", "O", "U", "2" ],
					  [ "t.h", "t", "t.h", "1" ],
					  [ "n.d", "n.d", "D", "1" ],
					  [ "g.n", "g.n", "N", "1" ] ]
#					  [ "", "", "", "" ],
#					  [ "", "", "", "" ], ]

finalReplaces	  =  [ [ "2", "a" ],
					   [ "3", "a" ],
					   [ "z", "x" ],
					   [ "Z", "x" ],
					   [ "yi", "y." ],
					   [ "vu", "v." ], ]

#should be 1,2,3
complexityFactors = [ [ "K" , "1" ],
					  [ "G" , "1" ],
					  [ "C" , "1" ],
					  [ "J" , "1" ],
					  [ "T" , "1" ],
					  [ "D" , "1" ],
					  [ "N" , "1" ],
					  [ "P" , "1" ],
					  [ "B" , "1" ],
					  [ "L" , "1" ],
					  [ "S" , "1" ],
					  [ "A" , "1" ],
					  [ "I" , "1" ],
					  [ "U" , "1" ],
					  [ "E" , "1" ],
					  [ "O" , "1" ],
					  [ "Z" , "1" ],
					  [ "2" , "2" ],
					  [ "3" , "3" ],
					  [ "" , "" ],
					  [ "" , "" ],
					  [ "" , "" ],
					  [ "" , "" ],
					  [ "" , "" ],
					  [ "" , "" ],
					  [ "" , "" ], ]



