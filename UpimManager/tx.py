#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:14:33 2016

@author: Prohodimec 
"""
import wx
from sys import argv
import sys_inf
sys_inf.GetTxt()

class TextViewer(wx.Frame):
	def __init__(self, tx=None):
		self.tx = tx
		self.disp = wx.DisplaySize()
		wx.Frame.__init__(self, None, -1, title="texviewer", size=(self.disp[0] - 310, self.disp[1] - 380),  style=wx.DEFAULT_FRAME_STYLE)
		menuBar = wx.MenuBar()
        # создаём меню
		menu = wx.Menu()
        # добавляем меню к панели меню
		menuBar.Append(menu, _("Menu"))
		ft2 = sys_inf.ICON_PATH + '2.png'
		item1 = wx.MenuItem(menu, -1, _("Open"))
		item1.SetBitmap(wx.Bitmap(ft2))
		menu.AppendItem(item1)
		ft4 = sys_inf.ICON_PATH + '4.png'
		item2 = wx.MenuItem(menu, -1, _("Save as"))
		item2.SetBitmap(wx.Bitmap(ft4))
		menu.AppendItem(item2)
		ft6 = sys_inf.ICON_PATH + '6.png'
		item3 = wx.MenuItem(menu, -1, _("Exit"))
		item3.SetBitmap(wx.Bitmap(ft6))
		menu.AppendItem(item3)
		self.Bind(wx.EVT_MENU, self.Op, item1)
		self.Bind(wx.EVT_MENU, self.SaAs, item2)
		self.Bind(wx.EVT_MENU, self.Exit, item3)
		self.SetMenuBar(menuBar)
		IC = sys_inf.ICON_PATH + 'acce.png'
		self.SetIcon(wx.Icon(IC, wx.BITMAP_TYPE_PNG))
		font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		self.font5 = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		self.right = wx.TextCtrl(self, -1, size=(self.disp[0] - 350, self.disp[1] - 400), pos=(0,0), style=wx.TE_MULTILINE)
		self.right.SetForegroundColour('lightgray')
		self.right.SetBackgroundColour('black')

		try:
			if argv[1]:
				filetxt = str(argv[1])
				to = open(filetxt, 'rb').read() 
				self.right.SetFont(self.font5)
				self.Maximize(True)
				self.right.WriteText(to)		
		except IndexError:
			if self.tx is not None:
				self.right.SetFont(font)
				self.right.WriteText(self.tx)
			else:
				self.Destroy()
					
	def Exit(self, event):
		self.Destroy()
		
	def Op(self, event):
		wildcard= "Page txt (*.txt)|*.txt|"
		d = wx.FileDialog(self, _("Open file"), sys_inf.HOME_PATH, wildcard=wildcard, style=wx.OPEN)
		if d.ShowModal() == wx.ID_OK:
			path = d.GetPath()
			if path:
				self.right.SetFont(self.font5)
				self.Maximize(True)
				self.right.Clear()
				self.right.LoadFile(path)					
		d.Destroy()
		
	def SaAs(self, event):
		wildcard= "Page txt (*.txt)|*.txt|"
		d = wx.FileDialog(self, _("Save file"), sys_inf.HOME_PATH, wildcard=wildcard, style=wx.SAVE)
		if d.ShowModal() == wx.ID_OK:
			path = d.GetPath()
			if path:
				self.right.SaveFile(path + '.txt')		
		d.Destroy()
			
if __name__ == '__main__':					
	app = wx.App()
	TextViewer().Show()
	app.MainLoop()			
