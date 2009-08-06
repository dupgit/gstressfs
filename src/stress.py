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

import os, time

class TestSuite :
	
	name = ''
	path = ''
	testlist = []
	
	def __init__(self, name, path) :
		self.name = name
		self.path = path


	def add_test(self, test) :
		self.testlist.append(test)


	def run_test_suite(self) :
		max = len(self.testlist)
		for i in range(max) :
			test = self.testlist[i]
			test.start(self.path)

						
	def set_path(self, path) :
		self.path = path


	def print_stats(self) :
		print 'Results for TestSuite "' + self.name + '"'
		max = len(self.testlist)
		for i in range(max) :
			print
			self.testlist[i].print_stats()
			
	def list_tests(self) :
		print 'Test list for TestSuite "' + self.name + '"'
		max = len(self.testlist)
		for i in range(max) :
			print str(i).ljust(3) + ' : ' + self.testlist[i].name
		
# Class TestSuite


class Test :
	
	def __init__(self, name, function) :
		self.name = name
		self.execute = function
		self.times = []
	
	
	def default_test(self) :
		print 'This is the default test'
	
	
	def start(self, path) :
		
		current_path = os.getcwd()
		os.chdir(path)
		
		begin_cpu = time.clock()
		begin_time = time.time()
		
		self.execute(path)
		
		end_time = time.time()
		end_cpu = time.clock()
		
		os.chdir(current_path)
		
		a_time = end_cpu - begin_cpu, end_time - begin_time
		self.times.append(a_time)


	def print_stats(self) :
		
		nb_tests = len(self.times)
		avg_cpu = 0
		avg_real = 0
		print 'Results for test "' + self.name + '"'
		print 'Tests'.ljust(8) + ' . ' + 'CPU   '.rjust(8) + '.' + 'real time'.rjust(42)
		for i in range(nb_tests) :
			cpu_time, real_time = self.times[i]
			avg_cpu += cpu_time
			avg_real += real_time
			print str(i).ljust(8) + ' : ' + str(cpu_time).rjust(8) + ' ' + str(real_time).rjust(42)
		
		print 'Averages : ' + str(avg_cpu/nb_tests).rjust(8) + ' ' + str(avg_real/nb_tests).rjust(42)


	name = ''		     	# name for the test
	execute = default_test	# function being executed by the test
	times = []              # execution times tuples (cpu, real_time)
	
	
# Class Test

