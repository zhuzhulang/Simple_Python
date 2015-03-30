#!/usr/bin/env/python

from __future__ import print_function
import os
import itertools

def directory_list(given_dir):
	f_num = 0
	d_num = 0
	for this_dir,sub_dir,filename in os.walk(given_dir):
		print(('-----'*(d_num+1)),this_dir)
		for f_name in filename:
			path = os.path.join(this_dir,f_name)
			print(path)
			f_num +=1
		d_num +=1
	print('Found',d_num,'directories')
	print('Found',f_num,'files')

dir = '/home/dog/py'
directory_list(dir)