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

class initAdvanced:

	suffixTable = None
	transTable  = None

	def setTables(self, suffixTable, transTable):

		#TODO create this method
		return None


	def getWordWithSuffix(self, text):

		#TODO create this method
		return None

	
	def getTransWord(self, text):

		#TODO create this method
		return text


	def newWordPartials(self, newWord):

		#TODO create this method
		return None,None #return con,vow


advanced = initAdvanced()
