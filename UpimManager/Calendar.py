#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:14:33 2016

@author: Prohodimec 
"""
import wx
import os
import time
import Caldar
import sys_inf
import validate
from sys import argv
import wx.lib.buttons as buttons
sys_inf.GetTxt()
# упаковка - календарик
class CalenFrame(wx.Frame):
	def __init__(self, parent):	
		wx.Frame.__init__(self, None, wx.ID_ANY, "Calendar",size=(320,252), style=(wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR))
		dis = wx.DisplaySize()
		
		try: # определяем положение фрейма
			if argv[1]:
				if argv[2]:
					x = int(argv[1])
					y = int(argv[2])
		except IndexError:
			x = 428
			y = 131
		if dis[0] - x < 160:
			z = x - 150
		else:
			z = x	
		self.SetPosition((z, y))
		
		i = sys_inf.ICON_PATH + 's.png'
		self.SetIcon(wx.Icon(i, wx.BITMAP_TYPE_PNG))
		self.n = wx.Panel(self, -1, size=(320,240))
		figf = sys_inf.ICON_PATH + 'fon.png'
		imj = wx.Image(figf, wx.BITMAP_TYPE_ANY)
		wx.StaticBitmap(self.n, 104, wx.BitmapFromImage(imj), pos=(0,0))
		font_button = wx.Font(8, wx.ROMAN, wx.NORMAL, wx.BOLD, True)
		bu = buttons.GenButton(self.n, -1, "+G", size=(47,23), pos=(287, 32))
		bu.SetBackgroundColour('#1f44df')
		bu.Bind(wx.EVT_BUTTON, self.Tuda, bu)
		bu.SetFont(font_button)
		but = buttons.GenButton(self.n, -1, "-G",size=(43,23), pos=(0, 32))
		but.Bind(wx.EVT_BUTTON, self.Suda, but)
		but.SetBackgroundColour('#1f44df')
		but.SetFont(font_button)
		seg = buttons.GenButton(self.n, -1, _("Act."), size=(67,23), pos=(44, 32))
		seg.Bind(wx.EVT_BUTTON, self.Seg, seg) 
		seg.SetBackgroundColour('#816B85')
		seg.SetFont(font_button)
		snap = buttons.GenButton(self.n, -1, _("Rem."), size=(78,23), pos=(111, 32))
		snap.Bind(wx.EVT_BUTTON, self.Napom, snap) 
		snap.SetBackgroundColour('#740B19')
		snap.SetFont(font_button)
		butm = buttons.GenButton(self.n, -1, "+M", size=(47,23), pos=(237, 32))
		butm.Bind(wx.EVT_BUTTON, self.Mtuda, butm)
		butm.SetBackgroundColour('#6B6838')
		butm.SetFont(font_button)
		buts = buttons.GenButton(self.n, -1, "-M", size=(47,23), pos=(189, 32))
		buts.Bind(wx.EVT_BUTTON, self.Msuda, buts)
		buts.SetFont(font_button)
		buts.SetBackgroundColour('#6B6838')
		font = wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD, True)
		self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
		self.Troon()
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
	
		

	
		self.goodtxt = wx.StaticText(self.n, -1, time.strftime('%G'), pos=(180,5), size=(80, 30))
		self.goodtxt.SetForegroundColour('#6BFFE5')
		self.goodtxt.SetFont(font)
		if sys_inf.Loc() == 'ru_RU':
			g = 'года'
		elif sys_inf.Loc() == 'en_US':
			g = 'year'
		self.gtxt = wx.StaticText(self.n, -1, g, pos=(240,5), size=(80, 40))
		self.gtxt.SetForegroundColour('lightgray')
		self.gtxt.SetFont(font)
		self.modtxt = wx.StaticText(self.n, -1, self.Ruys(), pos=(70,5), size=(80, 40))
		self.modtxt.SetForegroundColour('gold')
		self.modtxt.SetFont(font)
		self.chistxt = wx.StaticText(self.n, -1, sys_inf.Once(), pos=(35,5), size=(80, 30))
		self.chistxt.SetForegroundColour('lightgray')
		self.chistxt.SetFont(font)
# биндинг		
	def OnMouseEvent(self, event):
		if event.GetPosition()[0] <= 0:
			self.OnCloseWin()
			
	def Napom(self, event):
		os.system('python ' + sys_inf.UPIM_PATH + 'soxr_nap.py &')

	def Tuda(self, event):
		self.Pr(0)
		
		
	def Suda(self, event):
		self.Pr(1)
		
		
	def Mtuda(self, event):
		self.Prm(0)
		self.Room()
		
		
	def Msuda(self, event):
		self.Prm(1)
		self.Room()
		
		
	def Rooyt(self):
		o = str(self.good_f)
		self.goodtxt.SetLabel(o)

	def Room(self):
		io = self.Ruys()
		self.modtxt.SetLabel(io)
		
	def Seg(self, event):	
		self.Pr(2)
		self.Prm(2)
		self.modtxt.SetLabel(time.strftime('%B'))
		
		
# обработка годов	
	def Pr(self, on):
		ds = int(time.strftime('%G'))
		if on == 0:
			try:
				if self.good:
					self.good += 1
			except AttributeError:
				self.good = ds + 1
		if on == 1:
			try:
				if self.good:
					self.good -= 1
			except AttributeError:
				self.good = ds - 1
		if on == 2:
			self.good = ds
		self.Finals_G(self.good)

# обработка месяцев		
	def Prm(self, om):
		if om == 0:
			try:
				if self.me:
					self.me += 1
					if self.me > 12:
						self.me = 1
			except AttributeError:
				self.me = int(time.strftime('%m')) + 1 # если проблемы, смотри здесь
		if om == 1:
			try:
				if self.me:
					self.me -= 1 
					if self.me < 1:
						self.me = 12
			except AttributeError:
				self.me = int(time.strftime('%m')) - 1 # если проблемы, смотри здесь
		if om == 2:
			self.me = int(time.strftime('%m')) # если проблемы, смотри здесь
		self.Finals_M(self.me)	

# посредники года-месяцы		
	def Finals_G(self, ggod):
		try:
			if ggod:
				good_f = ggod
		except AttributeError:
			good_f = int(time.strftime('%G'))
		self.good_f = good_f
		self.Rooyt()
		self.Troon()
		
	def Finals_M(self, mmes):
		self.mes_f = mmes
		self.Ruys()
		self.Troon()
# обобщающая функция		
	def Troon(self):
		try:
			if self.mes_f:
				self.mes = self.mes_f - 1
		except AttributeError:
			self.mes = int(time.strftime('%m')) - 1 
		try:
			if self.good_f:
				self.goo = self.good_f
		except AttributeError:
			self.goo = int(time.strftime('%G'))
		self.Frook(self.mes, self.goo)
		
# Упаковка в боксы		
	def Frook(self, we, ds):
		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		try:
			if self.grid:
				self.grid.Dest()
				self.grid = Caldar.SimpleGrid(self, we, 1, 47, 42, 'Calendar')
		except AttributeError:
			self.grid = Caldar.SimpleGrid(self, we, ds, 1, 47, 42, 'Calendar')
		vbox.Add(self.n)
		vbox.Add(self.grid, 2, wx.EXPAND | wx.ALL, 1)
		hbox.Add(vbox, 1, wx.EXPAND | wx.ALL)
		self.SetSizer(hbox)
		self.Fit()
		self.Layout()
# динамичная функция-индикатор месяца по счётчику
	def Ruys(self):
		try:
			if self.mes_f:
				mesyac = self.mes_f - 1
		except AttributeError:
			mesyac = int(time.strftime('%m')) - 1
		if mesyac == 0:
			self.v = _('january')
		elif mesyac == 1:
			self.v = _('february')
		elif mesyac == 2:
			self.v = _('march')
		elif mesyac == 3:
			self.v = _('april')
		elif mesyac == 4:
			self.v = _('may')
		elif mesyac == 5:
			self.v = _('june')
		elif mesyac == 6:
			self.v = _('july')
		elif mesyac == 7:
			self.v = _('august')
		elif mesyac == 8:
			self.v = _('september')
		elif mesyac == 9:
			self.v = _('october')
		elif mesyac == 10:
			self.v = _('november')
		elif mesyac == 11:
			self.v = _('december')
		return self.v
		
	
# старый добрый look, чтоб десять календарей не нащёлкать	
	def OnCloseWindow(self, event):
		os.remove('/tmp/look')
		self.Destroy()
	def OnCloseWin(self):
		os.remove('/tmp/look')
		self.Destroy()
if os.path.exists('/tmp/look'):
	pass
else:
	f = open('/tmp/look', 'wb')	
	pf = str(os.getpid())
	f.write(pf)
	f.close()
	app = wx.App()
	frame = CalenFrame(None).Show()
	app.MainLoop()
