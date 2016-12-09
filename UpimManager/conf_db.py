#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:14:33 2016

@author: Prohodimec 
"""
# проcтенькие функции и классы для работы с bd
import shelve
import os
import sys_inf

class Ubd_class:
	def __init__(self, keys, opch):
		self.keys = keys
		self.opch = opch
	def baz_vsb(self):
		name_files = sys_inf.CONF_PATH + 'conf.db'
		if os.path.exists(name_files):
			db = shelve.open(name_files)
			db[self.keys] = self.opch
			db.close()

class Dobd_class:
	def __init__(self, keys):
		self.keys = keys
	def baz_vst(self):
		files = sys_inf.CONF_PATH + 'conf.db'
		if os.path.exists(files):
			bd = shelve.open(files)
			for i in list(bd.keys()):
				if i == self.keys:
					return bd[i]
			bd.close() 
			
def Ds(slovo, lists):
	fil = sys_inf.CONF_PATH + 'index.db'
	o = shelve.open(fil)
	for i in list(o.keys()):
		bas = o[i]
		if bas.find(slovo) != -1:
			lists.append(i.split('.')[0])

	o.close()
# база индекса заметок для поиска
def searcingdb(tops):
	fills = sys_inf.CONF_PATH + 'index.db'
	op = shelve.open(fills)
	nam = tops + '.ox'
	for i in list(op.keys()):
		if i == nam:
			return op[i]
	op.close()

def dobdb(keynam, texnam):
	fils = sys_inf.CONF_PATH + 'index.db'
	bd = shelve.open(fils)
	bd[keynam] = texnam
	bd.close()
# база недели
def dbdb(keynam, texnam):
	fils = sys_inf.CONF_PATH + 'ned.db'
	bd = shelve.open(fils)
	bd[keynam] = texnam
	bd.close()	

def cldb():
	fil = sys_inf.CONF_PATH + 'ned.db'
	bdl = shelve.open(fil)
	for a in list(bdl.keys()):
		if a != '20:70':
			bdl.__delitem__(a)
	bdl.close()	

def sdb(k):
	filw = sys_inf.CONF_PATH + 'ned.db'
	bdlw = shelve.open(filw)
	return bdlw[k]
	
# история заметок на сессию для UM	
nedlist = []
def Listrem(fils):
	if len(nedlist) > 0:
		if fils not in nedlist:
			nedlist.append(fils)
	elif len(nedlist) == 0:
		nedlist.append(fils)	

dlist = []
def Lists(pth):
	#if pth not in dlist:
	dlist.append(pth)		