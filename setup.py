
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import locale
from distutils.file_util import copy_file
import py_compile

if sys.version.split('.')[0] != '2':
	print 'UpimManager requires Python version >= 2.7.5 < 3.x.x'
	sys.exit(0)
try:
	import wx
	if wx.__version__ != '2.8.12.1':
		print 'UpimManager requires the wxPython-2.8.12.1'
		sys.exit(0)
except:
	print ''
	print 'UpimManager requires the wxPython version 2.8.12.1'
	sys.exit(0)

LOC_PREFIX = '/usr/local/'	

try:
	if sys.argv[1] == 'install':
		list_li = ['/usr/local/lib', '/usr/local/share', '/usr/local/share/upim', '/usr/local/lib/python2.7', '/usr/local/lib/python2.7/dist-packages', '/usr/local/lib/python2.7/dist-packages/UpimManager']
		for a in list_li:
			if os.path.exists(a):
				pass
			else:
				os.mkdir(a)
				print 'Create dir: ' +  a + '\n'
		
		for py in os.listdir('UpimManager'):
			copy_file('UpimManager/' + py, '/usr/local/lib/python2.7/dist-packages/UpimManager/' + py)
			py_compile.compile('/usr/local/lib/python2.7/dist-packages/UpimManager/' + py)
			print 'Copyring and compiling files: ' + py + '\n'
			
		if locale.getdefaultlocale()[0].split('_')[0] == 'ru':
			list_pt = [  '/usr/local/share/locale', '/usr/local/share/locale/ru', '/usr/local/share/locale/ru/LC_MESSAGES']
			for pt in list_pt:
				if os.path.exists(pt):
					pass
				else:
					os.mkdir(pt)
					print 'Create dir: ' +  pt + '\n'
			copy_file('Data/locale/upim.mo', '/usr/local/share/locale/ru/LC_MESSAGES/upim.mo')
			print 'Copyring upim.mo\n'
			copy_file('Data/locale/prz.ini', LOC_PREFIX + 'share/upim/prz.ini')
			copy_file('Data/locale/ManualRU.ox', LOC_PREFIX + 'share/upim/ManualRU.ox')
			
		for i in os.listdir('Data/upim'):
			copy_file('Data/upim/' + i, LOC_PREFIX + 'share/upim/' + i)
			print 'Copyring file: ' + i + '\n'
				
		os.mkdir(LOC_PREFIX + 'share/upim/icon')
		for ic in os.listdir('Data/icon'):
			copy_file('Data/icon/' + ic, LOC_PREFIX + 'share/upim/icon/' + ic)
		print 'Copyring icon...\n'
		
		copy_file('Data/Desktop/UpimManager.desktop', '/usr/share/applications/UpimManager.desktop')
		copy_file('Data/Desktop/UpimWriter.desktop', '/usr/share/applications/UpimWriter.desktop')
		print 'Create Desktop files\n'
		
		os.system('ln -s /usr/local/lib/python2.7/dist-packages/UpimManager/panel_richtext.py /usr/bin/panel_richtext')# eue
		print 'Create link: panel_richtext\n'
		
		print "========================================\n Ok! Upim Manager installed successfull\n========================================"
		
	elif sys.argv[1] == 'remove':
		if os.path.exists(LOC_PREFIX + 'lib/python2.7/dist-packages/UpimManager'):
			pass
		else:
			print "Upim Manager not installed!"
			sys.exit(0)
			
		if os.path.exists('/usr/bin/panel_richtext'):
			os.remove('/usr/bin/panel_richtext')
			print 'Removing link panel_richtext\n'
			
		if os.path.exists(LOC_PREFIX + 'share/upim/icon'):	
			for i in os.listdir(LOC_PREFIX + 'share/upim/icon'):
				os.remove(LOC_PREFIX + 'share/upim/icon/' + i)
			print 'Removing icon... Ok!\n'
				
		if os.path.exists(LOC_PREFIX + 'lib/python2.7/dist-packages/UpimManager'):
			for ins in os.listdir(LOC_PREFIX + 'lib/python2.7/dist-packages/UpimManager'):	
				os.remove(LOC_PREFIX + 'lib/python2.7/dist-packages/UpimManager/' + ins)
				print 'Removing \"py\" files: ' + ins + '\n'
			
		if os.path.exists(LOC_PREFIX + 'share/upim/'):
			for d in os.listdir(LOC_PREFIX + 'share/upim/'):
				if os.path.isfile(LOC_PREFIX + 'share/upim/' + d):
					os.remove(LOC_PREFIX + 'share/upim/' + d)
					print 'Removing conf. files: ' + d + '\n'

		if os.path.exists('/usr/local/share/locale/ru/LC_MESSAGES/upim.mo'):
			os.remove('/usr/local/share/locale/ru/LC_MESSAGES/upim.mo')
			print 'Removing upim.mo\n'
			
		if os.path.exists(LOC_PREFIX + 'share/upim/icon'):	
			os.rmdir(LOC_PREFIX + 'share/upim/icon')
			print 'Removing icon dir\n'
			
		if os.path.exists(LOC_PREFIX + 'lib/python2.7/dist-packages/UpimManager'):
			os.rmdir(LOC_PREFIX + 'lib/python2.7/dist-packages/UpimManager')
			print 'Removing DistUpim dir\n'

		if os.path.exists('/usr/share/applications/UpimManager.desktop'):
			os.remove('/usr/share/applications/UpimManager.desktop')
		if os.path.exists('/usr/share/applications/UpimWriter.desktop'):	
			os.remove('/usr/share/applications/UpimWriter.desktop')
			print 'Removing Desktop files\n'
		
		if os.path.exists(LOC_PREFIX + 'share/upim'):
			os.rmdir(LOC_PREFIX + 'share/upim')
			print 'Removing ShareUpim dir \n'
		
		print "================================================\n Upim Manager removed successfull\n If you remove all files:\n$ rm -rf /home/$USER/.Upim \n$ rm -rf /home/$USER/.config/Upim\n$ rm -rf /home/$USER/.config/autostart/cronpy.desktop\n$ rm -rf /home/$USER/.config/autostart/gtktray.desktop\n================================================"
	else:
		print "--------------\n Stupid enter!\n--------------"
		sys.exit(0)
except IndexError:
	print "=======================================================================\n Enter: \"sudo python setup.py install\" or \"sudo python setup.py remove\"\n======================================================================="
	sys.exit(0)
	

