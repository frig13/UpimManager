#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2017 YEAR

@author: FrIg aka Prohodimec 
"""
import wx 
from sys_inf import GetTxt
from sys_inf import HOME_PATH
import wx.lib.imagebrowser as imagebrowser
GetTxt()
# простенький редактор изображения для вставки в richtxt
class TestFrame(wx.Frame):
	def __init__(self, top):
		self.top = top
		dg = imagebrowser.ImageDialog(None, HOME_PATH)
		dg.SetSize((500, 400))		
		if dg.ShowModal() == wx.ID_OK:
			n = dg.GetFile() 
		dg.Destroy()
		self.orig = wx.Image(n, wx.BITMAP_TYPE_ANY)   
		self.img1 = wx.Image(n, wx.BITMAP_TYPE_ANY)   
		self.w = self.img1.GetWidth() 
		self.h = self.img1.GetHeight()
		ds = wx.DisplaySize()
		self.initpos = ds[1] / 4
		if self.w < 1000:
			self.wig = (ds[0] / 2, ds[1] / 2)
		else:
			self.wig = (ds[0] / 1.2, ds[1] / 1.2)
		wx.Frame.__init__(self, None, title=_("Write image"), size=self.wig) 
		self.sp = wx.SplitterWindow(self, style=wx.SP_NOBORDER)	
		self.p = wx.Panel(self.sp, size=self.wig, style=wx.SUNKEN_BORDER) 
		self.p2 = wx.Panel(self.sp, size=self.wig, style=wx.SUNKEN_BORDER) 
		self.p2.Hide()   
		wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(self.img1), pos=(0,31))
		mon = ['80%', '60%', '40%', '20%', '10%', '5%']
		self.ch =wx.ComboBox(self.p, value='0', choices=mon, size=(102, 30), pos=(32, 0), style=wx.CB_DROPDOWN)
		buttons_cb = wx.Button(self.p, -1, "-",size=(30, 30), pos=(0, 0))
		buttons_cb.Bind(wx.EVT_BUTTON, self.Tu, buttons_cb)
		buttons_cv = wx.Button(self.p, -1, "+",size=(30, 30), pos=(136, 0))
		buttons_cv.Bind(wx.EVT_BUTTON, self.Su, buttons_cv)
		bwr = wx.Button(self.p, -1, _("Write"), size=(90, 30), pos=(444, 0))
		bwr.Bind(wx.EVT_BUTTON, self.write, bwr)
		bor = wx.Button(self.p, -1, "OrigImage", size=(90, 30), pos=(352, 0))
		bor.Bind(wx.EVT_BUTTON, self.Orig, bor)
		buttons_cm = wx.Button(self.p, -1, "Mirror",size=(90, 30), pos=(168, 0))
		buttons_cm.Bind(wx.EVT_BUTTON, self.MuH, buttons_cm)
		buttons_cmv = wx.Button(self.p, -1, "Rotate",size=(90, 30), pos=(260, 0))
		buttons_cmv.Bind(wx.EVT_BUTTON, self.MuV, buttons_cmv)
	
	def Indx(self):
		if self.ch.GetValue() == '80%':
			ind = 1.5
		elif self.ch.GetValue() == '60%':
			ind = 2.5
		elif self.ch.GetValue() == '40%':
			ind = 3.5		
		elif self.ch.GetValue() == '20%':
			ind = 5	
		elif self.ch.GetValue() == '10%':
			ind = 6.5
		elif self.ch.GetValue() == '5%':
			ind = 8
		else:
			ind = 1
		return ind
		
	def Tu(self, event):	
		self.Trp()
		num = self.Indx()
		self.img2 = self.img1.Scale(self.w/num, self.h/num) 
		self.tosim = wx.StaticBitmap(self.p2 , -1, wx.BitmapFromImage(self.img2), pos=(0, 31))
		self.sp.SplitHorizontally(self.p, self.p2, self.initpos)
		
	def Su(self, event):
		self.Trp()
		if self.Indx() == 1:
			num = 1
		else:
			num = 10 - self.Indx()
		self.img2 = self.img1.Scale(self.w*num, self.h*num) 
		self.tosim = wx.StaticBitmap(self.p2 , -1, wx.BitmapFromImage(self.img2), pos=(0, 31))
		self.sp.SplitHorizontally(self.p, self.p2, self.initpos)	
		
	def write(self, event):
		try:
			if self.img2:
				self.top.WriteImage(self.img2)
				self.Destroy()
		except:
			self.top.WriteImage(self.img1)
			self.Destroy()
	
	def MuH(self, event):
		self.Trp()
		self.img2 = self.img1.Mirror(horizontally=True)
		self.tosim = wx.StaticBitmap(self.p2 , -1, wx.BitmapFromImage(self.img2), pos=(0, 31))
		self.sp.SplitHorizontally(self.p, self.p2, self.initpos)

	def MuV(self, event):
		self.Trp()
		self.img2 = self.img1.Rotate(5, (0, 1))
		self.tosim = wx.StaticBitmap(self.p2 , -1, wx.BitmapFromImage(self.img2), pos=(0, 31))
		self.sp.SplitHorizontally(self.p, self.p2, self.initpos)
	
	def Orig(self, event):
		self.img2 = self.orig
		self.Trp()
		self.tosim = wx.StaticBitmap(self.p2 , -1, wx.BitmapFromImage(self.img2), pos=(0, 31))
		self.sp.SplitHorizontally(self.p, self.p2, self.initpos)
	
	def Trp(self):
		try:
			if self.tosim:
				self.img1 = self.img2
				self.tosim.Hide()
				
		except:
			pass	
			
			
			
if __name__ == '__main__':
	app = wx.PySimpleApp() 
	TestFrame(None).Show() 
	app.MainLoop()	