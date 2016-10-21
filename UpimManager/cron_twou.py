#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:14:33 2016

@author: Prohodimec 
"""

import time
import os
import sys_inf

# простой скрипт ежесекундно сканирующий файл напоминаний; должен быть в автозагрузке, если эти угодны.
def Cron_Twoy():
	file_open = sys_inf.CONF_PATH + '.diarus.ini'
	for i in open(file_open).readlines():
		vremya  = i.split(';')[0]
		commands = i.split(';')[1]
		files = i.split(';')[2]
		music = i.split(';')[3]
		if vremya.split(':')[0] == '00':
			vr = vremya.split(':')[3] + ':' + vremya.split(':')[4] + ':' + vremya.split(':')[5]
			if vr == time.strftime('%H:%M:%S'):
				if commands != 'Not command':
					os.system(commands + ' &')
				if files != 'Not file':
					os.system('panel_richtext ' + '\"' + files + '\"' + ' &')
				if music != 'Not music':
					os.system('mpg123 -q -g 50 ' + music + ' &')
		else:
			if vremya == time.strftime('%d:%m:%G:%H:%M:%S'):
				if commands != 'Not command':
					os.system(commands + ' &')
				if files != 'Not file':
					os.system('panel_richtext ' + '\"' + files + '\"' + ' &')
				if music != 'Not music':
					os.system('mpg123 -q -g 50 ' + music+ ' &')
while True:
	time.sleep(1)
	Cron_Twoy()
