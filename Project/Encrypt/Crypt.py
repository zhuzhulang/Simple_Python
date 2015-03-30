#!/usr/bin/env/python

import hashlib

def Crypt(crypy_type,data):
	algo = str.lower(crypy_type)
	if algo in hashlib.algorithms:
		create_hash = hashlib.new(algo)
		#create_hash = getattr(hashlib,crypy_type)()
		for compute in chunk_size(32,data):
		    create_hash.update(compute)
		return create_hash.hexdigest()

def chunk_size(str_len,data):
	data_len = len(data)
	data_start = 0
	while str_len < data_len:
		compute = data[data_start:data_start+str_len]
		yield compute
		data_start +=str_len
	return

data='thisisatestfileformd5crypt'
print Crypt('Md5',data)