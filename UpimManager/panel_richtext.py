#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2016 year

@author: FrIg aka Prohodimec 
"""
import wx
import time
import os
import wx.richtext as text
import conf_db
import drag_drop
import sys_inf
from sys import argv
import validate
sys_inf.GetTxt()

"""
практически те же функ., что и в менеджере, поэтому нет иного коментов
"""
class Upim_Writer(wx.Frame):
	def __init__(self, patch=None):
		self.patch = patch# путь к файлу, чтобы запускать из bash: $1, для того и ссылка
		
		self.disp = sys_inf.Sizer()
		
		wx.Frame.__init__(self, None, title="Upim Writer", size=(self.disp[0] - 20, self.disp[1] - 200),  style=wx.DEFAULT_FRAME_STYLE)

		f = sys_inf.ICON_PATH  + 'up.png'
		self.SetIcon(wx.Icon(f, wx.BITMAP_TYPE_PNG))
		
		f11 = sys_inf.ICON_PATH  + '1.png'
		f22 = sys_inf.ICON_PATH  + '2.png'
		f33 = sys_inf.ICON_PATH  + '3.png'
		f44 = sys_inf.ICON_PATH  + '4.png'
		f55 = sys_inf.ICON_PATH  + '5.png'
		f66 = sys_inf.ICON_PATH  + '6.png'
		f77 = sys_inf.ICON_PATH  + '7.png'
		f57 = sys_inf.ICON_PATH  + 'prt.png'
		f88 = sys_inf.ICON_PATH  + '8.png'
		f58 = sys_inf.ICON_PATH + 'in.png'
		
		menuBar = wx.MenuBar()
		menu = wx.Menu()
		itm1 = wx.MenuItem(menu, -1, _('New File'))
		itm1.SetBitmap(wx.Bitmap(f11))
		menu.AppendItem(itm1)
		
		itm2 = wx.MenuItem(menu, -1, _('Open'))
		itm2.SetBitmap(wx.Bitmap(f22))
		menu.AppendItem(itm2)
		menu.AppendSeparator()
		
		itm4 = wx.MenuItem(menu, -1, _('Save'))
		itm4.SetBitmap(wx.Bitmap(f33))
		menu.AppendItem(itm4)
		
		itm5 = wx.MenuItem(menu, -1, _('Save as'))
		itm5.SetBitmap(wx.Bitmap(f44))
		menu.AppendItem(itm5)
		
		itm58 = wx.MenuItem(menu, -1, _('Save as html'))
		itm58.SetBitmap(wx.Bitmap(f58))
		menu.AppendItem(itm58)
		menu.AppendSeparator()
		
		itm57 = wx.MenuItem(menu, -1, _('Print'))
		itm57.SetBitmap(wx.Bitmap(f57))
		menu.AppendItem(itm57)
		menu.AppendSeparator()
		
		itm6 = wx.MenuItem(menu, -1, _('Clear'))
		itm6.SetBitmap(wx.Bitmap(f55))
		menu.AppendItem(itm6)
		menu.AppendSeparator()
		
		itm7 = wx.MenuItem(menu, -1, _('Exit'))
		itm7.SetBitmap(wx.Bitmap(f66))
		menu.AppendItem(itm7)
		
		self.Bind(wx.EVT_MENU, self.Onj1, itm1)
		self.Bind(wx.EVT_MENU, self.Onj2, itm2)
		self.Bind(wx.EVT_MENU, self.Savz, itm5)
		self.Bind(wx.EVT_MENU, self.prints, itm57)
		self.Bind(wx.EVT_MENU, self.OnFileSaveHtml, itm58)
		self.Bind(wx.EVT_MENU, self.Sav, itm4)
		self.Bind(wx.EVT_MENU, self.Clears, itm6)
		self.Bind(wx.EVT_MENU, self.OnCloses, itm7)
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
		
		menuBar.Append(menu, _("File"))
		menu3 = wx.Menu()
		
		ffg = sys_inf.ICON_PATH  + 'format-justify-left1.png'
		ffh = sys_inf.ICON_PATH  + 'format-justify-center1.png'
		fff = sys_inf.ICON_PATH  + 'format-justify-right1.png'
		ffl = sys_inf.ICON_PATH  + '161.png'
		ffk = sys_inf.ICON_PATH  + '41.png'
		ffs = sys_inf.ICON_PATH  + 'a1.png'
		ffn = sys_inf.ICON_PATH  + 's1.png'
		ffj = sys_inf.ICON_PATH  + 'format-text-bold1.png'
		ffna = sys_inf.ICON_PATH  + 'format-text-italic1.png'
		ffpo = sys_inf.ICON_PATH  + 'format-text-underline1.png'
		par = sys_inf.ICON_PATH  + '141.png'
		opar = sys_inf.ICON_PATH  + '151.png'

		menuBar.Append(menu3, _("Edit"))
		itm19 = wx.MenuItem(menu3, -1, _('Bold'))
		itm19.SetBitmap(wx.Bitmap(ffj))
		menu3.AppendItem(itm19)
		
		itm20 = wx.MenuItem(menu3, -1, _('Italic'))
		itm20.SetBitmap(wx.Bitmap(ffna))
		menu3.AppendItem(itm20)
		
		itm21 = wx.MenuItem(menu3, -1, _('Underline'))
		itm21.SetBitmap(wx.Bitmap(ffpo))
		menu3.AppendItem(itm21)
		menu3.AppendSeparator()
		
		itm22 = wx.MenuItem(menu3, -1, _('Indent'))
		itm22.SetBitmap(wx.Bitmap(par))
		menu3.AppendItem(itm22)
		
		itm23 = wx.MenuItem(menu3, -1, _('Unindent'))
		itm23.SetBitmap(wx.Bitmap(opar))
		menu3.AppendItem(itm23)
		menu3.AppendSeparator()
		
		itm12 = wx.MenuItem(menu3, -1, _('Left'))
		itm12.SetBitmap(wx.Bitmap(ffg))
		menu3.AppendItem(itm12)
		
		itm13 = wx.MenuItem(menu3, -1, _('Centre'))
		itm13.SetBitmap(wx.Bitmap(ffh))
		menu3.AppendItem(itm13)
		
		itm14 = wx.MenuItem(menu3, -1, _('Right'))
		itm14.SetBitmap(wx.Bitmap(fff))
		menu3.AppendItem(itm14)
		menu3.AppendSeparator()
		
		itm15 = wx.MenuItem(menu3, -1, _('Write lines'))
		itm15.SetBitmap(wx.Bitmap(ffl))
		menu3.AppendItem(itm15)
		
		itm16 = wx.MenuItem(menu3, -1, _('Write image'))
		itm16.SetBitmap(wx.Bitmap(ffk))
		menu3.AppendItem(itm16)
		
		itm17 = wx.MenuItem(menu3, -1, _('Write link to file'))
		itm17.SetBitmap(wx.Bitmap(ffs))
		menu3.AppendItem(itm17)	
		menu3.AppendSeparator()
		
		itm18 = wx.MenuItem(menu3, -1, _('Remember'))
		itm18.SetBitmap(wx.Bitmap(ffn))
		menu3.AppendItem(itm18)
		
		self.Bind(wx.EVT_MENU, self.To_Left, itm12)
		self.Bind(wx.EVT_MENU, self.To_Center, itm13)
		self.Bind(wx.EVT_MENU, self.To_Right, itm14)
		self.Bind(wx.EVT_MENU, self.Write_Line, itm15)
		self.Bind(wx.EVT_MENU, self.OnImageOpen, itm16)
		self.Bind(wx.EVT_MENU, self.URL2, itm17)
		self.Bind(wx.EVT_MENU, self.PanNap, itm18)
		self.Bind(wx.EVT_MENU, self.Bold, itm19)
		self.Bind(wx.EVT_MENU, self.It, itm20)
		self.Bind(wx.EVT_MENU, self.Underline, itm21)
		self.Bind(wx.EVT_MENU, self.Lines, itm22)
		self.Bind(wx.EVT_MENU, self.NewsLines, itm23)
		
		menu7= wx.Menu()
		menuBar.Append(menu7, _("Notes"))
		
		i0 = sys_inf.ICON_PATH + 'sse.png'
		itns =  wx.MenuItem(menu7, -1, _('Search notes'))
		itns.SetBitmap(wx.Bitmap(i0))
		menu7.AppendItem(itns)
		self.Bind(wx.EVT_MENU, self.OnSear, itns)
		
		i1 = sys_inf.ICON_PATH + 'acce.png'
		itnd =  wx.MenuItem(menu7, -1, _('My diary'))
		itnd.SetBitmap(wx.Bitmap(i1))
		menu7.AppendItem(itnd)
		self.Bind(wx.EVT_MENU, self.OnDiary, itnd)
		
		i2 = sys_inf.ICON_PATH + 'acce2.png'
		itno =  wx.MenuItem(menu7, -1, _('My notes'))
		itno.SetBitmap(wx.Bitmap(i2))
		menu7.AppendItem(itno)
		self.Bind(wx.EVT_MENU, self.OnOther, itno)
		
		menu5 = wx.Menu()
		fns = sys_inf.ICON_PATH  + 'nas1.png'
		menuBar.Append(menu5, _("Settings"))
		itm25 = wx.MenuItem(menu5, -1, _("Settings"))
		itm25.SetBitmap(wx.Bitmap(fns))
		menu5.AppendItem(itm25)
		self.Bind(wx.EVT_MENU, self.Nas, itm25)
		
		menu4 = wx.Menu()
		menuBar.Append(menu4, _("Tutorial"))
		itm8 = wx.MenuItem(menu4, -1, _('Open tutorial'))
		itm8.SetBitmap(wx.Bitmap(f77))
		menu4.AppendItem(itm8)
		self.Bind(wx.EVT_MENU, self.On8, itm8)
		
		itm9 = wx.MenuItem(menu4, -1, _('About'))
		itm9.SetBitmap(wx.Bitmap(f88))
		menu4.AppendItem(itm9)
		self.Bind(wx.EVT_MENU, self.On9, itm9)
		self.SetMenuBar(menuBar)

		tb = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT)
		#
		if conf_db.Dobd_class('toolbar').baz_vst() != 'Not':
			tb.Show()
		else:
			tb.Hide()
		#
		opp = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '11b.png'), _('Write time and date'))
		
		tb.AddSeparator()
		tf = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'bl2.png'), _('Return'))
		
		podws = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'podw.png'), _('GoEnd'))
		
		poups = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'poup.png'), _('GoHome'))
		
		ta = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'bl1.png'), _('Go'))
		tb.AddSeparator()
		
		bomp = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '4b.png'), _('Write image'))
		font = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '5b.png'), _('Choice font'))
		
		col = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '6b.png'), _('Choice colour text'))
		tb.AddSeparator()
		
		save = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '12b.png'), _('Save to calendar'))
		
		savas = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '9b.png'), _('Save real'))
		
		savz = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '8b.png'), _('Save to notes'))
		tb.AddSeparator()
		
		li = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-justify-left.png'), _('Left'))
		
		ct = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-justify-center.png'), _('Centre'))
		
		pr = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-justify-right.png'), _('Right'))

		tb.AddSeparator()
		
		tyd = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '14b.png'), _('Indent'))
		
		sud = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '15b.png'), _('Unindent'))
		tb.AddSeparator()
		
		bol = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'format-text-bold.png'), _('Bold'))
		itl = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'format-text-italic.png'), _('Italic'))
		poc = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-text-underline.png'), _('Underline'))
		tb.AddSeparator()
		
		lin = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '16.png'),_('Write lines') )
		tb.AddSeparator()
		
		clean = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '7b.png'), _('Clear'))
		tb.AddSeparator()
		
		link = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'a.png'), _('Write link to file'))
		
		nap = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 's.png'), _('Remember'))
		
		nopt = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'nas.png'), _('Settings'))
		self.Bind(wx.EVT_TOOL, self.Nas, nopt)
		tb.AddSeparator()
		
		sp = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'p.png'), _('Tutorial(ru)'))
		
		ex = tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'ex.png'), _('Exit'))
		tb.Realize()


		self.Bind(wx.EVT_TOOL, self.Tf, tf)
		self.Bind(wx.EVT_TOOL, self.Ta, ta)
		self.Bind(wx.EVT_TOOL, self.OnFileOpen, opp)
		self.Bind(wx.EVT_TOOL, self.OnImageOpen, bomp)
		self.Bind(wx.EVT_TOOL, self.OnFont, font) 
		self.Bind(wx.EVT_TOOL, self.OnColour, col)
		self.Bind(wx.EVT_TOOL, self.OnFileSaveAs, save)
		self.Bind(wx.EVT_TOOL, self.Sav, savas)
		self.Bind(wx.EVT_TOOL, self.Savz, savz)
		self.Bind(wx.EVT_TOOL, self.To_Left, li)
		self.Bind(wx.EVT_TOOL, self.To_Center, ct)
		self.Bind(wx.EVT_TOOL, self.To_Right, pr)
		self.Bind(wx.EVT_TOOL, self.Lines, tyd)
		self.Bind(wx.EVT_TOOL, self.NewsLines, sud)
		self.Bind(wx.EVT_TOOL, self.Bold, bol)
		self.Bind(wx.EVT_TOOL, self.It, itl)
		self.Bind(wx.EVT_TOOL, self.Underline, poc)
		self.Bind(wx.EVT_TOOL, self.Write_Line, lin)
		self.Bind(wx.EVT_TOOL, self.Clears, clean)
		self.Bind(wx.EVT_TOOL, self.URL2, link)
		self.Bind(wx.EVT_TOOL, self.PanNap, nap)
		self.Bind(wx.EVT_TOOL, self.On8, sp)
		self.Bind(wx.EVT_TOOL, self.OnCloseWindow, ex)
		self.Bind(wx.EVT_TOOL, self.PosDw, podws)
		self.Bind(wx.EVT_TOOL, self.PosUp, poups)
		
		self.win = text.RichTextCtrl(self, pos =wx.DefaultPosition, style = wx.DEFAULT_FRAME_STYLE)
		self.win.SetBackgroundColour(conf_db.Dobd_class('cvetwrit').baz_vst())
		self.win.Bind(wx.EVT_TEXT_URL, self.OnURLS)
		
		wx.CallAfter(self.win.SetFocus)
		
		font2 = wx.Font(conf_db.Dobd_class('fontrazwrit').baz_vst(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, conf_db.Dobd_class('fontwrit').baz_vst())
		self.win.SetFont(font2)
		
		self.AddRTCHandlers()
		self.win.BeginParagraphSpacing(0, 20) #''''
		
		if conf_db.Dobd_class('colorviz').baz_vst() == '#FFFFFF':
			self.win.BeginTextColour((0, 0, 0))
			self.cvet = '#000000'
		else:
			self.win.BeginTextColour((170, 153, 110))
			self.cvet = '#FFFFFF'
			
		if sys_inf.Loc() == 'ru_RU':
			h2 = time.strftime('%H:%M мин. %d %h %G года\n') + int(conf_db.Dobd_class('ul').baz_vst())*'-' + '\n'
		else:
			h2 = time.strftime('%H:%M min %d %h %G year\n') + int(conf_db.Dobd_class('ul').baz_vst())*'-' + '\n'
			
		files = sys_inf.CONF_PATH + 'prz.ini'
		for i in open(files, 'rb').readlines():
			if time.strftime('%d') + ':' + time.strftime('%h') == i.split(';')[0]:
				d2 = i.split(';')[1] + 3*'\t'
				try:
					if i.split(';')[2]:
						im = wx.Image(i.split(';')[2].strip(), wx.BITMAP_TYPE_ANY)   
						self.win.WriteImage(im)
				except IndexError:
					pass
				break
			else:
				d2 = ''
		self.win.WriteText(d2 + h2)	

		#
		dt = drag_drop.FileDrop(self.win)
		self.win.SetDropTarget(dt)
		#
		if self.patch is not None:
			self.win.LoadFile(self.patch)
		#	
		try:
			if argv[1]:
				try:
					if int(argv[1]):
						pass
				except ValueError:
					self.win.LoadFile(argv[1])
		except IndexError:
			pass
		#	
		self.font_rz = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')	
		#
	def PosDw(self, event):
		self.win.ShowPosition(len(self.win.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')))
		
	def PosUp(self, event):
		self.win.ShowPosition(2)
		
	# функции и биндинг лисбоксов заметок и поиска, что нет в diary
	def OnSear(self, event):
		self.pan = wx.Panel(self, -1, size=(self.disp[0] - 20, 160), pos=(0, 0))
		self.pan.SetBackgroundColour(conf_db.Dobd_class('cvetwrit').baz_vst())
		self.pan.SetForegroundColour(self.cvet)
		t1f = wx.StaticText(self.pan, -1, _("Find notes"), (self.disp[0]/2.3, 4))
		t1f.SetFont(self.font_rz)
		self.tex = wx.TextCtrl(self.pan, -1, _("Write text for searching"), pos=(22, 30), size=(250, 25))
		buttons = wx.Button(self.pan, label=_("Search"), size=(64, 25), pos=(275, 30))
		buttons.Bind(wx.EVT_BUTTON, self.Nahod, buttons)
		cuts = wx.BitmapButton(self.pan, -1, wx.Bitmap(sys_inf.ICON_PATH  + 'cutp.png', wx.BITMAP_TYPE_PNG), pos=(self.disp[0] - 42, 10), size=(20, 20), style=wx.NO_BORDER)
		cuts.Bind(wx.EVT_BUTTON, self.ClosePan, cuts)
		
	def Nahod(self, event):
		self.LIS = []
		if self.tex.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') != _("Write text for searching"):
			if self.tex.GetValue() != '':
				text_search = self.tex.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') 
				conf_db.Ds(text_search, self.LIS)
		self.listBoxN = wx.ListBox(self.pan, -1, (0, 60), (self.disp[0] - 20, 100), self.LIS, wx.LB_SORT)
		self.listBoxN.SetBackgroundColour(conf_db.Dobd_class('cvetwrit').baz_vst())
		self.listBoxN.SetForegroundColour(self.cvet)
		self.listBoxN.Bind(wx.EVT_LISTBOX_DCLICK, self.SelectN)
		
	def SelectN(self, event):
		del conf_db.dlist[:]
		conf_db.Lists(self.win.GetFilename())	
		ztxN = self.listBoxN.GetStringSelection().encode('utf-8').decode('latin-1').encode('latin-1')
		pat = [sys_inf.DATA_PATH + 'Data', sys_inf.DATA_PATH + 'Other']
		for patch in pat: 
			for i in os.listdir(patch):
				zt = patch + '/' + i
				if os.path.isfile(zt):
					pass
				else:
					for files in os.listdir(zt):
						if files == ztxN + '.ox':
							if os.path.exists(zt + '/' + files):
								self.win.LoadFile(zt + '/' + files)
								conf_db.Lists(self.win.GetFilename())
							
	def OnDiary(self, event):
		self.LIST2 = []
		fo = sys_inf.DATA_PATH + 'Data/'
		for ppo in os.listdir(fo):
			ffo = fo + ppo
			if os.path.isdir(ffo):
				for fap in os.listdir(ffo):
					self.LIST2.append(fap)
		self.CloseList()
		self.pan1 = wx.Panel(self, -1, size=(self.disp[0] - 20, 160), pos=(0, 0))
		cut2 = wx.BitmapButton(self.pan1, -1, wx.Bitmap(sys_inf.ICON_PATH  + 'cutp.png', wx.BITMAP_TYPE_PNG), pos=(self.disp[0] - 42, 10), size=(20, 20), style=wx.NO_BORDER)
		cut2.Bind(wx.EVT_BUTTON, self.ClosePan, cut2)
		t1 = wx.StaticText(self.pan1, -1, _("My diary"), (self.disp[0]/2.3, 4))
		t1.SetFont(self.font_rz)
		self.listBoxQ = wx.ListBox(self.pan1, -1, (0, 40), (self.disp[0] - 20, 120), self.LIST2, wx.LB_SORT)
		self.listBoxQ.Bind(wx.EVT_LISTBOX_DCLICK, self.SelectQ)
		self.listBoxQ.SetBackgroundColour(conf_db.Dobd_class('cvetwrit').baz_vst())
		self.listBoxQ.SetForegroundColour(self.cvet)
	
	def SelectQ(self, event):
		del conf_db.dlist[:]
		conf_db.Lists(self.win.GetFilename())	
		ztxs = self.listBoxQ.GetStringSelection().encode('utf-8').decode('latin-1').encode('latin-1')
		fmd = sys_inf.DATA_PATH + 'Data/'
		for ftd in os.listdir(fmd):
			patcd = fmd + ftd
			if os.path.isdir(patcd):
				for ftas in os.listdir(patcd):
					if ftas == ztxs:
						self.win.LoadFile(patcd + '/' + ftas)
						conf_db.Lists(self.win.GetFilename())
						
	def OnOther(self, event):
		self.LIST = []
		foo = sys_inf.DATA_PATH + 'Other/'
		for papo in os.listdir(foo):
			fifo = foo + papo
			if os.path.isdir(fifo):
				for fapo in os.listdir(fifo):
					self.LIST.append(fapo)
		self.CloseList()
		self.pan2 = wx.Panel(self, -1, size=(self.disp[0] - 20, 160), pos=(0, 0))
		t2 = wx.StaticText(self.pan2, -1, _("My notes"), (self.disp[0]/2.3, 4))
		t2.SetFont(self.font_rz)
		cut1 = wx.BitmapButton(self.pan2, -1, wx.Bitmap(sys_inf.ICON_PATH  + 'cutp.png', wx.BITMAP_TYPE_PNG), pos=(self.disp[0] - 42, 10), size=(20, 20), style=wx.NO_BORDER)
		cut1.Bind(wx.EVT_BUTTON, self.ClosePan, cut1)
		self.listBoxW = wx.ListBox(self.pan2, -1, (0, 40), (self.disp[0] - 20, 120), self.LIST, wx.LB_SORT)
		
		self.listBoxW.Bind(wx.EVT_LISTBOX_DCLICK, self.SelectW)
		self.listBoxW.SetBackgroundColour(conf_db.Dobd_class('cvetwrit').baz_vst())
		self.listBoxW.SetForegroundColour(self.cvet)	
		
	def SelectW(self, event):
		del conf_db.dlist[:]
		conf_db.Lists(self.win.GetFilename())
		ztxo = self.listBoxW.GetStringSelection().encode('utf-8').decode('latin-1').encode('latin-1')
		fmo = sys_inf.DATA_PATH + 'Other/'
		for fto in os.listdir(fmo):
			patco = fmo + fto
			if os.path.isdir(patco):
				for ftos in os.listdir(patco):
					if ftos == ztxo:
						self.win.LoadFile(patco + '/' + ftos)
						conf_db.Lists(self.win.GetFilename())


	def ClosePan(self, event):
		self.CloseList()
			
	def CloseList(self):
		try:
			if self.pan:
				self.pan.Destroy()
		except:
			pass
		try:
			if self.pan1:
				self.pan1.Destroy()
		except:
			pass
		try:
			if self.pan2:
				self.pan2.Destroy()	
		except:
			pass
			
	# мелочи		
	def Onj1(self, event):
		os.system('python ' + sys_inf.UPIM_PATH + 'panel_richtext.py &')	
		
	def Nas(self, event):
		os.system('python ' + sys_inf.UPIM_PATH + 'configuration.py &')	
	
	def Onj2(self, event):
		wildcard= "Page ox (*.ox)|*.ox|"
		dlg = wx.FileDialog(self, _("Choice file"), sys_inf.DATA_PATH, wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath().encode('utf-8').decode('latin-1').encode('latin-1')
			if path:
				self.win.LoadFile(path)
		dlg.Destroy()
	#
	def On8(self, event):
		if sys_inf.Loc() == 'ru_RU':
			self.win.LoadFile('/usr/local/share/upim/ManualRU.ox')
		else:
			self.win.Clear()
			self.win.WriteText('Not tutorial to ' + sys_inf.Loc().split('_')[1] + ' language! :-(')
	#
	def On9(self, event):	
		description = """Upim Writer is an advanced powerful richtext editor, viewer for Linux.
