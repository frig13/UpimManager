#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2016 year

@author: FrIg aka Prohodimec 
"""
import wx
import wx.richtext as text
import time
import os
import Caldar
import panel_richtext
import conf_db
import uni_pan
import sys_inf
import searching
import soxr_diary
import Sheet
import drag_drop
import day
import validate
sys_inf.GetTxt()

class Upim_Manager(wx.Frame):
	def __init__(self, parent, id=-1, title='Upim Manager', pos=wx.DefaultPosition, style=wx.DEFAULT_FRAME_STYLE):
		wx.Frame.__init__(self, parent, id, title, pos)
		
		if conf_db.Dobd_class('splash').baz_vst() != 'Not':# сплашскрин
			fl = sys_inf.ICON_PATH + 'logos.png'
			bmp = wx.Image(fl).ConvertToBitmap()
			wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
			1000, None, -1)

		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)# не даём выйти без сохранения

		self.dis = sys_inf.Sizer()# сайзер, по нелепости править sys_inf
	
		self.SetIcon(wx.Icon(sys_inf.ICON_PATH + 'upim.png', wx.BITMAP_TYPE_PNG))	
#меню и тулбар
		menuBar = wx.MenuBar()#менюбар
		
		f1 = sys_inf.ICON_PATH + '1.png'
		f2 = sys_inf.ICON_PATH + '2.png'
		f3 = sys_inf.ICON_PATH + '3.png'
		f4 = sys_inf.ICON_PATH + '4.png'
		f5 = sys_inf.ICON_PATH + '5.png'
		f6 = sys_inf.ICON_PATH + '6.png'
		f7 = sys_inf.ICON_PATH + '7.png'
		f8 = sys_inf.ICON_PATH + '8.png'
		f88 = sys_inf.ICON_PATH + 'in.png'
		f34 = sys_inf.ICON_PATH + 'obn2.png'
		f38 = sys_inf.ICON_PATH + 'prt.png'
		
		menu = wx.Menu()
		itm1 = wx.MenuItem(menu, -1, _('New File'))
		itm1.SetBitmap(wx.Bitmap(f1))
		menu.AppendItem(itm1)
		
		itm2 = wx.MenuItem(menu, -1, _('Open'))
		itm2.SetBitmap(wx.Bitmap(f2))
		menu.AppendItem(itm2)
		menu.AppendSeparator()
		
		itm4 = wx.MenuItem(menu, -1, _('Save'))
		itm4.SetBitmap(wx.Bitmap(f3))
		menu.AppendItem(itm4)
		
		itm5 = wx.MenuItem(menu, -1, _('Save as'))
		itm5.SetBitmap(wx.Bitmap(f4))
		menu.AppendItem(itm5)
		
		itm88 = wx.MenuItem(menu, -1, _('Save as html'))
		itm88.SetBitmap(wx.Bitmap(f88))
		menu.AppendItem(itm88)
		menu.AppendSeparator()
		
		itm38 = wx.MenuItem(menu, -1, _('Print'))
		itm38.SetBitmap(wx.Bitmap(f38))
		menu.AppendItem(itm38)
		menu.AppendSeparator()
		
		itm34 = wx.MenuItem(menu, -1, _('Return'))
		itm34.SetBitmap(wx.Bitmap(f34))
		menu.AppendItem(itm34)
		menu.AppendSeparator()
		
		itm6 = wx.MenuItem(menu, -1, _('Clear'))
		itm6.SetBitmap(wx.Bitmap(f5))
		menu.AppendItem(itm6)

		menu.AppendSeparator()
		
		itm7 = wx.MenuItem(menu, -1, _('Exit'))
		itm7.SetBitmap(wx.Bitmap(f6))
		menu.AppendItem(itm7)
		
		self.Bind(wx.EVT_MENU, self.On1, itm1)
		self.Bind(wx.EVT_MENU, self.On3, itm2)
		self.Bind(wx.EVT_MENU, self.Print, itm38)
		self.Bind(wx.EVT_MENU, self.OnFileSaveAs, itm5)
		self.Bind(wx.EVT_MENU, self.OnFileSaveHTML, itm88)
		self.Bind(wx.EVT_MENU, self.FileSave, itm4)
		self.Bind(wx.EVT_MENU, self.Clears, itm6)
		self.Bind(wx.EVT_MENU, self.OnClose, itm7)
		self.Bind(wx.EVT_MENU, self.Seg, itm34)
		
		menuBar.Append(menu, _("File"))

		menu3 = wx.Menu()
		
		f77 = sys_inf.ICON_PATH + '11bs.png'
		ffg = sys_inf.ICON_PATH + 'format-justify-left1.png'
		ffh = sys_inf.ICON_PATH + 'format-justify-center1.png'
		fff = sys_inf.ICON_PATH + 'format-justify-right1.png'
		ffl = sys_inf.ICON_PATH + '161.png'
		ffk = sys_inf.ICON_PATH + '41.png'
		ffs = sys_inf.ICON_PATH + 'a1.png'
		ffj = sys_inf.ICON_PATH + 'format-text-bold1.png'
		ffna = sys_inf.ICON_PATH + 'format-text-italic1.png'
		ffpo = sys_inf.ICON_PATH + 'format-text-underline1.png'
		par = sys_inf.ICON_PATH + '141.png'
		opar = sys_inf.ICON_PATH + '151.png'
		
		menuBar.Append(menu3, _("Edit"))
		itm191 = wx.MenuItem(menu3, -1, _('Write time and date'))
		itm191.SetBitmap(wx.Bitmap(f77))
		menu3.AppendItem(itm191)
		menu3.AppendSeparator()
		
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
	
		self.Bind(wx.EVT_MENU, self.To_Left, itm12)
		self.Bind(wx.EVT_MENU, self.To_Center, itm13)
		self.Bind(wx.EVT_MENU, self.To_Right, itm14)
		self.Bind(wx.EVT_MENU, self.Write_Line, itm15)
		self.Bind(wx.EVT_MENU, self.OnImageOpen, itm16)
		self.Bind(wx.EVT_MENU, self.URL_L, itm17)
		self.Bind(wx.EVT_MENU, self.Bold, itm19)
		self.Bind(wx.EVT_MENU, self.It, itm20)
		self.Bind(wx.EVT_MENU, self.Poc, itm21)
		self.Bind(wx.EVT_MENU, self.Lines, itm22)
		self.Bind(wx.EVT_MENU, self.NewsLines, itm23)
		self.Bind(wx.EVT_MENU, self.Dt, itm191)
		
		menu4 = wx.Menu()
		#показывать или нет имя записей на календаре
		self.itm = menu4.AppendCheckItem(-1, _("On/Off notes calendar"))
		if conf_db.Dobd_class('caloff').baz_vst() == 'On':
			self.itm.Check(True)
		else:
			self.itm.Check(False)
		self.Bind(wx.EVT_TOOL, self.Ckb, self.itm)
		menu4.AppendSeparator()
		
		menuBar.Append(menu4, _("Settings"))
		ito = wx.MenuItem(menu4, -1, _('Open diarus.ini for edit'))
		kit = sys_inf.ICON_PATH + 'ac.png'	
		ito.SetBitmap(wx.Bitmap(kit))
		menu4.AppendItem(ito)
		self.Bind(wx.EVT_MENU, self.OnRed, ito)
		
		itd = wx.MenuItem(menu4, -1, _('Open pattern day for edit'))
		itd.SetBitmap(wx.Bitmap(kit))
		menu4.AppendItem(itd)
		self.Bind(wx.EVT_MENU, self.OnRed2, itd)	

		itp = wx.MenuItem(menu4, -1, _('Open prz.ini for edit'))
		itp.SetBitmap(wx.Bitmap(kit))
		menu4.AppendItem(itp)
		self.Bind(wx.EVT_MENU, self.OnRed3, itp)		
		menu4.AppendSeparator()
		
		itmN = wx.MenuItem(menu4, -1, _("Settings"))
		kart = sys_inf.ICON_PATH + 'edit.png'
		itmN.SetBitmap(wx.Bitmap(kart))
		menu4.AppendItem(itmN)
		self.Bind(wx.EVT_MENU, self.OnN, itmN)
		menu5 = wx.Menu()
		menuBar.Append(menu5, _("Tutorial"))
		
		itm8 = wx.MenuItem(menu5, -1, _('Open tutorial'))
		itm8.SetBitmap(wx.Bitmap(f7))
		menu5.AppendItem(itm8)
		self.Bind(wx.EVT_MENU, self.On8, itm8)
		
		itm9 = wx.MenuItem(menu5, -1, _('About'))
		itm9.SetBitmap(wx.Bitmap(f8))
		menu5.AppendItem(itm9)
		self.Bind(wx.EVT_MENU, self.On9, itm9)
		self.SetMenuBar(menuBar)
		# тулбар
		self.tb = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT)
		
		if conf_db.Dobd_class('toolbar').baz_vst() != 'Not':# пок/скр тулбар
			self.tb.Show()
		else:
			self.tb.Hide()
		
		Rec = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'obn.png'), _('Update'))
		Filot = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'fileot.png'), _('Open'))
		self.tb.AddSeparator()
		
		podws = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'podw.png'), _('GoEnd'))
		
		poups = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'poup.png'), _('GoHome'))
		self.tb.AddSeparator()
		
		on5 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + '4b.png'), _('Write image'))
		
		on6 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + '5b.png'), _('Choice font'))
		
		on7 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + '6b.png'), _('Choice colour'))
		self.tb.AddSeparator()
		
		on9 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + '8b.png'), _('Save as'))
		
		on10 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + '9b.png'), _('Save real'))
		self.tb.AddSeparator()
		
		on11 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-text-bold.png'), _('Bold'))
		
		on12 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-text-italic.png'), _('Italic'))
		
		on13 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-text-underline.png'), _('Underline'))
		
		self.Bind(wx.EVT_TOOL, self.Seg, Rec)
		self.Bind(wx.EVT_TOOL, self.Fileot, Filot)
		self.Bind(wx.EVT_TOOL, self.OnImageOpen, on5)
		self.Bind(wx.EVT_TOOL, self.OnFont, on6)
		self.Bind(wx.EVT_TOOL, self.OnColour, on7)
		self.Bind(wx.EVT_TOOL, self.OnFileSaveAs, on9)
		self.Bind(wx.EVT_TOOL, self.FileSave, on10)
		self.Bind(wx.EVT_TOOL, self.Bold, on11)
		self.Bind(wx.EVT_TOOL, self.It, on12)
		self.Bind(wx.EVT_TOOL, self.Poc, on13)
		self.Bind(wx.EVT_TOOL, self.PosDw, podws)
		self.Bind(wx.EVT_TOOL, self.PosUp, poups)
		
		self.tb.AddSeparator()
		
		li = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-justify-left.png'), _('Left'))
		ct = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-justify-center.png'), _('Centre'))
		
		pr = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'format-justify-right.png'), _('Right'))

		self.tb.AddSeparator()
		
		on8 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + '7b.png'), _('Clear'))
		self.Bind(wx.EVT_TOOL, self.Clears, on8)
		self.tb.AddSeparator()
		
		goods = int(time.strftime('%G'))
		# выбор месяцев и годов для переключения календаря
		montd = [_('Jan'), _('Feb'), _('Mar'), _('Apr'), _('May'), _('Jun'), _('Jul'), _('Aug'), _('Sep'), _('Oct'), _('Nov'), _('Dec')]
		self.ch = wx.ComboBox(self.tb, -1, value = '', choices=montd, size=(100, 22), style=wx.CB_DROPDOWN)
		
		self.ch2 = wx.SpinCtrl(self.tb, value=str(goods), size=(60, 22), min=1970, max=2100)
		
		self.Bind(wx.EVT_TOOL, self.To_Left, li)
		self.Bind(wx.EVT_TOOL, self.To_Center, ct)
		self.Bind(wx.EVT_TOOL, self.To_Right, pr)
		
		self.tb.AddControl(self.ch)

		self.tb.AddControl(self.ch2)
		
		self.tb.AddSeparator()
		
		dont = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'b.png'), _('Go'))
		self.Bind(wx.EVT_TOOL, self.Vub, dont)
		
		Seg = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'b2.png'), _('Revert'))
		self.Bind(wx.EVT_TOOL, self.Seg, Seg)
		self.tb.AddSeparator()
		
		lin2 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + '16.png'),_('Write lines') )
		
		link2 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH  + 'a.png'), _('Write link to file'))
		
		ntl = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 's.png'), _('Remember'))
		self.Bind(wx.EVT_TOOL, self.PanNaps, ntl)
		self.tb.AddSeparator()
		
		ont = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'p.png'), _('Tutorial(ru)'))
		self.Bind(wx.EVT_TOOL, self.On8, ont)

		tnop = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'nas.png'), _('Settings'))
		self.Bind(wx.EVT_TOOL, self.OnN, tnop)
		self.tb.AddSeparator()
		self.Bind(wx.EVT_TOOL, self.Write_Line, lin2)
		self.Bind(wx.EVT_TOOL, self.URL_L, link2)
		
		on14 = self.tb.AddSimpleTool(-1, wx.Bitmap(sys_inf.ICON_PATH + 'e.png'), _('Exit'))
		self.Bind(wx.EVT_TOOL, self.OnCloseWindow, on14)
		
		# по дефолту - на сегодня
		i = int(time.strftime('%m')) - 1
		ds = int(time.strftime('%G'))
		# дата и таймер
		if sys_inf.Loc() == 'ru_RU':
			god = ' года  '
		else:
			god = ' year  '
		self.f = time.strftime('%A, ') + sys_inf.Once() + ' ' + time.strftime('%h, ') + time.strftime('%G') + god
		
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		self.timer.Start(1000)
		
		# ++++++++++++++++++++++
		self.Wins()
		# ++++++++++++++++++++++
		
		# статусбар
		self.sb = wx.StatusBar(self, -1)
		self.sb.SetBackgroundColour(conf_db.Dobd_class('colorviz').baz_vst())
		self.sb.SetFieldsCount(3)
		self.sb.SetStatusText(self.RetDay(), 2)
		
		# перетаскивать файлы
		dt = drag_drop.FileDrop(self.win)
		self.win.SetDropTarget(dt)
		
		# ++++++++++++++++++++++
		self.Pan_One()
		self.Pno(i, ds)		
		self.Sz()
		# ++++++++++++++++++++++
		
	def FilSt(self):# показывает файл в первом(0) отделе
		if self.win.GetFilename() != '':
			try:
				if self.win.GetFilename().split('/')[6]:
					ot = self.win.GetFilename().split('/')[6]
			except:
				ot = self.win.GetFilename()
		else:
			ot = _('New File')
		return ot
		
# часики в статусбаре
	def ChasY(self):
		self.sb.SetStatusText(self.FilSt(), 0)
		self.sb.SetStatusText(self.f + time.strftime('%H:%M:%S'), 1)
		
	def update(self, event):
		self.ChasY()
		
# обновляющая-переключающая функ. 
	def Pno(self, a, b):
		try:
			if self.panel2:
				self.panel2.Destroy()
				self.Pan_Tu()
		except AttributeError:
			self.Pan_Tu()
		try:
			if self.panel3:
				self.panel3.Destroy()
				self.Pan_Tr(a, b)
		except AttributeError:		
			self.Pan_Tr(a, b)

# сами notebook функции			
	def Pan_One(self):
		self.panel = wx.Panel(self)
		self.notebook = wx.Notebook(self.panel)
		if self.dis[1] > 500:
			tabOne = soxr_diary.Soxr(self.notebook, self.win)
			self.notebook.AddPage(tabOne, _("Save day"))
		tabTrya = searching.TabSearh(self.notebook, self.win)
		self.notebook.AddPage(tabTrya, _("Search notes"))	
		self.gsizer = wx.BoxSizer(wx.VERTICAL)
		self.gsizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)
		self.panel.SetSizer(self.gsizer)
		self.Layout()
		
	def Pan_Tu(self):
		self.panel2 = wx.Panel(self)
		self.notebook2 = wx.Notebook(self.panel2)
		tab1 = uni_pan.TabPanel(self.notebook2, self.win, 'Data', _('My diary'))
		self.notebook2.AddPage(tab1, _("Diary"))
		tab3 = uni_pan.TabPanel(self.notebook2, self.win, 'Other', _('My notes'))
		self.notebook2.AddPage(tab3, _("Notes"))
		self.gsizer2 = wx.BoxSizer(wx.VERTICAL)
		self.gsizer2.Add(self.notebook2, 1, wx.ALL|wx.EXPAND, 5)
		self.panel2.SetSizer(self.gsizer2)
		self.Layout()
	
	def Pan_Tr(self, c, d):
		self.panel3 = wx.Panel(self)
		self.notebook3 = wx.Notebook(self.panel3)
		tabCal =  Caldar.SimpleGrid(self.notebook3, c, d, self.win, self.dis[4], self.dis[5], 'Diary')
		self.notebook3.AddPage(tabCal, _("Calendar"))
		if self.dis[1] > 600:# никак не укладывается в меньше...
			tabCald =  Sheet.NedSheet(self.notebook3)
			self.notebook3.AddPage(tabCald, _("Real Week"))
		tabDay = day.Seg_Day(self.notebook3)
		self.notebook3.AddPage(tabDay, _("Day"))
		self.gsizer3 = wx.BoxSizer(wx.VERTICAL)
		self.gsizer3.Add(self.notebook3, 1, wx.ALL|wx.EXPAND, 0)
		self.panel3.SetSizer(self.gsizer3)
		self.Layout()
		
# открытие, сохранение...	
	def On1(self, event):
		panel_richtext.Upim_Writer().Show()
		
	# позиция	
	def PosDw(self, event):
		self.win.ShowPosition(len(self.win.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')))
		
	def PosUp(self, event):
		self.win.ShowPosition(2)
		
	# бинд заметок на календаре	
	def Ckb(self, event):
		if self.itm.IsChecked() == False:
			conf_db.Ubd_class('caloff', 'Off').baz_vsb()
		else:
			conf_db.Ubd_class('caloff', 'On').baz_vsb()
	
	# открытые файлы
	def Fileot(self, event):
		im = sys_inf.ICON_PATH + 's1.png'
		self.submenu = wx.Menu()
		for i in conf_db.nedlist:
			try:
				if i.split('/')[6]:
					a = i.split('/')[6]
					items = wx.MenuItem(self.submenu, -1, a.split('.')[0])
					items.SetBitmap(wx.Bitmap(im))
					self.Bind(wx.EVT_MENU, self.Lows, items)
					self.submenu.AppendItem(items)
			except:
				pass
		self.PopupMenu(self.submenu)
		
	def Lows(self, event):
		rec = self.submenu.FindItemById(event.GetId())
		partc = rec.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		for y in conf_db.nedlist:
			try:
				if y.split('/')[6]:
					if partc + '.ox' == y.split('/')[6]:
						self.win.LoadFile(y)
			except:
				pass
				
	def On2(self, event):
		wildcard= "Page ox (*.ox)|*.ox|"
		dlg = wx.FileDialog(self, _("Choice file"), sys_inf.DATA_PATH, wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			if path:
				panel_richtext.Upim_Writer(path).Show()			
		dlg.Destroy()
	# печать	
	def Print(self, event):
		if self.win.GetFilename() != '':
			self.printer = text.RichTextPrinting()
			self.printer.GetPrintData()
			self.printer.PrintFile(self.win.GetFilename())	
	# открыть...		
	def On3(self, event):
		wildcard= "Page ox (*.ox)|*.ox|"
		dlg = wx.FileDialog(self, _("Choice file"), sys_inf.DATA_PATH, wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			pathh = dlg.GetPath().encode('utf-8').decode('latin-1').encode('latin-1')
			self.win.LoadFile(pathh)
			conf_db.Listrem(pathh)
		dlg.Destroy()
	
	def OnRed(self, event):
		fgl = sys_inf.CONF_PATH + '.diarus.ini'
		os.system('xdg-open ' + fgl + ' &')
		
	def OnRed2(self, event):
		fgl2 = sys_inf.DATA_PATH + 'Pattern/shab'
		os.system('xdg-open ' + fgl2 + ' &')
		
	def OnRed3(self, event):
		fgp = sys_inf.CONF_PATH + 'prz.ini'
		os.system('xdg-open ' + fgp + ' &')
	
	def OnN(self, event):
		os.system('python ' + sys_inf.UPIM_PATH + 'configuration.py &')
	
	def To_Left(self, event):
		self.win.ApplyAlignmentToSelection(text.TEXT_ALIGNMENT_LEFT) 
		
	def To_Center(self, event):
		self.win.ApplyAlignmentToSelection(text.TEXT_ALIGNMENT_CENTRE)
		
	def To_Right(self, event):
		self.win.ApplyAlignmentToSelection(text.TEXT_ALIGNMENT_RIGHT)
		
	# статус этого дня		
	def RetDay(self):
		files = sys_inf.CONF_PATH + 'prz.ini'
		for i in open(files, 'rb').readlines():
			if time.strftime('%d') + ':' + time.strftime('%h') == i.split(';')[0]:
				day = i.split(';')[1]
				break
			else:
				if time.strftime('%A') == _("Saturday"):
					day = _('Pre-holiday')
				elif time.strftime('%A') == _("Sunday"):
					day = _('Holiday')
				else:
					day = _("Weekday")		
		return day
		
	def Write_Line(self, event):
		self.win.WriteText(int(conf_db.Dobd_class('ul').baz_vst())*'-' + '\n')
		
	def On8(self, event):
		if sys_inf.Loc() == 'ru_RU':
			self.win.LoadFile('/usr/local/share/upim/ManualRU.ox')
		else:
			self.win.Clear()
			self.win.WriteText('Not tutorial to ' + sys_inf.Loc().split('_')[1] + ' language! :-(')
			
	# я не знаю доподлинно, что здесь написано	
	def On9(self, event):	
		description = """Upim Manager is an advanced content-richtext manager for 
