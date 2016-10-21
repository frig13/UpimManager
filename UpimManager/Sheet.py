#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on Fri Feb 14 16:14:33 2016

@author: Prohodimec 
"""
from wx.lib import sheet
import wx
import conf_db
import time
import shelve
import sys_inf
sys_inf.GetTxt()

class NedSheet(sheet.CSheet):
	def __init__(self, parent):
		sheet.CSheet.__init__(self, parent)
		
		self.row = self.col = 0
		self.SetNumberRows(18)
		self.SetNumberCols(7)
		
		self.day = time.strftime('%a')
		
		self.dt = wx.DateTime()
		
		if sys_inf.Loc() == 'ru_RU':
			self.etc = 'Сег.'
		else:
			self.etc = 'Day'
		
		self.pn = sys_inf.Cal_Slov(self.day)[0]
		self.SetColLabelValue(0, self.pn)
		self.vt = sys_inf.Cal_Slov(self.day)[1]
		self.SetColLabelValue(1, self.vt)
		self.sr = sys_inf.Cal_Slov(self.day)[2]
		self.SetColLabelValue(2, self.sr)
		self.ct = sys_inf.Cal_Slov(self.day)[3]
		self.SetColLabelValue(3, self.ct)
		self.ptn = sys_inf.Cal_Slov(self.day)[4]
		self.SetColLabelValue(4, self.ptn)
		self.sb = sys_inf.Cal_Slov(self.day)[5]
		self.SetColLabelValue(5, self.sb)
		self.vs = sys_inf.Cal_Slov(self.day)[6]
		self.SetColLabelValue(6, self.vs)
		
		self.disp = sys_inf.Sizer()
		
		self.Bazned()
		
		font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		font2 = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		
		self.SetDefaultCellFont(font2)
		self.SetLabelFont(font)
		self.SetDefaultCellTextColour('black')
		self.SetGridLineColour('#A52A2A')
		self.SetLabelBackgroundColour(conf_db.Dobd_class('cvetdney').baz_vst())
		self.SetDefaultCellBackgroundColour(conf_db.Dobd_class('cvetchc').baz_vst())
		self.SetCellHighlightColour('#1E90FF')

     
		for i in range(18):
			self.SetRowSize(i, self.disp[7])
		for i in range(18):
			self.SetRowLabelValue(i, str(i + 6) + ':' + '00') 
		for i in range(7):
			self.SetColSize(i, self.disp[8])
		
		self.Days()	
# дни 
	def Days(self):
		if self.day == self.pn:
			for i in range(18):
				self.SetCellBackgroundColour(i, 0, '#A0EF7B')
				self.SetCellValue(0, 0, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
		elif  self.day == self.vt:
			for i in range(18):
				self.SetCellBackgroundColour(i, 1, '#A0EF7B')
				self.SetCellValue(0, 1, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
		elif  self.day == self.sr:
			for i in range(18):
				self.SetCellBackgroundColour(i, 2, '#A0EF7B')
				self.SetCellValue(0, 2, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
		elif  self.day == self.ct:
			for i in range(18):
				self.SetCellBackgroundColour(i, 3, '#A0EF7B')
				self.SetCellValue(0, 3, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
		elif  self.day == self.ptn:
			for i in range(18):
				self.SetCellBackgroundColour(i, 4, '#A0EF7B')
				self.SetCellValue(0, 4, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
		elif  self.day == self.sb:
			for i in range(18):
				self.SetCellBackgroundColour(i, 5, '#A0EF7B')
				self.SetCellValue(0, 5, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
		elif  self.day == self.vs:
			for i in range(18):
				self.SetCellBackgroundColour(i, 6, '#A0EF7B')
				self.SetCellValue(0, 6, self.etc + ' ' + sys_inf.Once() + ' ' + time.strftime('%h'))
				
					
			
# при изменении щита, сохр. в базе	
	def OnCellChange(self, event):
		self.row, self.col = event.GetRow(), event.GetCol()
		kl = str(self.row) + ':' +str(self.col)
		vl = self.GetCellValue(self.row, self.col)
		conf_db.dbdb(kl, vl)
		
# основная разводящая функция
	def Bazned(self):
		filsk = sys_inf.CONF_PATH + 'ned.db'
		bdm = shelve.open(filsk)
		for i in list(bdm.keys()):
			if i != '20:70':
				a = str(i).split(':')[0]
				b = str(i).split(':')[1]
				self.SetCellValue(int(a), int(b), bdm[i])
		bdm.close()
		
	# меню очистки щита	
	def OnRightClick(self, event):
		menu = wx.Menu()
		im = sys_inf.ICON_PATH + 'cut.png'
		item = wx.MenuItem(menu, -1, _('Clear'))
		item.SetBitmap(wx.Bitmap(im))
		menu.AppendItem(item)
		self.Bind(wx.EVT_MENU, self.Cl, item)
		self.PopupMenu(menu)
		
	def Cl(self, event):
		self.ClearGrid()
		conf_db.cldb()
		self.Days()
    
