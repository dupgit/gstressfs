#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#  Tools to stress your filesystem. Use at your own risks !
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
import os, sys, getopt, stress


# Help message for main program
def usage() :
  print """
  NAME
      stressfs
  
  SYNOPSIS
      stressfs [OPTION]... 
      
  DESCRIPTION
      
      
  OPTION
      -h, --help
        Show this help
        
  EXAMPLE

  """
#


def parse_command_line() :
	short_options = "h"
	long_options = ["help"]

	# Read options and arguments  
	try:
		opts, args = getopt.getopt(sys.argv[1:], short_options, long_options)
	except getopt.GetoptError, err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		print "opt = ",opt
		print "arg = ",arg
		
		if opt in ("-h", "--help") :
			usage();
			
#

def my_first_test() :
	
	print 'This is my first test'
	


# parse_command_line()

stressfs = stress.Test("Mon premier test")
stressfs.start()
stressfs.execute = my_first_test
stressfs.start()
print stressfs.testname
