#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#  Module that defines a stress class
#
#  (C) Copyright 2009 Olivier Delhomme
#  e-mail : olivier.delhomme@free.fr
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#

"""
module stress
"""

class Test :
	
	def __init__(self, testname) :
		self.testname = testname
	
	def default_test(self) :
		print 'This is a default test'
	
	def start(self) :
		self.execute()

	testname = ''			# name for the test
	execute = default_test	# function being executed by the test
		
	
#

