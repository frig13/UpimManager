#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:14:33 2016

@author: Prohodimec 
"""
import wx
import os
import time
import panel_richtext	
import conf_db
import sys_inf
import tx
sys_inf.GetTxt()

class TabPanel(wx.Panel):
	def __init__(self, parent, wop, pths, names):
		wx.Panel.__init__(self, parent=parent)
		self.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.wop = wop
		self.pths = pths
		self.names = names
		self.dis = sys_inf.Sizer()
		self.SetMinSize((self.dis[6], self.dis[2]))
		self.tcTree = wx.TreeCtrl(self, size=(self.dis[6], self.dis[2]-25), pos=(0, 25))
		
		rec = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + 'rece.png', wx.BITMAP_TYPE_PNG), pos=(0,0), size=(25, 25), style=wx.NO_BORDER)
		rec.Bind(wx.EVT_BUTTON, self.Recent, rec)
		sv = wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + 'cver.png', wx.BITMAP_TYPE_PNG), pos=(30,0), size=(25, 25), style=wx.NO_BORDER)
		sv.Bind(wx.EVT_BUTTON, self.Coll, sv)
		sn	= wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + 'cniz.png', wx.BITMAP_TYPE_PNG), pos=(55,0), size=(25, 25), style=wx.NO_BORDER)	
		sn.Bind(wx.EVT_BUTTON, self.OnP4, sn)
		dw	= wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + 'cdw.png', wx.BITMAP_TYPE_PNG), pos=(83,0), size=(25, 25), style=wx.NO_BORDER)	
		dw.Bind(wx.EVT_BUTTON, self.Down, dw)
		up	= wx.BitmapButton(self, -1, wx.Bitmap(sys_inf.ICON_PATH + 'cup.png', wx.BITMAP_TYPE_PNG), pos=(108,0), size=(25, 25), style=wx.NO_BORDER)	
		up.Bind(wx.EVT_BUTTON, self.Up, up)
		
		
		self.tcTree.Bind(wx.EVT_TREE_SEL_CHANGED, self.SelChan)
		self.tcTree.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.RightClick)
		self.tcTree.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.tcTree.SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		self.font = wx.Font(conf_db.Dobd_class('fontraztrey').baz_vst(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, conf_db.Dobd_class('fonttrey').baz_vst())
		self.font2 = wx.Font(conf_db.Dobd_class('fontraztreyIt').baz_vst(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, conf_db.Dobd_class('fonttreyIt').baz_vst())
		
		if self.names != _('Not folder'):
			t = self.tcTree.AddRoot(self.names)
			images1 = sys_inf.ICON_PATH + 'sear.png'
			images2 = sys_inf.ICON_PATH + 'folder-open.png'
			images3 = sys_inf.ICON_PATH + 'accez.png'
			images4 = sys_inf.ICON_PATH + 'folder-curr.png'
			images5 = sys_inf.ICON_PATH + 'folder-currG.png'
			images6 = sys_inf.ICON_PATH + 'advanced-directory.png'
			images7 = sys_inf.ICON_PATH + 'ks.png'
			image_list = wx.ImageList(16, 16)
			rotd = image_list.Add(wx.Image(images3, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			fold = image_list.Add(wx.Image(images2, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			fod = image_list.Add(wx.Image(images6, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			fod2 = image_list.Add(wx.Image(images7, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			fild = image_list.Add(wx.Image(images1, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			curr = image_list.Add(wx.Image(images4, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			curg = image_list.Add(wx.Image(images5, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
			self.tcTree.AssignImageList(image_list)
			self.tcTree.SetItemImage(t, rotd, wx.TreeItemIcon_Normal) 
			patch = sys_inf.DATA_PATH + self.pths + '/'
			self.list = []; self.folder = []
			for i in os.listdir(patch):
				self.z = patch + i
				if os.path.isfile(self.z):
					pass
				else:
					self.folder.append(self.z.split('/')[5])
					if self.pths == 'Data':
						if os.path.isdir(self.z): 
							parentItem = self.tcTree.AppendItem(t, self.z.split('/')[5])
							if i == time.strftime('%G:%h'):
								self.tcTree.SetItemImage(parentItem, curr, wx.TreeItemIcon_Normal)
								self.tcTree.SetItemTextColour(parentItem,'#FF9314')
							elif i.split(':')[0] == time.strftime('%G'):
								self.tcTree.SetItemImage(parentItem, curg, wx.TreeItemIcon_Normal)
							else:
								self.tcTree.SetItemImage(parentItem, fold, wx.TreeItemIcon_Normal)
							self.folder.append(parentItem)
							self.tcTree.SetItemFont(parentItem, self.font)
							
							for filtz in os.listdir(self.z):
								newItem = self.tcTree.AppendItem(parentItem, filtz.split('.')[0])	
								self.tcTree.SortChildren(parentItem)
								if i == time.strftime('%G:%h'):
									self.tcTree.SetItemTextColour(newItem,'#FF9314')
								self.tcTree.SetItemImage(newItem, fild, wx.TreeItemIcon_Normal)
								self.list.append(self.z + '/' + filtz)	
								self.tcTree.SetItemFont(newItem, self.font2)
					elif self.pths == 'Other':
						if os.path.isdir(self.z): 
							parentItem = self.tcTree.AppendItem(t, self.z.split('/')[5])
							self.tcTree.SetItemImage(parentItem, fod, wx.TreeItemIcon_Normal)
							self.folder.append(parentItem)
							self.tcTree.SetItemFont(parentItem, self.font)
							for filtz in os.listdir(self.z):
								newItem = self.tcTree.AppendItem(parentItem, filtz.split('.')[0])	
								self.tcTree.SortChildren(parentItem)
								self.tcTree.SetItemImage(newItem, fod2, wx.TreeItemIcon_Normal)
								self.list.append(self.z + '/' + filtz)
								self.tcTree.SetItemFont(newItem, self.font2)
						self.tcTree.ExpandAll()
		else:
			t = self.tcTree.AddRoot(_('Not folder'))
			patch = sys_inf.DATA_PATH + self.pths + '/'
			self.list = []
			for i in os.listdir(patch):
				self.z = patch + i
				if os.path.isfile(self.z):
					pass
				else:
					for filtz in os.listdir(self.z):
						newItem = self.tcTree.AppendItem(t, filtz.split('.')[0])	
						self.list.append(self.z + '/' + filtz)
						self.tcTree.SetItemFont(newItem, self.font2)
						if self.pths == 'Data':
							if self.z.split('/')[5] == time.strftime('%G:%h'):
								self.tcTree.SetItemTextColour(newItem,'#FF9314')
							
		self.tcTree.ExpandAll()
		self.tcTree.SortChildren(self.tcTree.GetSelection())
		
	def SelChan(self, event):		
		item = self.tcTree.GetSelection()
		tc = self.tcTree.GetItemText(item).encode('utf-8').decode('latin-1').encode('latin-1')
		for u in self.list:
				if tc in u.split('/')[6]:
					self.wop.LoadFile(u)
					conf_db.Listrem(u)
					
	def RightClick(self, event):
		self.popupmenu = wx.Menu()
		fil = sys_inf.ICON_PATH + '1.png'
		fil2 = sys_inf.ICON_PATH + 'new.png'
		fil26 = sys_inf.ICON_PATH + 'acce.png'
		fil3 = sys_inf.ICON_PATH + 'cut.png'
		item1 = wx.MenuItem(self.popupmenu, -1, _('New'))
		item1.SetBitmap(wx.Bitmap(fil))
		self.popupmenu.AppendItem(item1)
		item2 = wx.MenuItem(self.popupmenu, -1, _('Edit'))
		item2.SetBitmap(wx.Bitmap(fil2))
		self.popupmenu.AppendItem(item2)
		item26 = wx.MenuItem(self.popupmenu, -1, _('View as text'))
		item26.SetBitmap(wx.Bitmap(fil26))
		self.popupmenu.AppendItem(item26)
		item3 = wx.MenuItem(self.popupmenu, -1, _('Remove'))
		item3.SetBitmap(wx.Bitmap(fil3))
		self.popupmenu.AppendItem(item3)
		self.Bind(wx.EVT_MENU, self.OnP1, item1)
		self.Bind(wx.EVT_MENU, self.OnP2, item2)
		self.Bind(wx.EVT_MENU, self.OnP26, item26)
		self.Bind(wx.EVT_MENU, self.OnRD, item3)
		self.tcTree.PopupMenu(self.popupmenu)
		self.tcTree.Layout()
		
	def OnRD(self, event):
		itemf = self.tcTree.GetSelection()
		tcf = self.tcTree.GetItemText(itemf).encode('utf-8').decode('latin-1').encode('latin-1')
		
		ptd = sys_inf.DATA_PATH + 'Data/'
		pto = sys_inf.DATA_PATH + 'Other/'
		if os.path.isdir(ptd + tcf):
			dial = wx.MessageDialog(None, _('Warning!!! Remove all notes to folder. Delete?'), 'Info', wx.YES_NO | wx.ICON_QUESTION)
			ret = dial.ShowModal()
			if ret == wx.ID_YES:
				for i in os.listdir(ptd + tcf):
					os.remove(ptd + tcf + '/' + i)
				os.rmdir(ptd + tcf)
				self.tcTree.Delete(itemf)
		elif os.path.isdir(pto + tcf):
			dial = wx.MessageDialog(None, _('Warning!!! Remove all notes to folder. Delete?'), 'Info', wx.YES_NO | wx.ICON_QUESTION)
			ret = dial.ShowModal()
			if ret == wx.ID_YES:
				for i in os.listdir(pto + tcf):
					os.remove(pto + tcf + '/' + i)
				os.rmdir(pto + tcf)
				self.tcTree.Delete(itemf)
		else:
			d = self.tcTree.GetItemParent(itemf)
			par = self.tcTree.GetItemText(d).encode('utf-8').decode('latin-1').encode('latin-1')
			for u in self.list:
				delet = tcf + '.ox'
				n = u.split('/')[6]
				if delet == n:
					if os.path.exists(ptd + par + '/' + delet):
						os.remove(ptd + par + '/' + delet)
					elif os.path.exists(pto + par + '/' + delet):
						os.remove(pto + par + '/' + delet)
					self.tcTree.Delete(itemf)
		self.tcTree.Layout()
	
	def OnP1(self, event):
		panel_richtext.Upim_Writer().Show()
		
		
	def OnP26(self, event):
		item = self.tcTree.GetSelection()
		tc = self.tcTree.GetItemText(item).encode('utf-8').decode('latin-1').encode('latin-1')
		tes = conf_db.searcingdb(tc)
		tx.TextViewer(tes).Show()
	
		
	def OnP2(self, event):
		item = self.tcTree.GetSelection()
		tc = self.tcTree.GetItemText(item).encode('utf-8').decode('latin-1').encode('latin-1')
		for u in self.list:
			if tc in u:
				if tc in u.split('/')[6]:
					panel_richtext.Upim_Writer(patch=u).Show()
				
	def OnP4(self, event):
		self.tcTree.ExpandAll()
	
	def Coll(self, event):
		self.tcTree.CollapseAll()
	
	def Recent(self, event):
		im = sys_inf.ICON_PATH + 's1.png'
		self.submenu = wx.Menu()
		for i in conf_db.nedlist:
			a = i.split('/')[6]
			items = wx.MenuItem(self.submenu, -1, a.split('.')[0])
			items.SetBitmap(wx.Bitmap(im))
			self.Bind(wx.EVT_MENU, self.Low, items)
			self.submenu.AppendItem(items)
		self.PopupMenu(self.submenu)
	
	def Low(self, event):
		rec = self.submenu.FindItemById(event.GetId())
		partc = rec.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		for y in conf_db.nedlist:
			if partc + '.ox' == y.split('/')[6]:
				self.wop.LoadFile(y)

	def Down(self, event):
		self.tcTree.ScrollLines(self.tcTree.GetCount()*2)
	def Up(self, event):
		self.tcTree.ScrollLines(-self.tcTree.GetCount()*2)