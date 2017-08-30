#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue aug 28 19:42:29 2017

@author: prohodimec
"""
import wx
import os
import time
import conf_db
import sys_inf
sys_inf.GetTxt()
import shelve
import wx.lib.analogclock as clock

class Day_pan(wx.Panel):
	def __init__(self, parent, edtr):
		wx.Panel.__init__(self, parent=parent, style=wx.VSCROLL)
		self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
		self.SetBackgroundColour(conf_db.Dobd_class('cvettr').baz_vst())
		self.edtr = edtr
		self.dis = sys_inf.Sizer()
		font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		font2 = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		font3 = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		if conf_db.Dobd_class('colorviz').baz_vst() == '#FFFFFF':
			cvt = '#000000'
		else:
			cvt = '#FFFFFF'
		zdch = wx.StaticText(self, -1, time.strftime('%A'), (self.dis[1]/3.7, 5))
		zdch.SetFont(font)
		zdch.SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		dch = wx.StaticText(self, -1, time.strftime('%d'), (self.dis[1]/3.8,47))
		dch.SetFont(font2)
		dch.SetForegroundColour('red')
		Cdch = wx.StaticText(self, -1, time.strftime('%b.'), (self.dis[1]/3, 50))
		Cdch.SetFont(font)
		Cdch.SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		cl = clock.AnalogClock(self, size=(100, 100), pos=(10, 10))
		cl.SetForegroundColour('green')
		if sys_inf.Loc() == 'ru_RU':
			dg = 'г.'
		else:
			dg = 'y.'
		gd  = wx.StaticText(self, -1, time.strftime('%G'), (self.dis[1]/2.4, 45))
		gd.SetFont(font2)
		gd.SetForegroundColour('blue')
		gdt  = wx.StaticText(self, -1, dg, (self.dis[1]/1.95, 52))
		gdt.SetFont(font)
		gdt.SetForegroundColour(cvt)
				
		
		files = sys_inf.CONF_PATH + 'prz.ini'
		for i in open(files, 'rb').readlines():
			if time.strftime('%d') + ':' + time.strftime('%h') == i.split(';')[0]:
				day = i.split(';')[1]
				self.SmPaste(sys_inf.ICON_PATH + '12s.png')
				break
			else:
				if time.strftime('%A') == _("Saturday"):
					day = _('Pre-holiday')
					self.SmPaste(sys_inf.ICON_PATH + '14s.png')
				elif time.strftime('%A') == _("Sunday"):
					day = _('Holiday')
					self.SmPaste(sys_inf.ICON_PATH + '12s.png')
				else:
					day = _('Weekday')
					self.SmPaste(sys_inf.ICON_PATH + '11s.png')
		dl = wx.StaticText(self, -1, day, (self.dis[1]/3.5,90))
		dl.SetFont(font3)
		dl.SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		
		self.font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		self.font2 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		
	# распорядок по цвету
		wx.StaticLine(self, -1, (12, self.dis[1]/7.3-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if 6 <= int(time.strftime('%H'))  < 8:
			wx.StaticText(self, -1, '06:00', (5, self.dis[1]/7.3)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '06:00', (5, self.dis[1]/7.3)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/6-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  8 <= int(time.strftime('%H'))  < 10:
			wx.StaticText(self, -1, '08:00', (5, self.dis[1]/6)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '08:00', (5, self.dis[1]/6)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/5-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  10 <= int(time.strftime('%H'))  < 12:
			wx.StaticText(self, -1, '10:00', (5,  self.dis[1]/5)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '10:00', (5, self.dis[1]/5)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/4.3-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  12 <= int(time.strftime('%H'))  < 14:
			wx.StaticText(self, -1, '12:00', (5, self.dis[1]/4.3)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '12:00', (5, self.dis[1]/4.3)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/3.8-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  14 <= int(time.strftime('%H'))  < 16:
			wx.StaticText(self, -1, '14:00', (5, self.dis[1]/3.8)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '14:00', (5, self.dis[1]/3.8)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/3.4-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  16 <= int(time.strftime('%H'))  < 18:
			wx.StaticText(self, -1, '16:00', (5, self.dis[1]/3.4)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '16:00', (5, self.dis[1]/3.4)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/3.1-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  18 <= int(time.strftime('%H'))  < 20:
			wx.StaticText(self, -1, '18:00', (5, self.dis[1]/3.1)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '18:00', (5, self.dis[1]/3.1))
		wx.StaticLine(self, -1, (12, self.dis[1]/2.85-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL)
		if  20 <= int(time.strftime('%H'))  < 22:
			wx.StaticText(self, -1, '20:00', (5, self.dis[1]/2.85)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '20:00', (5, self.dis[1]/2.85)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/2.6-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  22 <= int(time.strftime('%H'))  :
			wx.StaticText(self, -1, '22:00', (5, self.dis[1]/2.6)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '22:00', (5, self.dis[1]/2.6)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/2.4-5), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if  0 <= int(time.strftime('%H'))  < 6:
			wx.StaticText(self, -1, '00:00', (5, self.dis[1]/2.4)).SetForegroundColour('red')
		else:
			wx.StaticText(self, -1, '00:00', (5, self.dis[1]/2.4)).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		wx.StaticLine(self, -1, (12, self.dis[1]/2.25), (self.dis[1]/1.4, 5), style=wx.LI_HORIZONTAL).SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		self.RmItem()
		self.ScanBD()
		self.FindDIARY()
		
		
# чёртовы смайлы	
	def Smile(self, path):
		bs = shelve.open(sys_inf.CONF_PATH + 'day.db')
		bs[time.strftime('%d') + ':' + time.strftime('%m') + ':' + time.strftime('%G') + '_' + 'sm' + '_(111, 000)'] = path
		bs.close()
	
	def SmPaste(self, pth):
		bsm = shelve.open(sys_inf.CONF_PATH + 'day.db')
		if 'sm' in str(bsm.keys()):
			for i in list(bsm.keys()):
				if i.split('_')[1] == 'sm':
					image = bsm[i]
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(image, wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)
			self.zg.Bind(wx.EVT_BUTTON, self.ZAG, self.zg)
		else:
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(pth, wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)
			self.zg.Bind(wx.EVT_BUTTON, self.ZAG, self.zg)
		bsm.close()
		
# чёртовы смайлы	
	def ZAG(self, event):
		menus = wx.Menu()
		it0 = wx.MenuItem(menus, -1, _("Choise smiley day"))
		menus.AppendItem(it0)	
		menus.AppendSeparator()
		im1 = sys_inf.ICON_PATH + '11s.png'
		it1 = wx.MenuItem(menus, 1, '')
		it1.SetBitmap(wx.Bitmap(im1))
		menus.AppendItem(it1)	
		im2 = sys_inf.ICON_PATH + '12s.png'
		it2 = wx.MenuItem(menus, 2, '')
		it2.SetBitmap(wx.Bitmap(im2))
		menus.AppendItem(it2)
		im3 = sys_inf.ICON_PATH + '13s.png'
		it3 = wx.MenuItem(menus, 3, '')
		it3.SetBitmap(wx.Bitmap(im3))
		menus.AppendItem(it3)
		im4 = sys_inf.ICON_PATH + '14s.png'
		it4 = wx.MenuItem(menus, 4, '')
		it4.SetBitmap(wx.Bitmap(im4))
		menus.AppendItem(it4)		
		im5 = sys_inf.ICON_PATH + '15s.png'
		it5 = wx.MenuItem(menus, 5, '')
		it5.SetBitmap(wx.Bitmap(im5))
		menus.AppendItem(it5)	
		im6 = sys_inf.ICON_PATH + '16s.png'
		it6 = wx.MenuItem(menus, 6, '')
		it6.SetBitmap(wx.Bitmap(im6))
		menus.AppendItem(it6)
		im7 = sys_inf.ICON_PATH + '17s.png'
		it7 = wx.MenuItem(menus, 7, '')
		it7.SetBitmap(wx.Bitmap(im7))
		menus.AppendItem(it7)
		im8 = sys_inf.ICON_PATH + '18s.png'
		it8 = wx.MenuItem(menus, 8, '')
		it8.SetBitmap(wx.Bitmap(im8))
		menus.AppendItem(it8)
		im9 = sys_inf.ICON_PATH + '19s.png'
		it9 = wx.MenuItem(menus, 9, '')
		it9.SetBitmap(wx.Bitmap(im9))
		menus.AppendItem(it9)	
		self.Bind(wx.EVT_MENU, self.Por, it1)
		self.Bind(wx.EVT_MENU, self.Por, it2)
		self.Bind(wx.EVT_MENU, self.Por, it3)
		self.Bind(wx.EVT_MENU, self.Por, it4)
		self.Bind(wx.EVT_MENU, self.Por, it5)
		self.Bind(wx.EVT_MENU, self.Por, it6)
		self.Bind(wx.EVT_MENU, self.Por, it7)
		self.Bind(wx.EVT_MENU, self.Por, it8)
		self.Bind(wx.EVT_MENU, self.Por, it9)
		self.PopupMenu(menus)
		
# чёртовы смайлы
	def Por(self, event):
		if event.GetId() == 1:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '11s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)
			self.Smile(sys_inf.ICON_PATH + '11s.png')
		elif event.GetId() == 2:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '12s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)
			self.Smile(sys_inf.ICON_PATH + '12s.png')
		elif event.GetId() == 3:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '13s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)	
			self.Smile(sys_inf.ICON_PATH + '13s.png')
		elif event.GetId() == 4:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '14s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)	
			self.Smile(sys_inf.ICON_PATH + '14s.png')
		elif event.GetId() == 5:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '15s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)	
			self.Smile(sys_inf.ICON_PATH + '15s.png')
		elif event.GetId() == 6:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '16s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)	
			self.Smile(sys_inf.ICON_PATH + '16s.png')
		elif event.GetId() == 7:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '17s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)	
			self.Smile(sys_inf.ICON_PATH + '17s.png')
		elif event.GetId() == 8:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '18s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)
			self.Smile(sys_inf.ICON_PATH + '18s.png')
		elif event.GetId() == 9:
			self.zg.Destroy()
			self.zg = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + '19s.png', wx.BITMAP_TYPE_PNG), pos=(self.dis[1]-self.dis[1]/3, 7), style=wx.NO_BORDER)	
			self.Smile(sys_inf.ICON_PATH + '19s.png')
		self.Bind(wx.EVT_BUTTON, self.ZAG, self.zg)	
			
# Mouse Event
	def OnMouseEvent(self, event):
		if event.RightDown() == True:
			self.cord = event.GetPosition()
			if self.dis[1]/7.3 < self.cord[1] < self.dis[1]/2.25:
				if 20 < self.cord[0] < self.dis[1]-self.dis[1]/3:
					menu = wx.Menu()
					im1 = sys_inf.ICON_PATH + 'cut4.png'
					it1 = wx.MenuItem(menu, 1, _('Add notes'))
					it1.SetBitmap(wx.Bitmap(im1))
					menu.AppendItem(it1)	
					im2 = sys_inf.ICON_PATH + '4b.png'
					it2 = wx.MenuItem(menu, 2, _('Add image(<50pix)'))
					it2.SetBitmap(wx.Bitmap(im2))
					menu.AppendItem(it2)
					im4 = sys_inf.ICON_PATH + '3.png'
					it4 = wx.MenuItem(menu, 4, _('Save for newday'))
					it4.SetBitmap(wx.Bitmap(im4))
					menu.AppendItem(it4)		
					im5 = sys_inf.ICON_PATH + '5.png'
					it5 = wx.MenuItem(menu, 5, _('Clear old/currday'))
					it5.SetBitmap(wx.Bitmap(im5))
					menu.AppendItem(it5)
					self.Bind(wx.EVT_MENU, self.PasteNotes, it1)
					self.Bind(wx.EVT_MENU, self.PasteImages, it2)
					self.Bind(wx.EVT_MENU, self.Add, it4)
					self.Bind(wx.EVT_MENU, self.ClBase, it5)
					self.PopupMenu(menu)			
		elif event.LeftDown() == True:  		
			try:
				if self.right:
					if self.right.IsEmpty() == False:
						if self.right.IsModified() == True:
							daydb = sys_inf.CONF_PATH + 'day.db'
							bdday = shelve.open(daydb)
							bdday[time.strftime('%d') + ':' + time.strftime('%m') + ':' + time.strftime('%G') + '_' + 't_' + str(self.cord)] = self.right.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')
							bdday.close()
					self.right.Destroy()
			except:
				pass

#сканирование базы данных на сегодня			
	def ScanBD(self):
		bdday = shelve.open(sys_inf.CONF_PATH + 'day.db')
		for i in list(bdday.keys()):
			if int(i.split('_')[0].split(':')[2]) == int(time.strftime('%G')):
				if int(i.split('_')[0].split(':')[1]) == int(time.strftime('%m')):
					if int(i.split('_')[0].split(':')[0]) == int(time.strftime('%d')):
						if i.split('_')[1] == 't':
							idt = int(i.split('_')[2].split('(')[1].split(')')[0].split(',')[0] + i.split('_')[2].split('(')[1].split(')')[0].split(',')[1].split(' ')[1])
							butttxt = wx.BitmapButton(self, idt, wx.Bitmap(sys_inf.ICON_PATH + 'cut4.png', wx.BITMAP_TYPE_PNG), pos=(int(i.split('_')[2].split('(')[1].split(')')[0].split(',')[0]), int(i.split('_')[2].split('(')[1].split(')')[0].split(',')[1])), style=wx.NO_BORDER)	
							butttxt.Bind(wx.EVT_BUTTON, self.Zam, butttxt)
						if i.split('_')[1] == 'i':
							imgd = bdday[i]
							immd = wx.Image(imgd, wx.BITMAP_TYPE_ANY)  
							wx.StaticBitmap(self, -1, wx.BitmapFromImage(immd), pos=(int(i.split('_')[2].split('(')[1].split(')')[0].split(',')[0]), int(i.split('_')[2].split('(')[1].split(')')[0].split(',')[1])))	
		
		bdday.close()

#пасте иконки блокнотика		
	def PasteNotes(self, event):
		but = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + 'cut4ob.png', wx.BITMAP_TYPE_PNG), pos=self.cord, style=wx.NO_BORDER)	
		but.Bind(wx.EVT_BUTTON, self.ZamNew, but)			
	
	def ZamNew(self, event):
		self.TextPad()

# открытие заметок		
	def Zam(self, event):
		try:
			if self.right:
				self.right.Destroy()
		except:
			pass
		bdday = shelve.open(sys_inf.CONF_PATH + 'day.db')
		for i in list(bdday.keys()):
			if int(event.GetId()) == int(i.split('_')[2].split('(')[1].split(')')[0].split(',')[0] + i.split('_')[2].split('(')[1].split(')')[0].split(',')[1].split(' ')[1]):
				if i.split('_')[1] == 't':
					self.TextPad(bdday[i])
		bdday.close()	
		
# notepad	
	def TextPad(self, tx=None):
		if tx != None:
			self.right = wx.TextCtrl(self, -1, size=(200,100), pos=(300, 100), style=(wx.TE_READONLY | wx.TE_MULTILINE))
			self.right.SetBackgroundColour('#B3AE65')
			self.right.SetForegroundColour('blue')	
			self.right.SetFont(self.font)
			self.right.SetValue(tx)
		else:
			self.right = wx.TextCtrl(self, -1, size=(200,100), pos=(300, 130), style=wx.TE_MULTILINE)
			self.right.SetFont(self.font)
			
#сохранение картинок		
	def PasteImages(self, event):
		wildcard= "Image png (*.png)|*png|image jpg (*.jpg)|*.jpg"
		dlg = wx.FileDialog(self, _("Choice image"), sys_inf.DATA_PATH, wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			pathh = dlg.GetPath().encode('utf-8').decode('latin-1').encode('latin-1')
			m = wx.Image(pathh, wx.BITMAP_TYPE_ANY)   
			w = m.GetWidth() 
			h = m.GetHeight() 
			if w < 50:
				if h < 50:
					wx.StaticBitmap(self, -1, wx.BitmapFromImage(m), pos=self.cord)				
					bdday = shelve.open(sys_inf.CONF_PATH + 'day.db')
					bdday[time.strftime('%d') + ':' + time.strftime('%m') + ':' + time.strftime('%G') + '_' + 'i_' + str(self.cord)] = str(pathh)
					bdday.close()
		dlg.Destroy()
		
	
		
# очистка базы по требованию
	def ClBase(self, event):
		bdday = shelve.open(sys_inf.CONF_PATH + 'day.db')
		for i in list(bdday.keys()):
			if int(time.strftime('%G')) - int(i.split('_')[0].split(':')[2]) > 0:
				bdday.__delitem__(i)
			elif int(time.strftime('%m')) - int(i.split('_')[0].split(':')[1]) > 0:
				bdday.__delitem__(i)
			elif int(time.strftime('%m')) - int(i.split('_')[0].split(':')[1]) == 0:
				if int(time.strftime('%d')) - int(i.split('_')[0].split(':')[0]) >= 0:
					bdday.__delitem__(i)
		bdday.close()
		
# панель сохранения на новый день		
	def Add(self, event):
		self.pan = wx.Panel(self, -1, size=(430, 140), pos=(100, 50))
		
		self.txttd = wx.SpinCtrl(self.pan, value=time.strftime('%d'), size=(100, 30), pos=(20, 45), min=1, max=31)
		self.txttm = wx.SpinCtrl(self.pan, value=time.strftime('%m'), size=(100, 30), pos=(155, 45), min=1, max=12)
		self.txttg = wx.SpinCtrl(self.pan, value=time.strftime('%G'), size=(100, 30), pos=(300, 45), min=int(time.strftime('%G')), max=2112)
	
		wx.StaticText(self.pan, -1,_("Save for Newday"),pos=(120, 10)).SetFont(self.font2)
		
		self.ex = buttons.GenButton(self.pan, -1, label=_("Exit"), size=(100, 30), pos=(325, 100))
		self.ex.Bind(wx.EVT_BUTTON, self.Ex, self.ex)
		self.ex.SetBackgroundColour('blue')
		self.sv = buttons.GenButton(self.pan, -1, label=_("Save"), size=(100, 30), pos=(2, 100))
		self.sv.Bind(wx.EVT_BUTTON, self.Sv, self.sv)
		self.sv.SetBackgroundColour('blue')
	
# бинд сохранения расписания на новый день		
	def Sv(self, event):
		if int(self.txttm.GetValue()) < 10:
			mes = '0' + str(self.txttm.GetValue()) 
		else:
			mes = str(self.txttm.GetValue()) 
		chsot = str(self.txttd.GetValue()) + ':' + mes + ':' + str(self.txttg.GetValue())
		db = shelve.open(sys_inf.CONF_PATH + 'day.db')
		for i in list(db.keys()):
			db[chsot + '_' + i.split('_')[1] + '_' + i.split('_')[2]] = db[i]
		db.close()
		self.pan.Destroy()
		
#дестрой
	def Ex(self, event):
		self.pan.Destroy()
		
# автоудаление старых расписаний
	def RmItem(self):
		bdday = shelve.open(sys_inf.CONF_PATH + 'day.db')
		for i in list(bdday.keys()):			
			if int(time.strftime('%G')) - int(i.split('_')[0].split(':')[2]) > 0:
				bdday.__delitem__(i)
			elif int(time.strftime('%m')) - int(i.split('_')[0].split(':')[1]) > 0:
				bdday.__delitem__(i)
			elif int(time.strftime('%m')) - int(i.split('_')[0].split(':')[1]) == 0:
				if int(time.strftime('%d')) - int(i.split('_')[0].split(':')[0]) > 0:
					bdday.__delitem__(i)
		bdday.close()		
		
# доступ к заметкам календаря сего дня		
	def FindDIARY(self):
		self.segp = []
		ftem = time.strftime('%G:%h')
		if os.path.exists(sys_inf.DATA_PATH + 'Data/' + ftem):
			for i in os.listdir(sys_inf.DATA_PATH + 'Data/'):
				if int(i.split(':')[0]) == int(time.strftime('%G')):
					if i.split(':')[1] == time.strftime('%h'): 
						self.pth = sys_inf.DATA_PATH  + 'Data/' + i + '/'
			for c in os.listdir(self.pth):
				if int(c.split(':')[0]) == int(time.strftime('%d')):
					self.segp.append(c)
					fim = sys_inf.ICON_PATH + 'clen.png'
					ifim = wx.Image(fim, wx.BITMAP_TYPE_ANY)
					self.sb = wx.StaticBitmap(self, -1, wx.BitmapFromImage(ifim), pos=(self.dis[1]-self.dis[1]/3.056, 70))
					self.sb.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEv)
			
	def 	OnMouseEv(self, event):
		if event.LeftDown() == True:
			self.menus = wx.Menu()
			for i in self.segp:
				ime = sys_inf.ICON_PATH + 'sear.png'
				it0 = wx.MenuItem(self.menus, -1, i)
				it0.SetBitmap(wx.Bitmap(ime))
				self.menus.AppendItem(it0)	
				self.Bind(wx.EVT_MENU, self.Open, it0)	
			self.PopupMenu(self.menus)
			
	def Open(self, event):
		item = self.menus.FindItemById(event.GetId())
		items = item.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		self.edtr.LoadFile(self.pth + items)
	
	