"""
		lic = '/usr/local/share/upim/LICENSE'
		licence = open(lic, 'r').read()
		info = wx.AboutDialogInfo()
		info.SetName('Upim Writer')
		info.SetVersion('1.0.4')
		info.SetDescription(description)
		info.SetCopyright('(C) 2013 - 2017 Victor Frig')
		info.SetLicence(licence)
		info.AddDeveloper('Victor Frig aka Prohodimec')
		wx.AboutBox(info)
	#	
	def URL2(self, event):
		self.pnn = wx.Panel(self, -1, size=(280, 100), pos=(500, 400))
		self.aText = wx.TextCtrl(self.pnn, -1, _("Write name link"), size=(270, 30), pos=(5, 2))
		button_vub = wx.Button(self.pnn, -1, _("Choice file"), size=(270,30), pos=(5, 34))
		button_vub.Bind(wx.EVT_BUTTON, self.FILE_apS, button_vub)
		button_write = wx.Button(self.pnn, -1, _("Save"), size=(130,30), pos=(5, 66))
		button_write.Bind(wx.EVT_BUTTON, self.URL_apS, button_write)
		button_e = wx.Button(self.pnn, -1, _("Cancel"), size=(130,30), pos=(145, 66))
		button_e.Bind(wx.EVT_BUTTON, self.ExS, button_e)
	#
	def URL_apS(self, event):
		if self.aText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') != _("Write name link"):
			if self.aText.GetValue() != '':
				name_text = self.aText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')
		if self.path != '':
			name_url = self.path.encode('utf-8').decode('latin-1').encode('latin-1')
		urlStyle = text.TextAttrEx()
		urlStyle.SetTextColour(wx.RED)
		urlStyle.SetFontUnderlined(True)
		self.win.BeginStyle(urlStyle)
		self.win.BeginURL(name_url)
		self.win.WriteText(name_text)
		self.win.EndURL()
		self.win.Newline()
		self.win.EndStyle()
		self.pnn.Destroy()
		self.win.WriteText('      ')
	#	
	def FILE_apS(self, event):		
		dlg = wx.FileDialog(self, _("Choice file"), style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.path = dlg.GetPath()
			if self.path:
				self.URL_apS()
		dlg.Destroy()
		self.pnn.Destroy()
	#
	def PanNap(self, event):
		os.system('python '+ sys_inf.UPIM_PATH + 'soxr_nap.py &')	
		
	# туда-сюда 1 позишен
	def Tf(self, event):
		i = 1
		f = len(conf_db.dlist)
		for a in range(f):
			self.topnit = f-i
			self.win.LoadFile(conf_db.dlist[f-i])
			i += 1
	
	def Ta(self, event):
		i = 1
		f = len(conf_db.dlist)
		for a in range(f):
			self.win.LoadFile(conf_db.dlist[self.topnit+i])
			i += 1

	def ExS(self, event):
		self.pnn.Destroy()
	#	
	def OnURLS(self, event):
		try:
			if event.GetString().encode('utf-8').decode('latin-1').encode('latin-1').split('/')[6].split('.')[1] == 'ox':
				del conf_db.dlist[:]
				conf_db.Lists(self.win.GetFilename())
				self.win.LoadFile(event.GetString().encode('utf-8').decode('latin-1').encode('latin-1'))
				conf_db.Lists(self.win.GetFilename())
			else:
				os.system('xdg-open ' + '"' + event.GetString().encode('utf-8').decode('latin-1').encode('latin-1') + '"' + ' &')
		except IndexError:
			os.system('xdg-open ' + '"' + event.GetString().encode('utf-8').decode('latin-1').encode('latin-1') + '"' + ' &')
	#
	def To_Left(self, event):
		self.win.ApplyAlignmentToSelection(text.TEXT_ALIGNMENT_LEFT) 
		
	def To_Center(self, event):
		self.win.ApplyAlignmentToSelection(text.TEXT_ALIGNMENT_CENTRE)
		
	def To_Right(self, event):
		self.win.ApplyAlignmentToSelection(text.TEXT_ALIGNMENT_RIGHT)
	#	
	def Write_Line(self, event):
		self.win.WriteText(int(conf_db.Dobd_class('ul').baz_vst())*'-' + '\n')
	#
	def Clears(self, event):
		self.win.Clear()
	#
	def OnFileOpen(self, evt):
		if sys_inf.Loc() == 'ru_RU':
			self.win.WriteText(time.strftime('%d %h %G года  %H:%M мин'))
		else:
			self.win.WriteText(time.strftime('%d %h %G years  %H:%M min'))
	#		
	def OnFileSaveAs(self, evt):
		import soxr
		soxr.Soxr(self, None, self.win)
	#
	def OnCloses(self, event):
		self.Destroy()
	#
	def OnFont(self, evt):
		if not self.win.HasSelection():
			return
		r = self.win.GetSelectionRange()
		fontData = wx.FontData()
		fontData.EnableEffects(False)
		attr = text.TextAttrEx()
		attr.SetFlags(text.TEXT_ATTR_FONT)
		if self.win.GetStyle(self.win.GetInsertionPoint(), attr):
			fontData.SetInitialFont(attr.GetFont())
		dlg = wx.FontDialog(self, fontData)
		if dlg.ShowModal() == wx.ID_OK:
			fontData = dlg.GetFontData()
			font = fontData.GetChosenFont()
			if font:
				attr.SetFlags(text.TEXT_ATTR_FONT)
				attr.SetFont(font)
				self.win.SetStyle(r, attr)
		dlg.Destroy()
	#
	def OnColour(self, evt):
		colourData = wx.ColourData()
		attr = text.TextAttrEx()
		attr.SetFlags(text.TEXT_ATTR_TEXT_COLOUR)
		if self.win.GetStyle(self.win.GetInsertionPoint(), attr):
			colourData.SetColour(attr.GetTextColour())
		dlg = wx.ColourDialog(self, colourData)
		if dlg.ShowModal() == wx.ID_OK:
			colourData = dlg.GetColourData()
			colour = colourData.GetColour()
			if colour:
				if not self.win.HasSelection():
					self.win.BeginTextColour(colour)
				else:
					r = self.win.GetSelectionRange()
					attr.SetFlags(text.TEXT_ATTR_TEXT_COLOUR)
					attr.SetTextColour(colour)
					self.win.SetStyle(r, attr)
		dlg.Destroy()
	#	
	def prints(self, event):
		if self.win.GetFilename() != '':
			self.printer = text.RichTextPrinting()
			self.printer.GetPrintData()
			self.printer.PrintFile(self.win.GetFilename())
	#
	def AddRTCHandlers(self):
		if text.RichTextBuffer.FindHandlerByType(text.RICHTEXT_TYPE_HTML) is not None:
			return
		text.RichTextBuffer.AddHandler(text.RichTextXMLHandler(name="Other XML",
                                                           ext="ox",
                                                           type=99))
		text.RichTextBuffer.AddHandler(text.RichTextHTMLHandler())
		wx.FileSystem.AddHandler(wx.MemoryFSHandler())	
	#
	def OnImageOpen(self, event):
		import imag
		imag.TestFrame(self.win).Show()
	#
	def Sav(self, event):
		if self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1') != '':
			if self.win.IsModified():
				lg = wx.MessageDialog(None, _("Warning!!! Edit real file. Save file?"), 'Info',wx.YES_NO | wx.ICON_QUESTION)
				retCode = lg.ShowModal()
				if (retCode == wx.ID_YES):
					fils = self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1')
					self.win.SaveFile(fils)
					self.Osh(fils)	
	#					
	def Bold(self, event):
		self.win.ApplyBoldToSelection()

	def It(self, event):
		self.win.ApplyItalicToSelection()
	
	def Underline(self, event):
		self.win.ApplyUnderlineToSelection()
	#
	def Lines(self, event):
		attr = text.TextAttrEx()
		attr.SetFlags(text.TEXT_ATTR_LEFT_INDENT)
		ip = self.win.GetInsertionPoint()
		if self.win.GetStyle(ip, attr):
			r = text.RichTextRange(ip, ip)
			if self.win.HasSelection():
				r = self.win.GetSelectionRange()
			attr.SetLeftIndent(attr.GetLeftIndent() + 100)
			attr.SetFlags(text.TEXT_ATTR_LEFT_INDENT)
			self.win.SetStyle(r, attr)
	#
	def OnCloseWindow(self, event):
		if self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1') != '':
			if self.win.IsModified():		
				files = self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1')
				dial = wx.MessageDialog(None, _(' Do you want save changes?\n Editable file ') + files, 'Info', wx.YES_NO | wx.ICON_QUESTION)
				ret = dial.ShowModal()
				if ret == wx.ID_YES:
					self.Destroy()
			else:
				self.Destroy()
		else:
			self.Destroy()					
	#	
	def NewsLines(self, event):
		attr = text.TextAttrEx()
		attr.SetFlags(text.TEXT_ATTR_LEFT_INDENT)
		ip = self.win.GetInsertionPoint()
		if self.win.GetStyle(ip, attr):
			r = text.RichTextRange(ip, ip)
			if self.win.HasSelection():
				r = self.win.GetSelectionRange()
		if attr.GetLeftIndent() >= 100:
			attr.SetLeftIndent(attr.GetLeftIndent() - 100)
			attr.SetFlags(text.TEXT_ATTR_LEFT_INDENT)
			self.win.SetStyle(r, attr)
	#
	def Savz(self, event):# Помнишь меня!?! - Nain!
		tch = sys_inf.DATA_PATH + 'Other/'
		wildcard= "Page ox (*.ox)|*.ox|"
		dlg = wx.FileDialog(self, _("Choice file"), tch, wildcard=wildcard, style=wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			if path:
				savep = path + '.ox'
				try:
					if len(savep.split('/')[6].split('.')[0]) == 1:
						dlgs1 = wx.MessageDialog(None, 'Error name: one symbol not valid name!\n No save notes!')
						dlgs1.ShowModal()
					elif savep.split('/')[6].split('.')[0].find('_') != -1:
						dlgs2 = wx.MessageDialog(None, 'Error name: \"_\" not valid symbol\n No save notes!')
						dlgs2.ShowModal()
					else:	
						self.win.SaveFile(savep)
						self.Osh(savep.encode('utf-8').decode('latin-1').encode('latin-1'))							
				except IndexError:
					self.win.SaveFile(savep)
				
		dlg.Destroy()
	#	
	def OnFileSaveHtml(self, event):
		tch = sys_inf.HOME_PATH
		wildcard= "Page html (*.html)|*.html|"
		dlg = wx.FileDialog(self, _("Create file"), tch, wildcard=wildcard, style=wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			if path:
				savep = path + '.html'
				self.win.SaveFile(savep)
		dlg.Destroy()	
	#	
	def Osh(self, path):
		pt = path.split('/')[6]
		once = self.win.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')
		conf_db.dobdb(pt, once)
		
if __name__ == '__main__':		
	app = wx.App()
	Upim_Writer().Show()
	app.MainLoop()