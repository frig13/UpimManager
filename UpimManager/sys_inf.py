# -*- coding: utf-8 -*-
# наш rc.config

def GetTxt():
	import gettext
	gettext.textdomain('upim')
	gettext.install('upim', '/usr/local/share/locale')
	gettext.bindtextdomain('upim', '/usr/local/share/locale')

def Name_User():
	import getpass
	return getpass.getuser()
	
def Loc():
	import locale
	return locale.getdefaultlocale()[0]

def Sizer():#возможны нелепости, ибо не проверено на всех size-трах!
	from wx import DisplaySize
	displ = DisplaySize()
	if displ[1] <= 600:
		y = 270 # ширина панели трея
		z = displ[1]/5.2# высота визора заметок менеджера
		b = displ[0]/14.8#делители ширины
		c = displ[1]/12.7#-высоты гридеров календаря
		d = displ[0]/4.92#высота панели трея
		e = displ[1]/40.9#делители ширины
		f = displ[0]/13.8#-высоты гридеров недели
		g = displ[0]/3.2# ширина текстового визора дней
	elif 600 < displ[1] <= 800:
		y = displ[1]/2.13
		z = displ[1]/3.9
		b = displ[0]/13.2
		c = displ[1]/11.7
		d = displ[0]/4.92
		e = displ[1]/40.9
		f = displ[0]/15
		g = displ[0]/2.9
	elif 801 < displ[1] <= 1124:
		y = displ[0]/2.8
		z = displ[1]/3.7
		b = displ[0]/12.8
		c = displ[1]/11.7
		d = displ[0]/4.92
		e = displ[1]/40.9
		f = displ[0]/13.8
		g = displ[0]/2.7
	elif displ[1] >= 1200:
		y = 540
		z = displ[1]/3.7	
		b = displ[0]/12.8
		c = displ[1]/11.7
		d = displ[0]/4.92
		e = displ[1]/40.9
		f = displ[0]/13.8
		g = displ[0]/2.7
	dis = (displ[0], displ[1], y, z, b, c, d, e, f, g)
	return dis
	
def Cal_Slov(idz):# кончать издеваться над руссо-программисто!!!
	slov1 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	slov2 = ['Пнд', 'Втр', 'Срд', 'Чтв', 'Птн', 'Суб', 'Вс']
	slov3 = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
	slov4 = ['Пн.', 'Вт.', 'Ср.', 'Чт.', 'Пт.', 'Сб.', 'Вс.']
	if idz in slov1:
		lists = slov1
	elif idz in slov2:
		lists = slov2
	elif idz in slov3:
		lists = slov3
	elif idz in slov4:
		lists = slov4
	return lists		

def Once():#нули впереди можно и опустить, иное дело - нули сзади!
	import time
	if time.strftime('%d') == '01':
		a = '1'
	elif time.strftime('%d') == '02':
		a = '2'
	elif time.strftime('%d') == '03':
		a = '3'
	elif time.strftime('%d') == '04':
		a = '4'
	elif time.strftime('%d') == '05':
		a = '5'
	elif time.strftime('%d') == '06':
		a = '6'
	elif time.strftime('%d') == '07':
		a = '7'
	elif time.strftime('%d') == '08':
		a = '8'	
	elif time.strftime('%d') == '09':
		a = '9'	
	elif int(time.strftime('%d')) >= 10:
		a = time.strftime('%d')	
	return a
		
# импортируемые пути
#from distutils import sysconfig
#sysconfig.get_python_lib()
CONF_PATH = '/home/' + Name_User() + '/.config/Upim/'
ICON_PATH = '/usr/local/share/upim/icon/'
UPIM_PATH = '/usr/local/lib/python2.7/dist-packages/UpimManager/'
DATA_PATH = '/home/' + Name_User() + '/.Upim/'
HOME_PATH = '/home/' + Name_User() + '/'