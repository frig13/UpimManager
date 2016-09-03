# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 00:13:26 2016

@author: frig
"""
import os
import sys_inf
from distutils.file_util import copy_file

DP = sys_inf.DATA_PATH
LIST_PATH = [DP, DP + 'Data', DP + 'Other', DP + 'Pattern', DP + 'Text', sys_inf.CONF_PATH]

for pt in LIST_PATH:
	if os.path.exists(pt):
		pass
	else:
		os.mkdir(pt)
		
CONFDB_PATH = sys_inf.CONF_PATH + 'conf.db'
if os.path.exists(CONFDB_PATH):
	pass
else:
	copy_file('/usr/local/share/upim/conf.db', sys_inf.CONF_PATH)
	if os.path.exists('/home/' + sys_inf.Name_User() + '/.config/autostart'):
		pass
	else:
		os.mkdir('/home/' + sys_inf.Name_User() + '/.config/autostart')		
	if os.path.exists('/home/' + sys_inf.Name_User() + '/.config/autostart/cronpy.desktop'):
		pass
	else:
		copy_file('/usr/local/share/upim/cronpy.desktop', '/home/' + sys_inf.Name_User() + '/.config/autostart/cronpy.desktop')
		copy_file('/usr/local/share/upim/gtktray.desktop', '/home/' + sys_inf.Name_User() + '/.config/autostart/gtktray.desktop')
		os.system('python /usr/local/lib/python2.7/dist-packages/UpimManager/cron_twou.py &')
		os.system('python /usr/local/lib/python2.7/dist-packages/UpimManager/gtktray.py &')
	
DIARYINI_PATH = sys_inf.CONF_PATH + '.diarus.ini'
if os.path.exists(DIARYINI_PATH):
	pass
else:
	os.system('touch ' + DIARYINI_PATH)
	
PRZINI_PATH = sys_inf.CONF_PATH + 'prz.ini'	
if os.path.exists(PRZINI_PATH):
	pass
else:
	if os.path.exists('/usr/local/share/upim/prz.ini'):
		copy_file('/usr/local/share/upim/prz.ini', PRZINI_PATH)
	else:
		os.system('touch ' + PRZINI_PATH)
		os.system('echo "31:jan;NewYers"> ' + PRZINI_PATH)
	
SHAB = DP + 'Pattern/shab'
if os.path.exists(SHAB):
	pass
else:
	copy_file('/usr/local/share/upim/shab', SHAB)
	os.system('touch ' + DP + 'Pattern/stock')