Linux operating system. Features include powerful richtext editor, 
advanced search capabilities and more...
"""
		lic = '/usr/local/share/upim/LICENSE'
		licence = open(lic, 'r').read()
		info = wx.AboutDialogInfo()
		info.SetName('Upim Manager')
		info.SetIcon(wx.Icon(sys_inf.ICON_PATH + 'upim.png', wx.BITMAP_TYPE_PNG))
		info.SetVersion('1.0.4')
		info.SetDescription(description)
		info.SetCopyright('(C) 2013 - 2017 Victor Frig')
		info.SetLicence(licence)
		info.AddDeveloper('Victor Frig aka Prohodimec')
		wx.AboutBox(info)


	
	# картинки, примерные функции, шрифты-цвет	
	def OnImageOpen(self, event):
		import imag
		imag.TestFrame(self.win).Show()

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
		
	# визор заметок
	
	def Wins(self):
		self.win = text.RichTextCtrl(self, style = wx.DEFAULT_FRAME_STYLE)
		self.col_back()
		self.win.SetMinSize( (self.dis[0] - 400, self.dis[3]) )
		self.win.Bind(wx.EVT_TEXT_URL, self.OnURL)
		font2 = wx.Font(conf_db.Dobd_class('fontrazviz').baz_vst(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, conf_db.Dobd_class('fontviz').baz_vst())
		self.win.SetFont(font2)
		self.AddRTCHandlers()
		# цвет текста взависимости от темы
		if conf_db.Dobd_class('colorviz').baz_vst() == '#FFFFFF':
			self.win.BeginTextColour((0, 0, 0))
		else:
			self.win.BeginTextColour((255, 255, 255))
			
		# заголовок в зависимости от локали	
		if sys_inf.Loc() == 'ru_RU':
			h = time.strftime('%H:%M мин. %d %h %G года\n') + int(conf_db.Dobd_class('ul').baz_vst())*'-' + '\n'
		else:
			h = time.strftime('%H:%M min %d %h %G year\n') + int(conf_db.Dobd_class('ul').baz_vst())*'-' + '\n'
		
		#поздравление с праздником и иконка
		files = sys_inf.CONF_PATH + 'prz.ini'
		for i in open(files, 'rb').readlines():
			if time.strftime('%d') + ':' + time.strftime('%h') == i.split(';')[0]:
				d = i.split(';')[1] + 5*'\t'
				try:
					if i.split(';')[2]:
						im = wx.Image(i.split(';')[2].strip(), wx.BITMAP_TYPE_ANY)   
						self.win.WriteImage(im)
				except IndexError:
					pass
				break
			else:
				d = ''
				
		if conf_db.Dobd_class('posfile').baz_vst() != 'Not':# последний файл
			self.win.LoadFile(conf_db.Dobd_class('posfile').baz_vst())
		else:
			self.win.WriteText(d + h)	
			
		return self.win
		
	# напоминания	
	def PanNaps(self, event):
		os.system('python '+ sys_inf.UPIM_PATH + 'soxr_nap.py &')	
		
	#	Background
	def col_back(self):
		self.win.SetBackgroundColour(conf_db.Dobd_class('colorviz').baz_vst())

	def AddRTCHandlers(self):
		if text.RichTextBuffer.FindHandlerByType(text.RICHTEXT_TYPE_HTML) is not None:
			return
		text.RichTextBuffer.AddHandler(text.RichTextXMLHandler(name="Other XML",
                                                           ext="ox",
                                                           type=99))

		text.RichTextBuffer.AddHandler(text.RichTextHTMLHandler())
		wx.FileSystem.AddHandler(wx.MemoryFSHandler())
		
	# Вставка ссылки на файл	
	def URL_L(self, event):
		self.pnn = wx.Panel(self, -1, size=(280, 100), pos=(500, 400))
		self.pnn.SetBackgroundColour('#7180A8')
		self.aText = wx.TextCtrl(self.pnn, -1, _("Write name link"), size=(270, 30), pos=(5, 2))
		button_vub = wx.Button(self.pnn, -1, _("Choice file"), size=(270,30), pos=(5, 34))
		button_vub.Bind(wx.EVT_BUTTON, self.FILE_ap, button_vub)
		button_write = wx.Button(self.pnn, -1, _("Save"), size=(130,30), pos=(5, 66))
		button_write.Bind(wx.EVT_BUTTON, self.URL_ap, button_write)
		button_e = wx.Button(self.pnn, -1, _("Cancel"), size=(130,30), pos=(145, 66))
		button_e.Bind(wx.EVT_BUTTON, self.Ex, button_e)
	
	def URL_ap(self, event):
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
	# п>		
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
			
	# чтоб не упустить			
	def OnCloseWindow(self, event):
		if self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1') != '':
			files = self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1')
			self.PosFil(files)
			if self.win.IsModified():
				dial = wx.MessageDialog(None, _(' Do you want save changes?\n Edit file ') + files, 'Info', wx.YES_NO | wx.ICON_QUESTION)
				ret = dial.ShowModal()
				if ret == wx.ID_YES:
					self.Destroy()		
			else:
				self.Destroy()	
		else:
			self.Destroy()
		
	#последний файл --> в базу			
	def PosFil(self, fl):
		try:
			if conf_db.Dobd_class('posfile').baz_vst():
				if conf_db.Dobd_class('posfile').baz_vst() != 'Not':
					conf_db.Ubd_class('posfile', fl).baz_vsb()
		except KeyError:
			conf_db.Ubd_class('posfile', fl).baz_vsb()
				
	# п<		
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
			
	# открыть ссылку на файл, url - святым копипастием			
	def OnURL(self, event):
		try:
			if event.GetString().encode('utf-8').decode('latin-1').encode('latin-1').split('/')[6].split('.')[1] == 'ox':
				self.win.LoadFile(event.GetString().encode('utf-8').decode('latin-1').encode('latin-1'))
				conf_db.Listrem(event.GetString().encode('utf-8').decode('latin-1').encode('latin-1'))
			else:
				os.system('xdg-open ' + '"' + event.GetString().encode('utf-8').decode('latin-1').encode('latin-1') + '"' + ' &')
		except IndexError:
			os.system('xdg-open ' + '"' + event.GetString().encode('utf-8').decode('latin-1').encode('latin-1') + '"' + ' &')
		
	# мелочи
	def Clears(self, event):
		self.win.Clear()
		
	def OnClose(self, event):
		self.Destroy()
	#
	def FILE_ap(self, event):
		dlg = wx.FileDialog(self, _("Choice file"), style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.path = dlg.GetPath()
			if self.path:
				self.URL_ap()
		dlg.Destroy()
		self.pnn.Destroy()
	
	def Ex(self, event):
		self.pnn.Destroy()
		
	def Dt(self, event):
		if sys_inf.Loc() == 'ru_RU':
			self.win.WriteText(time.strftime('%d_%h_%G года  %H:%M мин'))
		else:
			self.win.WriteText(time.strftime('%d_%h_%G years  %H:%M min'))
			
	def Bold(self, event):
		self.win.ApplyBoldToSelection()
	
	def It(self, event):
		self.win.ApplyItalicToSelection()
	
	def Poc(self, event):
		self.win.ApplyUnderlineToSelection()
	
	def FileSave(self, evt):
		if self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1') != '':
			if self.win.IsModified():
				lg = wx.MessageDialog(None, _("Warning!!! Editable real file. Save editable?"), 'Info',wx.YES_NO | wx.ICON_QUESTION)
				retCode = lg.ShowModal()
				if (retCode == wx.ID_YES):
					fil = self.win.GetFilename().encode('utf-8').decode('latin-1').encode('latin-1')
					self.win.SaveFile(fil)
					self.Os(fil)
	

	def OnFileSaveHTML(self, event):
		tch = sys_inf.HOME_PATH
		wildcard= "Page html (*.html)|*.html|"
		dlg = wx.FileDialog(self, _("Create file"), tch, wildcard=wildcard, style=wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			if path:
				savep = path + '.html'
				self.win.SaveFile(savep)
		dlg.Destroy()
			
	def OnFileSaveAs(self, evt):
		tch = sys_inf.DATA_PATH + 'Other/'
		wildcard= "Page ox (*.ox)|*.ox|"
		dlg = wx.FileDialog(self, _("Create file"), tch, wildcard=wildcard, style=wx.SAVE)
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
						self.Os(savep.encode('utf-8').decode('latin-1').encode('latin-1'))							
				except IndexError:
					self.win.SaveFile(savep)
		dlg.Destroy()

# ---------------------вот эта фор-ла encode.decode спасает от ужаса ru	
	def Vub(self, event):
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Jan'):
			m = 0
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Feb'):
			m = 1
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Mar'):
			m = 2
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Apr'):
			m = 3
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('May'):
			m = 4
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Jun'):
			m = 5
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Jul'):
			m = 6
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Aug'):
			m = 7
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Sep'):
			m = 8
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Oct'):
			m = 9
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Nov'):
			m = 10
		if self.ch.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _('Dec'):
			m = 11
		try:
			if self.ch.GetValue():
				pass
		except AttributeError:
			m = int(time.strftime('%m')) - 1
		g = self.ch2.GetValue()
		self.Pno(m, g)
		self.Sz()
				
# ВАЖНАЯ ФУНКЦИЯ  - ИНДЕКСИРУЕТ ЗАМЕТКИ В BD-shelve		
	def Os(self, pth):
		p = pth.split('/')[6]
		on = self.win.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')
		conf_db.dobdb(p, on)

#СЕГОДНЯ!		
	def Seg(self, event):
		m = int(time.strftime('%m')) - 1
		g = int(time.strftime('%G'))
		self.Pno(m, g)
		self.Sz()
		
#ГЛАВНЫЙ САЙЗЕР
	def Sz(self):
		gbox = wx.BoxSizer(wx.HORIZONTAL)	
		gbox.Add(self.panel2)
		gbox.Add(self.panel3)
		gbox.Add(self.panel)
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(gbox, flag=wx.EXPAND)
		vbox.Add(self.win, 2, flag=wx.EXPAND)
		vbox.Add(self.sb)
		self.SetSizer(vbox)
		self.Fit()

if __name__ == '__main__':	
	app = wx.App()
	Upim_Manager(None).Show()
	app.MainLoop()
