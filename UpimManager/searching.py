#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:14:33 2016

@author: Prohodimec 
"""
import wx
import os
import sys_inf
import conf_db
import shelve
import tx
sys_inf.GetTxt()

class TabSearh(wx.Panel):
	def __init__(self, parent, wop):
		wx.Panel.__init__(self, parent=parent)
		self.wop = wop
		self.dis = sys_inf.Sizer()
		self.SetMinSize((self.dis[6], self.dis[2]))
		self.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		tf = wx.StaticText(self, -1, _("Find notes"), (55, 4))
		font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		tf.SetFont(font)
		self.tex = wx.TextCtrl(self, -1, _("Write text for searching"), pos=(2, 30), size=(self.dis[6]/1.4, 25))
		self.tex.SetBackgroundColour('black')
		self.tcTrees = wx.TreeCtrl(self, size=(255, self.dis[2] - 60), pos=(2, 60))
		self.tcTrees.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.tcTrees.SetForegroundColour(str(conf_db.Dobd_class('cvetmencr').baz_vst()))
		
		buttons = wx.Button(self, label=_("Search"), size=(64, 25), pos=(self.dis[6]/1.4+5, 30))
		buttons.Bind(wx.EVT_BUTTON, self.Nah, buttons)
		buttons.SetBackgroundColour('#421700')
		self.tcTrees.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.RightClick)
		self.tcTrees.Bind(wx.EVT_TREE_SEL_CHANGED, self.SelChan)
		self.flist = []; self.filelist = []; self.filel = []
		self.root = self.tcTrees.AddRoot(_('Result:'))
		
		im2 = sys_inf.ICON_PATH + 'sear.png'
		im = sys_inf.ICON_PATH + 'ef.png'
		image_list = wx.ImageList(16, 16)
		img = image_list.Add(wx.Image(im, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
		self.img2 = image_list.Add(wx.Image(im2, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
		self.tcTrees.AssignImageList(image_list)
		self.tcTrees.SetItemImage(self.root, img, wx.TreeItemIcon_Normal)

	def Nah(self, event):
		self.Scan()
		self.RmDel()
		if len(self.flist) >= 1:
			del self.flist[:]
			self.tcTrees.DeleteChildren(self.root)
		if self.tex.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') != _("Write text for searching"):
			if self.tex.GetValue() != '':
				self.text_searh = self.tex.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') 
		conf_db.Ds(self.text_searh, self.flist)
		for lis in self.flist:
			itm = self.tcTrees.AppendItem(self.root, lis)
			self.tcTrees.SetItemImage(itm, self.img2, wx.TreeItemIcon_Normal) 
			self.tcTrees.ExpandAll()
			self.tcTrees.SortChildren(self.tcTrees.GetSelection())
			self.tex.Clear()
			self.tex.WriteText(_("Write text for searching"))
			
	def SelChan(self, event):
		item = self.tcTrees.GetSelection()
		tc = self.tcTrees.GetItemText(item).encode('utf-8').decode('latin-1').encode('latin-1')
		for u in self.flist:
			if u == tc:
				self.Loads(u)

					

	def Scan(self):
		pat = [sys_inf.DATA_PATH + 'Data', sys_inf.DATA_PATH + 'Other']
		for patch in pat: 
			for i in os.listdir(patch):
				self.zt = patch + '/' + i
				if os.path.isfile(self.zt):
					pass
				else:
					for files in os.listdir(self.zt):
						ot_fil = self.zt + '/' + files
						self.filelist.append(ot_fil)
						
	def Loads(self, stxt):
		for l in self.filelist:
			ton = l.split('/')[6]
			if ton.split('.')[0] == stxt:
				self.wop.LoadFile(l)	
				conf_db.Listrem(l)
	
	def RmDel(self):
		for p in self.filelist:
			self.filel.append(p.split('/')[6])
		h = shelve.open(sys_inf.CONF_PATH + 'index.db')
		for i in list(h.keys()): 
			if i in self.filel:
				pass
			else:
				h.__delitem__(i)
		h.close()
			
	def RightClick(self, event):
		self.popupmenu = wx.Menu()
		fil = sys_inf.ICON_PATH + 'acce.png'	
		item1 = wx.MenuItem(self.popupmenu, -1, _('Open in text'))
		item1.SetBitmap(wx.Bitmap(fil))
		self.popupmenu.AppendItem(item1)
		self.Bind(wx.EVT_MENU, self.OnPn1, item1)
		fil2 = sys_inf.ICON_PATH + '5.png'	
		item2 = wx.MenuItem(self.popupmenu, -1, _('Clear'))
		item2.SetBitmap(wx.Bitmap(fil2))
		self.popupmenu.AppendItem(item2)
		self.Bind(wx.EVT_MENU, self.OnPn2, item2)
		self.tcTrees.PopupMenu(self.popupmenu)
		self.tcTrees.Layout()
		
	def OnPn1(self, event):
		item = self.tcTrees.GetSelection()
		tc = self.tcTrees.GetItemText(item).encode('utf-8').decode('latin-1').encode('latin-1')
		for u in self.flist:
			if u == tc:
				val = conf_db.searcingdb(u)
				tx.TextViewer(val).Show()

	def OnPn2(self, event):
		self.tcTrees.DeleteChildren(self.root)		
				
			
	
