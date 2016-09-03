#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import os
import sys_inf
sys_inf.GetTxt()

class Treya():
	def __init__(self):
		self.tray = gtk.StatusIcon()
		self.tray.connect("activate", self.Showm)
		self.tray.connect("popup-menu", self.showm)
		self.menu = gtk.Menu()
		img = gtk.Image()
		img.set_from_file(sys_inf.ICON_PATH + 'upm.png')
		upmimg = gtk.ImageMenuItem(_("Show Upim"))
		upmimg.set_image(img)
		upmimg.connect("activate", self.Upshow)
		self.menu.append(upmimg)
		img4 = gtk.Image()
		img4.set_from_file(sys_inf.ICON_PATH + 'upw.png')
		upimw = gtk.ImageMenuItem(_("Show Writer"))
		upimw.set_image(img4)
		upimw.connect("activate", self.Upwshow)
		self.menu.append(upimw)
		img2 = gtk.Image()
		img2.set_from_file(sys_inf.ICON_PATH + 'nas1.png')
		nas = gtk.ImageMenuItem(_("Settings"))
		nas.set_image(img2)
		nas.connect("activate", self.Wrshow)
		self.menu.append(nas)
		img3 = gtk.Image()
		img3.set_from_file(sys_inf.ICON_PATH + '6.png')
		vux = gtk.ImageMenuItem(_("Exit"))
		vux.set_image(img3)
		vux.connect("activate", gtk.main_quit)
		self.menu.append(vux)
		self.tray.set_tooltip(_("Calendar"))
		fil = sys_inf.ICON_PATH + 'clen.png'
		pixbuf = gtk.gdk.pixbuf_new_from_file(fil)
		self.tray.set_from_pixbuf(pixbuf)
		gtk.main()		
	
	def showm(self, status_icon, button, time):
		self.menu.show_all()
		self.menu.popup(None, None, None, button, time)
		
	def Upshow(self, widget):
		os.system('python ' + sys_inf.UPIM_PATH + 'DIARY.py &') 
	def Upwshow(self, widget):
		os.system('python ' + sys_inf.UPIM_PATH + 'panel_richtext.py &')
	def Wrshow(self, widget):
		os.system('python ' + sys_inf.UPIM_PATH + 'configuration.py &') 	

	def Showm(self, widget):	
		if os.path.exists('/tmp/look'):
			os.system('mpg123 -q --gain 30 ' + '/usr/local/share/upim/Music/chpok.mp3 &')
			fl = open('/tmp/look', 'rb').read()
			os.kill(int(fl), 9)
			os.remove('/tmp/look')
		else:
			x,y,z = gtk.status_icon_position_menu(self.menu, self.tray)	
			os.system('mpg123 -q --gain 30 ' + '/usr/local/share/upim/Music/dzin.mp3 &')
			os.system('python ' + sys_inf.UPIM_PATH + 'Calendar.py ' + str(x) + ' ' + str(y) + ' &')	
	
Treya()		

