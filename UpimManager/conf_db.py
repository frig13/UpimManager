#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2016-2017 year

@author: Prohodimec 
"""
# простенькие функции и классы для работы с bd_shelve
import shelve
import os
import sys_inf

# классы конфигурации
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
			
			
# создание, поиск, удаление			
def Ds(slovo, lists):
	fil = sys_inf.CONF_PATH + 'index.db'
	o = shelve.open(fil)
	for i in list(o.keys()):
		bas = o[i]
		if bas.find(slovo) != -1:
			lists.append(i.split('.')[0])

	o.close()

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

# создание, поиск, удаление	
def catdb(keynam, texnam):
	filc = sys_inf.CONF_PATH + 'cat.db'
	bdcat = shelve.open(filc)
	bdcat[keynam] = texnam
	bdcat.close()
	
def dbcat(knam):
	fc = sys_inf.CONF_PATH + 'cat.db'
	bdct = shelve.open(fc)
	for kl in list(bdct.keys()):
		if  kl == knam:
			return bdct[kl]
	bdct.close()
def rmcat(rmnam):
	frm = sys_inf.CONF_PATH + 'cat.db'
	bdrm = shelve.open(frm)
	for rmn in list(bdrm.keys()):
		if  rmn == rmnam:
			bdrm.__delitem__(rmnam)
	bdrm.close()
	
# создание, поиск, удаление
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
	
# листы для запоминаниия заметок на сессию	
nedlist = []
def Listrem(fils):
	if len(nedlist) > 0:
		if fils not in nedlist:
			nedlist.append(fils)
	elif len(nedlist) == 0:
		nedlist.append(fils)	

dlist = []
def Lists(pth):
	dlist.append(pth)