#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:42:29 2016

@author: prohodimec
"""
import wx
import time
import sys_inf
import conf_db
from os import listdir
from os import remove
import tx
import wx.lib.buttons as buttons
sys_inf.GetTxt()

class Seg_Day(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.dis = sys_inf.Sizer()
		self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
		

# шаблоны и статик-тексты
		self.srt = open(sys_inf.DATA_PATH + 'Pattern/shab', 'rb').read()
		self.poth = sys_inf.DATA_PATH + 'Pattern/' + 'stock'
		self.wline = str(int(conf_db.Dobd_class('dl').baz_vst())*'+')
		
# определяется язык для вставки заголовка	
		if sys_inf.Loc() == 'ru_RU':
			self.nam = time.strftime('%A') + ':' + sys_inf.Once() + ':' + time.strftime('%h.') + time.strftime('%G') + "года"
			self.namc = time.strftime('%A, ') + sys_inf.Once() + time.strftime(' %h.') + time.strftime(' %G') + " года\n"
		else:
			self.nam = time.strftime('%A') + ':' + sys_inf.Once() + ':' + time.strftime('%h') + time.strftime('%G') + " year"
			self.namc = time.strftime('%A, ') + sys_inf.Once() + time.strftime(' %h.') + time.strftime(' %G') + " year\n"

# сегодня - в базе		
		try:
			if conf_db.sdb('20:70'):
				pass
		except KeyError:
			conf_db.dbdb('20:70', self.nam)
	
		self.Txts('2.28', '18', 'a', None)		

# кнопочки!..
		self.st = buttons.GenButton(self, -1, label=_("Save as"), size=(self.dis[0]/16, 18), pos=(25,0))
		self.st.SetBackgroundColour('#3B3B3B')
		self.st.SetForegroundColour('lightgray')
		self.st.Bind(wx.EVT_BUTTON, self.OnSaveAs, self.st)
		
		self.stn = buttons.GenButton(self, -1, label=_("Save to"), size=(self.dis[0]/16, 18), pos=(26+self.dis[0]/16,0))
		self.stn.SetBackgroundColour('#3B3B3B')
		self.stn.SetForegroundColour('lightgray')
		self.stn.Bind(wx.EVT_BUTTON, self.OnSaveNa, self.stn)
		
		self.ct = buttons.GenButton(self, -1, label=_("Ret. day"), size=(self.dis[0]/16, 18), pos=(26+self.dis[0]/16*3,0))
		self.ct.SetBackgroundColour('#3B3B3B')
		self.ct.SetForegroundColour('lightgray')
		self.ct.Bind(wx.EVT_BUTTON, self.Clea, self.ct)
		
		self.cl  = buttons.GenButton(self, -1, label=_("Cl. day"), size=(self.dis[0]/16, 18), pos=(26+self.dis[0]/16*2,0))
		self.cl.SetBackgroundColour('#3B3B3B')
		self.cl.SetForegroundColour('lightgray')
		self.cl.Bind(wx.EVT_BUTTON, self.Cl, self.cl)

		self.LtBox()
		
#	листбокс и его бинды
	def LtBox(self):	
		ls = []
		for i in listdir(sys_inf.DATA_PATH + 'Text/'):
			ls.append(i.split('.')[0])
		self.listBox = wx.ListBox(self, -1, (26, 18), (self.dis[0]/7.2, self.dis[1]/2.28), ls, 
                wx.LB_SINGLE)
		self.listBox.Bind(wx.EVT_LISTBOX, self.Select)
		self.listBox.Bind(wx.EVT_LISTBOX_DCLICK,self.OnFileOpen)
		self.listBox.SetBackgroundColour(conf_db.Dobd_class('colorviz').baz_vst())
		self.listBox.SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		
	def Select(self, event):
		ztx = self.listBox.GetStringSelection()
		if ztx != '':
			path_txt = sys_inf.DATA_PATH + 'Text/' + ztx + '.txt'
			tz = open(path_txt, 'rb').read()	
			self.Txts('2.28', '18', 'b', tz)
			
#два клика по итемке и бинды меню	
	def OnFileOpen(self, event):
		self.menu = wx.Menu()
		pth = sys_inf.DATA_PATH + 'Text/' 
		fs = sys_inf.ICON_PATH + 'acce.png'
		vmenu1 = wx.Menu()
		for s in listdir(pth):
			it = wx.MenuItem(vmenu1, -1, str(s).split('.')[0])	
			it.SetBitmap(wx.Bitmap(fs))
			vmenu1.AppendItem(it)
			vmenu1.Bind(wx.EVT_MENU, self.TxOpen, it)
		self.menu.AppendMenu(-1, _("Open as text"), vmenu1)
		self.menu.AppendSeparator()		
		vmenu2 = wx.Menu()
		fd = sys_inf.ICON_PATH + 'cut.png'
		for y in listdir(pth):
			ity = wx.MenuItem(vmenu2, -1, str(y).split('.')[0])	
			ity.SetBitmap(wx.Bitmap(fd))
			vmenu2.AppendItem(ity)
			vmenu2.Bind(wx.EVT_MENU, self.DelTx, ity)
		self.menu.AppendMenu(-1, _("Remove notes day"), vmenu2)
		self.PopupMenu(self.menu)	
	
	def TxOpen(self, event):
		itx = self.menu.FindItemById(event.GetId())
		tcitx = itx.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		text_files = open(sys_inf.DATA_PATH + 'Text/' + tcitx + '.txt', 'rb').read()
		tx.TextViewer(text_files).Show()
	
	def DelTx(self, event):
		itdel = self.menu.FindItemById(event.GetId())
		tcitdel = itdel.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		remove(sys_inf.DATA_PATH + 'Text/' + tcitdel + '.txt')		
		
			
	def OnSaveAs(self, event):
		wildcard= "Page txt (*.txt)|*.txt|"
		d = wx.FileDialog(self, _("Save file"), sys_inf.HOME_PATH, wildcard=wildcard, style=wx.SAVE)
		if d.ShowModal() == wx.ID_OK:
			path = d.GetPath()
			if path:
				self.Text1.SaveFile(path + '.txt')		
		d.Destroy()
		
# соранение на число и его бинды	
	def OnSaveNa(self, event):
		self.pan = wx.Panel(self, -1, size=(330, 72), pos=(190, 220))
		self.chc = wx.SpinCtrl(self.pan, value='1', size=(60, 30), pos=(5, 5), min=1, max=31)
		montd = [_('jan'), _('feb'), _('mar'), _('apr'), _('may'), _('jun'), _('jul'), _('aug'), _('sep'), _('oct'), _('nov'), _('dec')]
		self.chm = wx.ComboBox(self.pan, -1, value=time.strftime('%h'), choices=montd, size=(80, 30), pos=(75, 5), style=wx.CB_DROPDOWN)
		self.chg = wx.SpinCtrl(self.pan, value=time.strftime('%G'), size=(60, 30), pos=(160, 5), min=1970, max=2100)
		self.name = wx.TextCtrl(self.pan, -1,size=(100, 30), pos=(225, 5), style=wx.TE_MULTILINE)
		self.name.WriteText(_('name>'))
		soxb = wx.Button(self.pan, label=_("Save"), pos=(5, 40))
		soxb.Bind(wx.EVT_BUTTON, self.Savc, soxb)
		otm = wx.Button(self.pan, label=_("Cancel"), pos=(230, 40))
		otm.Bind(wx.EVT_BUTTON, self.Exp, otm)
		
	def Exp(self, event):
		self.pan.Destroy()
		

	def Savc(self, event):
		if sys_inf.Loc() == 'ru_RU':
			g = ' года\n'
		else:
			g = ' year\n'
			
		strepl = str(self.chc.GetValue()) + ' ' + self.chm.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') + ' ' + str(self.chg.GetValue()) + g
		
		txts = str(self.chc.GetValue()) + ':' + self.chm.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') + ':' + str(self.chg.GetValue()) + ':' + self.name.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') + '.txt'
		
		path = sys_inf.DATA_PATH + 'Text/'

		self.Text1.Replace(0, 200, strepl)
		self.Text1.SaveFile(path + txts)
		self.pan.Destroy()

#чистим моск, йощь твою...
	def Cl(self, event):
		self.Text1.Clear()		
		self.Text1.WriteText(self.wline + '\n' + '                          ' + self.namc + self.wline + self.srt)
		self.Text1.ShowPosition(70)
		
	def Clea(self, event):
		self.Txts('2.28', '18', 'a', None)
		
#текстовое расписание,надоели гриды - проще стало быть
	def Txts(self, num, position, mark, txtx=None):
		try:
			if self.Text1:
				self.Text1.Hide()
		except AttributeError:
			pass
			
		font3 = wx.Font(int(conf_db.Dobd_class('fontrazdays').baz_vst()), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, conf_db.Dobd_class('fontdays').baz_vst())
		self.Text1 = wx.TextCtrl(self, -1,size=(self.dis[9], self.dis[1]/float(num)), pos=(25 + self.dis[0]/7, int(position)), style=wx.TE_MULTILINE)
		self.Text1.SetFont(font3)
		if mark == 'a':
			self.Text1.SetBackgroundColour(conf_db.Dobd_class('colorviz').baz_vst())
			self.marker = 'a'
		elif mark == 'b':
			self.Text1.SetBackgroundColour('#81565B')
			self.marker = 'b'
		self.Text1.SetForegroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		if txtx == None:
			if conf_db.sdb('20:70') == self.nam:
				t = open(self.poth, 'rb').read()
				self.Text1.Clear()
				self.Text1.AppendText(t)
			else:
				self.Text1.Clear()

				self.Text1.WriteText(self.wline + '\n' + '                          ' + self.namc + self.wline + self.srt)	
		else:
			self.Text1.Clear()
			self.Text1.AppendText(txtx)
		self.Text1.ShowPosition(70)	
		
#стоит только двинуть мышкой...	
	def OnMouseEvent(self, event):
		if event.GetPosition()[1] != '':
			conf_db.dbdb('20:70', self.nam)
			if self.marker == 'a':
				self.Text1.SaveFile(self.poth)
