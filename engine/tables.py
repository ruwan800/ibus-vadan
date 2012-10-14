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


vowels = ["a","e","i","o","u","A","E","I","O","U"]

#consonents 	= 	["b","c","d","f","g","h","j","k","l","m",
#				 "n","p","r","s","t","v","w","x","y","B","C","D","F",
#				 "G","J","K","L","N","P","T","."]

#replace key length should be less than 5 characters		
primaryReplaces   =	[ [ "aa", "A" ],
					  [ "AA", "A" ],
					  [ "ae", "2" ],
					  [ "q" , "2" ],
					  [ "aE", "3" ],	#ah>>
					  [ "Q" , "3" ],
					  [ "aae","3" ],
					  [ "aee","3" ],
					  [ "Ae", "3" ],
					  [ "AE", "3" ],
					  [ "ee", "E" ],
					  [ "EE", "E" ],
					  [ "ea", "E" ],
					  [ "ii", "I" ],
					  [ "II", "I" ],
					  [ "uu", "U" ],
					  [ "UU", "U" ],
					  [ "oo", "O" ],
					  [ "oa", "O" ],
					  [ "OO", "O" ],
					  [ "aai", "Ay." ],
					  [ "ai", "2y." ],
					  [ "aI", "2y." ],
					  [ "Ai", "2y." ],
					  [ "AI", "2y." ],
					  [ "oi", "oy." ],
					  [ "oI", "oy." ],
					  [ "Oi", "Oy." ],
					  [ "OI", "Oy." ],
					  [ "au", "av." ],
					  [ "AU", "av." ],
					  [ "eu", "ev." ],
					  [ "EU", "ev." ],
					  [ "ei", "ey." ],
					  [ "EI", "ey." ],
					  [ "t", "T" ],
					  [ "H", "h" ],
					  [ "", "" ],
					  [ "W", "v" ],
					  [ "W", "v" ],
					  [ "f", "P" ],
					  [ "F", "P" ],
					  [ "z", "s" ],
					  [ "Z", "s" ],
					  [ "M", "m" ],
					  [ "X", "ks" ],
					  [ "x", "ks" ] ]

#priority level should be equal or less than 5 and cannot be 0.
secondaryReplaces =	[ [ "e", "e", "2", "2" ],
					  [ "u", "u", "a", "2" ],
					  [ "c", "k", "c", "2" ],
					  [ "O", "O", "U", "1" ],
					  [ "E", "E", "I", "1" ],
					  [ "k.h", "K", "k.h", "1" ],
					  [ "K.h", "K", "K.h", "1" ],
					  [ "g.h", "G", "g.h", "1" ],
					  [ "G.h", "G", "G.h", "1" ],
					  [ "c.h", "c", "c.h", "1" ],
					  [ "C.h", "C", "C.h", "1" ],
					  [ "T.h", "t", "T.h", "1" ],
					  [ "d.h", "D", "d.h", "1" ],
					  [ "D.h", "D", "D.h", "1" ],
					  [ "p.h", "P", "p.h", "1" ],
					  [ "P.h", "P", "p.h", "1" ],
					  [ "b.h", "B", "b.h", "1" ],
					  [ "B.h", "B", "B.h", "1" ],
					  [ "s.h", "S", "s.h", "1" ],
					  [ "S.h", "S", "S.h", "1" ],
					  [ "n.d", "n.d", "D", "1" ],
					  [ "n.D", "n.D", "D", "1" ],
					  [ "N.d", "N.d", "D", "1" ],
					  [ "N.D", "N.D", "D", "1" ],
					  [ "m.d", "m.d", "D", "1" ],
					  [ "m.D", "m.D", "D", "1" ],
					  [ "ah.", "3",  "a.h.", "1" ],
					  [ "Ah.", "3",  "A.h.", "1" ],
					  [ "oh.", "O",  "o.h.", "1" ],
					  [ "Oh.", "O",  "O.h.", "1" ],
					  [ "eh.", "E",  "e.h.", "1" ],
					  [ "Eh.", "E",  "E.h.", "1" ],
					  [ "g.n", "g.n", "N", "1" ],
					  [ "g.N", "g.N", "N", "1" ],
					  [ "G.n", "G.n", "N", "1" ],
					  [ "G.N", "G.N", "N", "1" ] ]
#					  [ "", "", "", "" ], ]

finalReplaces	  =  [ [ "2", "a" ],
					   [ "3", "a" ],
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
					  [ "" , "" ], ]



