#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:14:33 2015

@author: Prohodimec 
"""
# первый модуль на wx, пусть быдлокод, но работает
import wx, os
from sys_inf import GetTxt
from sys_inf import HOME_PATH
import wx.lib.imagebrowser as imagebrowser
GetTxt()

class TestFrame(wx.Frame): 
	def __init__(self, top):
		self.top = top
		dg = imagebrowser.ImageDialog(None, HOME_PATH)
		dg.SetSize((500, 400))		
		if dg.ShowModal() == wx.ID_OK:
			n = dg.GetFile() 
		dg.Destroy()
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
		self.sp2 = wx.SplitterWindow(self)
		self.sp2.SetBorderSize(0)
		self.p = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER) 
		self.p2 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER) 
		self.p3 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER) 
		self.p4 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p5 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p6 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p7 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p8 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p9 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p10 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p11 = wx.Panel(self.sp2, size=self.wig, style=wx.SUNKEN_BORDER)
		self.p2.Hide()   
		self.p3.Hide()  
		self.p4.Hide()
		self.p5.Hide()
		self.p6.Hide()
		self.p7.Hide()
		self.p8.Hide()
		self.p9.Hide()
		self.p10.Hide()
		self.p11.Hide()
		wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(self.img1), pos=(0,31))
		buttons_cb = wx.Button(self.p, -1, ":80%",size=(60, 30), pos=(0, 0))
		buttons_cb.Bind(wx.EVT_BUTTON, self.Tu, buttons_cb)
		buttons_wb = wx.Button(self.p, -1, ":60%",size=(60, 30), pos=(61, 0))
		buttons_wb.Bind(wx.EVT_BUTTON, self.Fu, buttons_wb)
		buttons_cs = wx.Button(self.p, -1, ":40%", size=(60, 30), pos=(122, 0))
		buttons_cs.Bind(wx.EVT_BUTTON, self.sy, buttons_cs)
		buttons_ce = wx.Button(self.p, -1, ":20%", size=(60, 30), pos=(183, 0))
		buttons_ce.Bind(wx.EVT_BUTTON, self.oy, buttons_ce)
		buttons_cw = wx.Button(self.p, -1, ":10%", size=(60, 30), pos=(244, 0))
		buttons_cw.Bind(wx.EVT_BUTTON, self.iy, buttons_cw)
		buttons_ct = wx.Button(self.p, -1, ":5%", size=(60, 30), pos=(305, 0))
		buttons_ct.Bind(wx.EVT_BUTTON, self.yy, buttons_ct)
		buttons_cans = wx.Button(self.p, -1, _("Write"), size=(70, 30), pos=(386, 0))
		buttons_cans.Bind(wx.EVT_BUTTON, self.cansel, buttons_cans)
		txtd = str(self.w) + "x" + str(self.h)
		txton = wx.StaticText(self.p, -1, txtd, pos=(465,5), size=(60, 30))
		txton.SetForegroundColour('lightgray')
		

	def Once(self, num, op, pan):
		if op == "de":
			img2 = self.img1.Scale(self.w/num, self.h/num) 
			txtd = str(int(self.w/num)) + "x" + str(int(self.h/num))
		if op == "um":
			img2 = self.img1.Scale(self.w*num, self.h*num) 
			txtd = str(int(self.w*num)) + "x" + str(int(self.h*num))
		self.sp2.Unsplit()
		bcb = wx.Button(pan, -1, "*1/5r",size=(60, 30), pos=(0, 0))
		bcb.Bind(wx.EVT_BUTTON, self.Tu2, bcb)
		bwb = wx.Button(pan, -1, "*2/5r",size=(60, 30), pos=(61, 0))
		bwb.Bind(wx.EVT_BUTTON, self.Fu2, bwb)
		bcs = wx.Button(pan, -1, "*3/5r", size=(60, 30), pos=(122, 0))
		bcs.Bind(wx.EVT_BUTTON, self.sy2, bcs)
		bce = wx.Button(pan, -1, "*5r", size=(60, 30), pos=(183, 0))
		bce.Bind(wx.EVT_BUTTON, self.oy2, bce)
		bwr = wx.Button(pan, -1, _("Write"), size=(70, 30), pos=(366, 0))
		bwr.Bind(wx.EVT_BUTTON, self.write, bwr)
		self.data = img2
		txton = wx.StaticText(pan, -1, txtd, pos=(445, 5), size=(60, 30))
		wx.StaticBitmap(pan, -1, wx.BitmapFromImage(img2), pos=(0, 31)) 
		self.sp2.SplitHorizontally(self.p, pan, self.initpos)
		self.Fit()
		
	def Tu(self, event):
		self.Once(1.5, "de", self.p2)
	def Fu(self, event):
		self.Once(2.5, "de", self.p3)
	def sy(self, event):
		self.Once(3.5, "de", self.p4)
	def oy(self, event):
		self.Once(5, "de", self.p5)
	def iy(self, event):
		self.Once(6.5, "de", self.p6)	
	def yy(self, event):
		self.Once(8, "de", self.p7)
	def Tu2(self, event):
		self.Once(1.5, "um", self.p8)
	def Fu2(self, event):
		self.Once(2.5, "um", self.p9)
	def sy2(self, event):
		self.Once(3.5, "um", self.p10)
	def oy2(self, event):
		self.Once(5, "um", self.p11)
	def write(self, event):
		self.top.WriteImage(self.data)
		self.Destroy()
	def cansel(self, event):
		self.top.WriteImage(self.img1)
		self.Destroy()
		

if __name__ == '__main__':
	app = wx.PySimpleApp() 
	TestFrame(None).Show() 
	app.MainLoop()
