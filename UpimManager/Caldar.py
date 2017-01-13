#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2016-2017 year

@author: FrIg aka Prohodimec 
"""
import wx
import os
import time
import wx.grid as gridlib
import panel_richtext
import conf_db
import sys_inf
sys_inf.GetTxt()

class SimpleGrid(gridlib.Grid):
	def __init__(self, parent, monts, goods, nwin, x, y, zet):
		self.monts = monts # int параметр месяца
		self.goods = goods # int параметр года
		self.nwin = nwin # визор заметок
		self.x = x # размеры в пикселях
		self.y = y #
		self.zet = zet # тип календаря - в зависимости какой модуль его импортирует
		gridlib.Grid.__init__(self, parent, -1)
		self.moveTo = None
		self.days = int(time.strftime('%d'))
		self.chis = []
		self.ui = sys_inf.DATA_PATH + 'Data/' + str(self.goods) + ':' + self.Diary_day() + '/'		
		
		self.Diary_day_monts()
		self.CreateGrid(5, 7)
		self.dt = wx.DateTime()
		
		self.lift = []
		fo = sys_inf.DATA_PATH + 'Other/'
		for pap in os.listdir(fo):
			filfo = fo + pap
			if os.path.isdir(filfo):
				for fap in os.listdir(filfo):
					self.lift.append(fap)
		self.lift.sort()
		
		
		for i in range(7):
			self.SetColSize(i, self.x)
			self.SetRowSize(i, self.y)
			self.SetReadOnly(i, i, True)
		
		

		self.attr = gridlib.GridCellAttr()
		if self.zet == 'Diary':
			self.attr.SetTextColour(wx.BLACK)
			self.attr.SetBackgroundColour('#1B222D')
			self.attr.SetFont(wx.Font(17, wx.SWISS, wx.NORMAL, wx.BOLD))	
		elif self.zet == 'Calendar':
			self.attr.SetTextColour('#000000')
			self.attr.SetBackgroundColour('#C6BFA4')
			self.attr.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD))															
		
		self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)
		if self.zet == 'Diary':
			self.SetLabelFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Monospace'))
			self.SetLabelTextColour(wx.BLUE)
			self.SetLabelBackgroundColour(conf_db.Dobd_class('cvetdney').baz_vst())
		elif self.zet == 'Calendar':
			self.SetLabelFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Monospace'))
			self.SetLabelTextColour('#6B000A')
			self.SetLabelBackgroundColour(conf_db.Dobd_class('colordn').baz_vst())
			
		self.Cal_S()
		self.Ch_S()
			
		il = self.GetNumberRows() + 1
		li = self.GetNumberCols() + 1
		for i in range(li):
			for a in range(il):
				self.Top(a,i)
		
		
		self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)
		self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick)
		self.Noisk()
		self.Layout()
		
# маркировка сегодня, дней без заметок праздников и чистых гридеров	
	def Top(self, one, two):
		self.a = one
		self.i = two
		nn = self.GetCellValue(self.a, self.i)
		if nn == str(self.days):
			if self.zet == 'Diary':
				self.SetCellTextColour(self.a, self.i, conf_db.Dobd_class('cvettseg').baz_vst())
				self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetseg').baz_vst())
			elif self.zet == 'Calendar':
				self.SetCellTextColour(self.a, self.i, "#FFEF0A")
				self.SetCellBackgroundColour(self.a, self.i, wx.RED)
		elif nn == '':
			if self.zet == 'Diary':
				self.SetCellBackgroundColour(self.a, self.i, str(conf_db.Dobd_class('cvetcaldnit').baz_vst()))
			elif self.zet == 'Calendar':
				self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('colordn').baz_vst())
		else:
			if self.zet == 'Diary':
				self.SetCellTextColour(self.a, self.i, conf_db.Dobd_class('cvetcaltxt').baz_vst())
				if self.i == 5:
					self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetsat').baz_vst())
				elif self.i == 6:
					self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetsun').baz_vst())
				else:
					self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetchc').baz_vst())   
			elif self.zet == 'Calendar':
				if self.i == 5:
					self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetsat').baz_vst())
				elif self.i == 6:
					self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetsun').baz_vst())
				else:
					self.SetCellBackgroundColour(self.a, self.i, conf_db.Dobd_class('cvetcal').baz_vst())   

#тот цикл, что ищет и окрашивает	заметки
	def Hoin(self, kol):
		self.kol = kol
		bb = self.GetNumberRows() + 1
		cc = self.GetNumberCols() + 1
		for id in range(cc):
			for ad in range(bb):
				mm =  self.GetCellValue(ad, id)
				if self.kol == mm:
					if self.zet == 'Diary':
						self.CatCal(ad, id, mm, 'Diary')
						self.Chiick(ad, id, mm)
					if self.zet == 'Calendar':
						self.CatCal(ad, id, mm, 'Calendar')
						
	#управление цветами категорий 1ф.
	def CatCal(self, ads, ids, ch, bn):
		if bn == 'Diary':
			for fil in os.listdir(self.ui):
				if int(fil.split(':')[0]) == int(ch):
					if int(fil.split(':')[0]) != int(self.days):
						self.CvetCol(fil, ads, ids, 0)
		if bn == 'Calendar':
			for fil in os.listdir(self.ui):
				if int(fil.split(':')[0]) == int(ch):
					if int(fil.split(':')[0]) != int(self.days):
						self.CvetCol(fil, ads, ids, 1)
					
		
		 #управление цветами категорий 2ф.
	def CvetCol(self, file, x, y, z):
		if conf_db.dbcat(file) == _('important'):
			self.SetCellBackgroundColour(x, y, '#FF297D')
			self.SetCellTextColour(x, y, '#FFFFFF')
		elif conf_db.dbcat(file) == _('personal'):
			self.SetCellBackgroundColour(x, y, '#575DE5')
			self.SetCellTextColour(x, y, '#C2D600')
		elif conf_db.dbcat(file) == _('holidays'):
			self.SetCellBackgroundColour(x, y, '#29FF3D')
			self.SetCellTextColour(x, y, '#FF29EA')
		elif conf_db.dbcat(file) == _('achievement'):
			self.SetCellBackgroundColour(x, y, '#9C75FF')
			self.SetCellTextColour(x, y, '#D7FF3D')		
		elif conf_db.dbcat(file) == _('reminders'):
			self.SetCellBackgroundColour(x, y, '#EAFF29')
			self.SetCellTextColour(x, y, '#000000')				
		elif conf_db.dbcat(file) == _('black days'):
			self.SetCellBackgroundColour(x, y, '#000000')
			self.SetCellTextColour(x, y, '#FFFFFF')	
		else:
			if z == 0:
				self.SetCellBackgroundColour(x, y, conf_db.Dobd_class('cvetzm').baz_vst())
			else:
				self.SetCellBackgroundColour(x, y, conf_db.Dobd_class('cvetzam').baz_vst())
# функция совмещения двух циклов - поиск дней с заметками					
	def Noisk(self):
		for z in self.chis:
			if str(z) == '01':
				self.Hoin('1')
			if str(z) == '02':
				self.Hoin('2')
			if str(z) == '03':
				self.Hoin('3')
			if str(z) == '04':
				self.Hoin('4')
			if str(z) == '05':
				self.Hoin('5')
			if str(z) == '06':
				self.Hoin('6')
			if str(z) == '07':
				self.Hoin('7')
			if str(z) == '08':
				self.Hoin('8')
			if str(z) == '09':
				self.Hoin('9')
			if str(z) == '10':
				self.Hoin('10')	
			if str(z) == '11':
				self.Hoin('11')	
			if str(z) == '12':
				self.Hoin('12')
			if str(z) == '13':
				self.Hoin('13')
			if str(z) == '14':
				self.Hoin('14')
			if str(z) == '15':
				self.Hoin('15')
			if str(z) == '16':
				self.Hoin('16')
			if str(z) == '17':
				self.Hoin('17')
			if str(z) == '18':
				self.Hoin('18')
			if str(z) == '19':
				self.Hoin('19')
			if str(z) == '20':
				self.Hoin('20')
			if str(z) == '21':
				self.Hoin('21')
			if str(z) == '22':
				self.Hoin('22')		
			if str(z) == '23':
				self.Hoin('23')
			if str(z) == '24':
				self.Hoin('24')
			if str(z) == '25':
				self.Hoin('25')
			if str(z) == '26':
				self.Hoin('26')
			if str(z) == '27':
				self.Hoin('27')
			if str(z) == '28':
				self.Hoin('28')
			if str(z) == '29':
				self.Hoin('29')
			if str(z) == '30':
				self.Hoin('30')
			if str(z) == '31':
				self.Hoin('31')	
				
# счётчики распределители 
	def Ch_S(self):
		for b in range(5):
			self.SetRowAttr(b, self.attr)
		self.SetRowLabelSize(0)
		self.SetColLabelValue(0, _("Mon"))
		self.SetColLabelValue(1, _("Tue"))
		self.SetColLabelValue(2, _("Wed"))
		self.SetColLabelValue(3, _("Thu"))
		self.SetColLabelValue(4, _("Fri"))
		self.SetColLabelValue(5, _("Sat"))
		self.SetColLabelValue(6, _("Sun"))	
		
	def Cal_S(self):
		hhj = self.dt.GetNumberOfDaysInMonth(self.monts, self.goods)		
		imdex_pn = []; imdex_vt = []; imdex_sr = []; imdex_ct = []
		imdex_pt = []; imdex_sb = []; imdex_vc = []
		for self.i in range(hhj):
			self.yx = self.i + 1
			self.ty = list(str(self.dt.Set(self.yx, self.monts, self.goods)).split(' '))
			if int(self.ty[1]) == 1:
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[0]:
					self.cg = 7			
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[1]:
					self.cg = 6
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[2]:
					self.cg = 5
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[3]:
					self.cg = 4
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[4]:
					self.cg = 3
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[5]:
					self.cg = 2
				if self.ty[0] == sys_inf.Cal_Slov(self.ty[0])[6]:
					self.cg = 1
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[0], imdex_pn, 0)	
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[1], imdex_vt, 1)
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[2], imdex_sr, 2)
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[3], imdex_ct, 3)
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[4], imdex_pt, 4)
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[5], imdex_sb, 5)
			self.calfun(sys_inf.Cal_Slov(self.ty[0])[6], imdex_vc, 6)
	
# фунция построения календаря		
	def calfun(self, day, lists, number):
		if day in self.ty[0:1]:
			lists.append(1)
			self.SetCellValue(self.Nedela(self.yx), number, str(self.yx))
			
#меню	
	def OnCellRightClick(self, evt):
		self.click = self.GetCellValue(evt.GetRow(), evt.GetCol())
		self.popupmenus = wx.Menu()
		#иконки категорий
		m = sys_inf.ICON_PATH + 'vaj.png'
		m2 = sys_inf.ICON_PATH + 'lic.png'
		m3 = sys_inf.ICON_PATH + 'prz.png'
		m4 = sys_inf.ICON_PATH + 'pam.png'
		m5 = sys_inf.ICON_PATH + 'che.png'
		m6 = sys_inf.ICON_PATH + 'sna.png'
		m7 = sys_inf.ICON_PATH + 'dost.png'
		#иконки категорий
		f = sys_inf.ICON_PATH + 'et1.png'
		fil3f = sys_inf.ICON_PATH + 'cut.png'
		self.flist = []		
		if os.path.exists(self.ui):
			for fol in os.listdir(self.ui):
				if int(fol.split(':')[0]) == int(self.click.split('\n')[0]):
					submenu2 = wx.Menu()
					pop = fol.split('.')[0]
					self.flist.append(pop)
					ite0 = wx.MenuItem(self.popupmenus, -1, pop)
					ite0.SetBitmap(wx.Bitmap(f))
					self.popupmenus.AppendItem(ite0)
					self.Bind(wx.EVT_MENU, self.OP2, ite0)
					self.popupmenus.AppendSeparator()
					#категории
					itm = wx.MenuItem(submenu2, -1, _('important'))		
					itm.SetBitmap(wx.Bitmap(m))
					submenu2.AppendItem(itm)
					self.Bind(wx.EVT_MENU, self.CalCat, itm)
					itm2 = wx.MenuItem(submenu2, -1, _('personal'))		
					itm2.SetBitmap(wx.Bitmap(m2))
					submenu2.AppendItem(itm2)
					self.Bind(wx.EVT_MENU, self.CalCat, itm2)
					itm3 = wx.MenuItem(submenu2, -1, _('holidays'))		
					itm3.SetBitmap(wx.Bitmap(m3))
					submenu2.AppendItem(itm3)
					self.Bind(wx.EVT_MENU, self.CalCat, itm3)
					itm4 = wx.MenuItem(submenu2, -1, _('reminders'))		
					itm4.SetBitmap(wx.Bitmap(m4))
					submenu2.AppendItem(itm4)
					self.Bind(wx.EVT_MENU, self.CalCat, itm4)
					itm7 = wx.MenuItem(submenu2, -1, _('achievement'))		
					itm7.SetBitmap(wx.Bitmap(m7))
					submenu2.AppendItem(itm7)
					self.Bind(wx.EVT_MENU, self.CalCat, itm7)
					itm5 = wx.MenuItem(submenu2, -1, _('black days'))		
					itm5.SetBitmap(wx.Bitmap(m5))
					submenu2.AppendItem(itm5)
					self.Bind(wx.EVT_MENU, self.CalCat, itm5)
					submenu2.AppendSeparator()
					itm6 = wx.MenuItem(submenu2, -1, _('delete category'))		
					itm6.SetBitmap(wx.Bitmap(m6))
					submenu2.AppendItem(itm6)
					self.Bind(wx.EVT_MENU, self.CalCat, itm6)
					self.popupmenus.AppendMenu(-1, _("Add category"), submenu2)
					self.popupmenus.AppendSeparator()
					#категории
		if self.zet == 'Calendar':
			fs = sys_inf.ICON_PATH + 'ev.png'
			submenu = wx.Menu()
			for lisst in self.lift:
				it = wx.MenuItem(submenu, -1, lisst.split('.')[0])		
				it.SetBitmap(wx.Bitmap(fs))
				submenu.AppendItem(it)
				submenu.Bind(wx.EVT_MENU, self.OP5, it)	
			self.popupmenus.AppendMenu(-1, _("Notes"), submenu)
			self.popupmenus.AppendSeparator()	
		itedel = wx.MenuItem(self.popupmenus, -1, _("Remove all notes day"))
		itedel.SetBitmap(wx.Bitmap(fil3f))
		self.popupmenus.AppendItem(itedel)
		self.Bind(wx.EVT_MENU, self.OP3, itedel)
		self.PopupMenu(self.popupmenus)
		
# функция движения по каталогам год:месяц и возвращающая месяц	
	def Diary_day(self):
		if sys_inf.Loc().split('_')[0] == 'ru':
			if self.monts == 0:
				chislo = 'янв'
			elif self.monts == 1:
				chislo = 'фев'
			elif self.monts == 2:
				chislo = 'мар'
			elif self.monts == 3:
				chislo = 'апр'
			elif self.monts == 4:
				chislo = 'май'
			elif self.monts == 5:
				chislo = 'июн'
			elif self.monts == 6:
				chislo = 'июл'
			elif self.monts == 7:
				chislo = 'авг'
			elif self.monts == 8:
				chislo = 'сен'
			elif self.monts == 9:
				chislo = 'окт'
			elif self.monts == 10:
				chislo = 'ноя'
			elif self.monts == 11:
				chislo = 'дек'
		else:
			if self.monts == 0:
				chislo = 'Jan'
			elif self.monts == 1:
				chislo = 'Feb'
			elif self.monts == 2:
				chislo = 'Mar'
			elif self.monts == 3:
				chislo = 'Apr'
			elif self.monts == 4:
				chislo = 'May'
			elif self.monts == 5:
				chislo = 'Jun'
			elif self.monts == 6:
				chislo = 'Jul'
			elif self.monts == 7:
				chislo = 'Aug'
			elif self.monts == 8:
				chislo = 'Sep'
			elif self.monts == 9:
				chislo = 'Oct'
			elif self.monts == 10:
				chislo = 'Nov'
			elif self.monts == 11:
				chislo = 'Dec'
		return chislo
		
# находит существующие заметки и добавляет их в лист		
	def Diary_day_monts(self):
		if os.path.exists(self.ui):
			for f in os.listdir(self.ui):
				self.chis.append(f.split(':')[0])
				
# функция LeftClick биндинга
	def OnCellLeftClick(self, evt):
		value = self.GetCellValue(evt.GetRow(), evt.GetCol()).encode('utf-8').decode('latin-1').encode('latin-1')
		for fil in os.listdir(self.ui):
			if int(fil.split(':')[0]) == int(value.split('\n')[0]):
				pt = self.ui + fil
				if self.zet == 'Diary':
					self.nwin.LoadFile(pt)
					conf_db.Listrem(pt)
				elif self.zet == 'Calendar':
					panel_richtext.Upim_Writer(patch=pt).Show()
					
# биндинг категорий 
	def CalCat(self, evt):
		itemc = self.popupmenus.FindItemById(evt.GetId())
		itemcs = itemc.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		pr = self.click.encode('utf-8').decode('latin-1').encode('latin-1')
		for fil in os.listdir(self.ui):
			if int(fil.split(':')[0]) == int(pr.split('\n')[0]):
				if itemcs != 'снять категорию':
					conf_db.catdb(fil, itemcs)
				else:
					conf_db.rmcat(fil) 
	
# функция вида дней с заметками	
	def Chiick(self, ad, id, vk):
		for fil in os.listdir(self.ui):
			if int(fil.split(':')[0]) == int(vk):
				self.SetCellFont(ad, id, wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
				kd = fil.split(':')[2]
				hj = kd.split('.')[0]
				one = hj.split(' ')[0]
				try:
					two = hj.split(' ')[1]
				except IndexError:
					two = ' '
				if conf_db.Dobd_class('caloff').baz_vst() == 'On':
					self.SetCellFont(ad, id, wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))
					self.SetCellValue(ad, id, str(vk) + '\n' + one + '\n' + two)
				else:
					self.SetCellFont(ad, id, wx.Font(17, wx.SWISS, wx.NORMAL, wx.BOLD))
					self.SetCellValue(ad, id, str(vk))
#	эвенты
	def OP3(self, event):
		for fol in os.listdir(self.ui):
			if int(fol.split(':')[0]) == int(self.click.split('\n')[0]):
				os.remove(self.ui + fol)
			
		
	def OP2(self, event):
		item1 = self.popupmenus.FindItemById(event.GetId())
		items1 = item1.GetText().encode('utf-8').decode('latin-1').encode('latin-1')
		for a in self.flist:
			if a == items1:
				panel_richtext.Upim_Writer(self.ui + a + '.ox').Show()


	def OP5(self, event):
		item = self.popupmenus.FindItemById(event.GetId())
		items = item.GetText().encode('utf-8').decode('latin-1').encode('latin-1') + '.ox'
		fom = sys_inf.DATA_PATH + 'Other/'
		for fots in os.listdir(fom):
			patchj = fom + fots
			for futa in os.listdir(patchj):
				if futa == items:
					panel_richtext.Upim_Writer(patch=patchj + '/' + futa).Show()
					
# основная, строящая расположение дней в календаре функция
	def Nedela(self, chk):
		if self.cg == 7:
			if chk <= 7:
				self.chff = 0
			if 7 < chk <= 14:
				self.chff = 1
			if 14 < chk <= 21:
				self.chff = 2
			if 21 < chk <= 28:
				self.chff = 3
			if chk > 28:
				self.chff = 4		
		elif self.cg == 6:		
			if chk <= 6:
				self.chff = 0
			if 6 < chk <= 13:
				self.chff = 1
			if 13 < chk <= 20:
				self.chff = 2
			if 20 < chk <= 27:
				self.chff = 3
			if chk > 27:
				self.chff = 4
		elif self.cg == 5:
			if chk <= 5:
				self.chff = 0
			if 5 < chk <= 12:
				self.chff = 1
			if 12 < chk <= 19:
				self.chff = 2
			if 19 < chk <= 26:
				self.chff = 3
			if chk > 26:
				self.chff = 4
		elif self.cg == 4:
			if chk <= 4:
				self.chff = 0
			if 4 < chk <= 11:
				self.chff = 1
			if 11 < chk <= 18:
				self.chff = 2
			if 18 < chk <= 25:
				self.chff = 3
			if chk > 25:
				self.chff = 4
		elif self.cg == 3:
			if chk <= 3:
				self.chff = 0
			if 3 < chk <= 10:
				self.chff = 1
			if 10 < chk <= 17:
				self.chff = 2
			if 17 < chk <= 24:
				self.chff = 3
			if chk > 24:
				self.chff = 4
		elif self.cg == 2:
			if chk <= 2:
				self.chff = 0
			if 2 < chk <= 9:
				self.chff = 1
			if 9 < chk <= 16:
				self.chff = 2
			if 16 < chk <= 23:
				self.chff = 3
			if chk > 23:
				if chk == 31:
					self.chff = 0
				else:
					self.chff = 4
		elif self.cg == 1:
			if chk <= 1:
				self.chff = 0
			if 1 < chk <= 8:
				self.chff = 1
			if 8 < chk <= 15:
				self.chff = 2
			if 15 < chk <= 22:
				self.chff = 3
			if chk > 22:
				if chk == 30:
					self.chff = 0
				elif chk == 31:
					self.chff = 0
				else:
					self.chff = 4
		return self.chff
