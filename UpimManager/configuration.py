#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:14:33 2016

@author: Prohodimec 
"""
import wx
import conf_db
from sys_inf import ICON_PATH
from sys_inf import CONF_PATH
from sys_inf import GetTxt
GetTxt()
# простой хотя и муторный конфигурвтор
class TabPan(wx.Panel):# панель основных настроек
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		#рисуем гробики
		wx.StaticLine(self, -1, (12, 2), (210, 5), style=wx.LI_HORIZONTAL)
		wx.StaticLine(self, -1, (12, 79), (210, 5), style=wx.LI_HORIZONTAL)
		wx.StaticLine(self, -1, (220, 5), (5, 240), style=wx.LI_VERTICAL)
		wx.StaticLine(self, -1, (10, 5), (5, 240), style=wx.LI_VERTICAL)
# ===============================================================		
		wx.StaticText(self, -1, _("Load note to old session"), (30, 10))
		self.chk = wx.CheckBox(self, -1, _("Load"), (65, 40))
		
		if conf_db.Dobd_class('posfile').baz_vst() != 'Not':
			self.chk.SetValue(True)
		else:
			self.chk.SetValue(False)
		self.chk.Bind(wx.EVT_CHECKBOX, self.CK, self.chk)
# ===============================================================			
		wx.StaticText(self, -1, _("Load splash screen"), (40, 90))
		self.chk2 = wx.CheckBox(self, -1, _("Load"), (65, 115))
		wx.StaticLine(self, -1, (12, 150), (210, 5), style=wx.LI_HORIZONTAL)
		if conf_db.Dobd_class('splash').baz_vst() != 'Not':
			self.chk2.SetValue(True)
		else:
			self.chk2.SetValue(False)
		self.chk2.Bind(wx.EVT_CHECKBOX, self.CK, self.chk2)
# ===============================================================			
		wx.StaticText(self, -1, _("Show/Hide toolbar to UM-UW"), (26, 164))
		wx.StaticText(self, -1, _("Show/Hide toolbar to UM-UW"), (26, 164))
		self.chk3 = wx.CheckBox(self, -1, _("Load"), (65, 190))
		if conf_db.Dobd_class('toolbar').baz_vst() != 'Not':
			self.chk3.SetValue(True)
		else:
			self.chk3.SetValue(False)
		self.chk3.Bind(wx.EVT_CHECKBOX, self.CK, self.chk3)
# ===============================================================			
		wx.StaticLine(self, -1, (12, 240), (210, 5), style=wx.LI_HORIZONTAL)
		wx.StaticLine(self, -1, (240, 2), (320, 5), style=wx.LI_HORIZONTAL)
		wx.StaticLine(self, -1, (238, 5), (5, 240), style=wx.LI_VERTICAL)
		wx.StaticLine(self, -1, (556, 5), (5, 240), style=wx.LI_VERTICAL)
		wx.StaticLine(self, -1, (240, 79), (320, 5), style=wx.LI_HORIZONTAL)
# линия дня(продолжительность(число знаков(рис. на кнопке 'равно'('='))))
		wx.StaticText(self, -1, _("Wide line [* '-']"), (360, 10))
		self.txl = wx.TextCtrl(self, -1, conf_db.Dobd_class('ul').baz_vst(), size=(60, 30), pos=(270, 36))
		wx.StaticText(self, -1, _("To UM/UW"), (335, 40))
		self.txl2 = wx.TextCtrl(self, -1, conf_db.Dobd_class('dl').baz_vst(), size=(60, 30), pos=(410, 36))
		wx.StaticText(self, -1, _("To Daysheet"), (473, 40))
# шрифты и их размер для день-транспоранта и запись-лозунга
		motd11 = ['Times', 'Times New Roman', 'Comic Sans MS', 'Exposure COutline', 'FreeMono', 'FreeSans', 'Monospace', 'Pet Me', 'PR Number 3', 'QumpellkaNo12']
		self.cfh33 = wx.ComboBox(self, -1, value = conf_db.Dobd_class('fontdays').baz_vst(), choices=motd11, size=(180, 30), pos=(270, 110), style=wx.CB_DROPDOWN)
		
		self.cfh34 = wx.SpinCtrl(self, value = str(conf_db.Dobd_class('fontrazdays').baz_vst()), size=(80, 30), pos=(450, 110), min=8, max=86)
		wx.StaticText(self, -1, _("Font and size for daysheet"), (310, 90))
		wx.StaticLine(self, -1, (240, 150), (320, 5), style=wx.LI_HORIZONTAL)
		wx.StaticText(self, -1, _("Font and size for savesheet"), (310, 170))
		
		self.sashf = wx.ComboBox(self, -1, value = conf_db.Dobd_class('fontwxc').baz_vst(), choices=motd11, size=(180, 30), pos=(270, 190), style=wx.CB_DROPDOWN)
		self.sash = wx.SpinCtrl(self, value = str(conf_db.Dobd_class('fontwxcal').baz_vst()), size=(80, 30), pos=(450, 190), min=6, max=46)
		wx.StaticLine(self, -1, (240, 240), (320, 5), style=wx.LI_HORIZONTAL)
# tw.
		wx.StaticLine(self, -1, (12, 260), (545, 5), style=wx.LI_HORIZONTAL)
		wx.StaticLine(self, -1, (10, 262), (5, 80), style=wx.LI_VERTICAL)
		wx.StaticLine(self, -1, (554, 262), (5, 80), style=wx.LI_VERTICAL)
		wx.StaticLine(self, -1, (12, 340), (545, 5), style=wx.LI_HORIZONTAL)
#кнопки на бинды
		btns= wx.Button(self, label=_("Save"), size=(100, 30), pos=(25, 290))
		btne= wx.Button(self, label=_("Exit"), size=(100, 30), pos=(445, 290))
		btns.Bind(wx.EVT_BUTTON, self.Fin, btns) 		
		btne.Bind(wx.EVT_BUTTON, self.Ex, btne) 			
# сами бинды
	def Ex(self, event):
		frame.Close()

	def CK(self, event):
		if self.chk.GetValue() == False:
			conf_db.Ubd_class('posfile', 'Not').baz_vsb()
		else:
			conf_db.Ubd_class('posfile', CONF_PATH + 'Zero.ox').baz_vsb()
		if self.chk2.GetValue() == False:
			conf_db.Ubd_class('splash', 'Not').baz_vsb()
		else:
			conf_db.Ubd_class('splash', 'Похрен').baz_vsb()
		if self.chk3.GetValue() == False:
			conf_db.Ubd_class('toolbar', 'Not').baz_vsb()
		else:
			conf_db.Ubd_class('toolbar', 'aga').baz_vsb()
			
	def Fin(self, event):
		conf_db.Ubd_class('fontwxc', self.sashf.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontwxcal', self.sash.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontdays', self.cfh33.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontrazdays', int(self.cfh34.GetValue())).baz_vsb()
		try:
			if int(self.txl.GetValue()):
				conf_db.Ubd_class('ul', self.txl.GetValue()).baz_vsb()
		except:
			pass
		try:
			if int(self.txl2.GetValue()):
				conf_db.Ubd_class('dl', self.txl2.GetValue()).baz_vsb()
		except:
			pass
		frame.Close()	
# далее тому подобное...		
			
class TabPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
# ===============================================================			
		wx.StaticText(self, -1, _("Font and size for") + " Upim Manager", (10, 110))
		wx.StaticText(self, -1, _("Colour visor notes Upim Manager"), (310, 10))
# ===============================================================	
		motd = ['Times', 'Times New Roman', 'Comic Sans MS', 'Exposure COutline', 'FreeMono', 'FreeSans', 'Monospace', 'Pet Me', 'PR Number 3', 'QumpellkaNo12']
		self.cfh = wx.ComboBox(self, -1, value = conf_db.Dobd_class('fontviz').baz_vst(), choices=motd, size=(180, 30), pos=(10, 150), style=wx.CB_DROPDOWN)
# ===============================================================	
		wx.StaticText(self, -1, _( "Choice theme Upim"), (10, 10))
		th = ['Metal', 'Brown', 'Black', 'Blue', 'Red', 'Light']
		self.th = wx.ComboBox(self, -1, value = 'Metal', choices=th, size=(180, 30), pos=(5, 50), style=wx.CB_DROPDOWN)
		bt = wx.Button(self, label=_("Select"), pos=(185, 50))
		bt.Bind(wx.EVT_BUTTON, self.Themes, bt)
# ===============================================================	
		self.cfh2 = wx.SpinCtrl(self, value = str(conf_db.Dobd_class('fontrazviz').baz_vst()), size=(80, 30), pos=(205, 150), min=8, max=86)
# ===============================================================	
		self.tt = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 50))
		self.tt.SetBackgroundColour(conf_db.Dobd_class('colorviz').baz_vst())
		btc = wx.Button(self, label=_("Select"), pos=(485, 50))
		btc.Bind(wx.EVT_BUTTON, self.Ct, btc)
# ===============================================================			
		btn = wx.Button(self, label=_("Write changes for fonts"), size=(280, 30), pos=(5, 320))
		btn.Bind(wx.EVT_BUTTON, self.Final, btn) 	
# ===============================================================			
		btno = wx.Button(self, label=_("Exit"), pos=(480, 320))
		btno.Bind(wx.EVT_BUTTON, self.Exit, btno)
# ===============================================================			
		wx.StaticText(self, -1, _("Select colour font tray"), (320, 110))
		self.tct = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 150))
		self.tct.SetBackgroundColour(conf_db.Dobd_class('cvetmencr').baz_vst())
		btk = wx.Button(self, label=_("Select"), pos=(485, 150))
		btk.Bind(wx.EVT_BUTTON, self.Ctp, btk)
# ===============================================================	
		wx.StaticText(self, -1, _("Select font tray folder"), (10, 210))
		wx.StaticText(self, -1, _("Select font tray note"), (320, 210))
# ===============================================================			
		mot = ['TimesItalic', 'Times New Roman', 'Comic Sans MS', 'FreeMono Normal', 'Sans', 'Arial', 'Monospace', 'PR Number 3']
		
		self.ctrh = wx.ComboBox(self, -1, value = conf_db.Dobd_class('fonttrey').baz_vst(), choices=mot, size=(180, 30), pos=(10, 250), style=wx.CB_DROPDOWN)

		self.ctrh3 = wx.ComboBox(self, -1, value = conf_db.Dobd_class('fonttreyIt').baz_vst(), choices=mot, size=(180, 30), pos=(300, 250), style=wx.CB_DROPDOWN)
        
		self.ctrh2 = wx.SpinCtrl(self, value = str(conf_db.Dobd_class('fontraztrey').baz_vst()), size=(80, 30), pos=(195, 250), min=8, max=86)
		
		self.ctrh4 = wx.SpinCtrl(self, value = str(conf_db.Dobd_class('fontraztreyIt').baz_vst()), size=(80, 30), pos=(485, 250), min=8, max=86)
        
	def Exit(self, event):
		frame.Close()
	
	def ChoiceCv(self):
		dialog = wx.ColourDialog(None)
		dialog.GetColourData().SetChooseFull(True)
		if dialog.ShowModal() == wx.ID_OK:
			self.data = dialog.GetColourData()
			return self.data
		
	def Ct(self, event):
		self.ChoiceCv()
		self.tt.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('colorviz', self.data.GetColour()).baz_vsb()
		  
	def Ctp(self, event):
		self.ChoiceCv()
		self.tct.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetmencr', self.data.GetColour()).baz_vsb()
			

	def Themes(self, event):
		if self.th.GetValue() == 'Metal':
			conf_db.Ubd_class('colorviz', '#1B222D').baz_vsb()
			conf_db.Ubd_class('cvetmencr', '#e8d890').baz_vsb()
			conf_db.Ubd_class('cvetcaldnit', '#A1A8B5').baz_vsb()
			conf_db.Ubd_class('cvettr', '#1B222D').baz_vsb()
		if self.th.GetValue() == 'Brown':
			conf_db.Ubd_class('colorviz', '#1A1914').baz_vsb()
			conf_db.Ubd_class('cvetmencr', '#AFD9BA').baz_vsb()
			conf_db.Ubd_class('cvetcaldnit', '#989697').baz_vsb()
			conf_db.Ubd_class('cvettr', '#25251D').baz_vsb()
		if self.th.GetValue() == 'Black':
			conf_db.Ubd_class('colorviz', '#000000').baz_vsb()
			conf_db.Ubd_class('cvetmencr', '#FFFFFF').baz_vsb()
			conf_db.Ubd_class('cvetcaldnit', '#A2A2A2').baz_vsb()
			conf_db.Ubd_class('cvettr', '#323339').baz_vsb()
		if self.th.GetValue() == 'Blue':
			conf_db.Ubd_class('colorviz', '#141433').baz_vsb()
			conf_db.Ubd_class('cvetmencr', '#6DBA81').baz_vsb()
			conf_db.Ubd_class('cvetcaldnit', '#94ACAC').baz_vsb()
			conf_db.Ubd_class('cvettr', '#2E2E76').baz_vsb()
		if self.th.GetValue() == 'Red':
			conf_db.Ubd_class('colorviz', '#130202').baz_vsb()
			conf_db.Ubd_class('cvetmencr', '#A7BA6D').baz_vsb()
			conf_db.Ubd_class('cvetcaldnit', '#F04C4C').baz_vsb()
			conf_db.Ubd_class('cvettr', '#390505').baz_vsb()
		if self.th.GetValue() == 'Light':
			conf_db.Ubd_class('colorviz', '#FFFFFF').baz_vsb()
			conf_db.Ubd_class('cvetmencr', '#000000').baz_vsb()
			conf_db.Ubd_class('cvetcaldnit', '#F04C4C').baz_vsb()
			conf_db.Ubd_class('cvettr', '#FFFFFF').baz_vsb()
		frame.Close()

	def Final(self, event):
		conf_db.Ubd_class('fontviz', self.cfh.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontrazviz', int(self.cfh2.GetValue())).baz_vsb()
		conf_db.Ubd_class('fonttrey', self.ctrh.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontraztrey', int(self.ctrh2.GetValue())).baz_vsb()
		conf_db.Ubd_class('fonttreyIt', self.ctrh3.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontraztreyIt', int(self.ctrh4.GetValue())).baz_vsb()		
		frame.Close()
  
class TabPanel1(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		wx.StaticText(self, -1, _("Font and size for") + " Upim Writer", (10, 10))
# ===============================================================			
		motd1 = ['Times', 'Times New Roman', 'Comic Sans MS', 'Exposure COutline', 'FreeMono', 'FreeSans', 'Monospace', 'Pet Me', 'PR Number 3', 'QumpellkaNo12']
		self.cfh1 = wx.ComboBox(self, -1, value = conf_db.Dobd_class('fontwrit').baz_vst(), choices=motd1, size=(180, 30), pos=(5, 50), style=wx.CB_DROPDOWN)
# ===============================================================			
		wx.StaticText(self, -1, _("Colour visor writer"), (310, 10))
		self.cfh3 = wx.SpinCtrl(self, value = str(conf_db.Dobd_class('fontrazwrit').baz_vst()), size=(80, 30), pos=(200, 50), min=8, max=86)
# ===============================================================		
		self.trt = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 50))
		self.trt.SetBackgroundColour(conf_db.Dobd_class('cvetwrit').baz_vst())
		btrc = wx.Button(self, label=_("Select"), pos=(485, 50))
		btrc.Bind(wx.EVT_BUTTON, self.Crt, btrc)
# ===============================================================		
		btn1 = wx.Button(self, label=_("Write changes for fonts"), size=(280, 30),pos=(5, 320))
		btn1.Bind(wx.EVT_BUTTON, self.FinalR, btn1) 
		btno = wx.Button(self, label=_("Exit"), pos=(480, 320))
		btno.Bind(wx.EVT_BUTTON, self.Exit, btno)

	def Exit(self, event):
		frame.Close()  
		
	def ChoiceCw(self):
		dialog = wx.ColourDialog(None)
		dialog.GetColourData().SetChooseFull(True)
		if dialog.ShowModal() == wx.ID_OK:
			self.data = dialog.GetColourData()
			return self.data
			
	def Crt(self, event):
		self.ChoiceCw()
		self.trt.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetwrit', self.data.GetColour()).baz_vsb()
    
	def Cwp(self, event):
		self.ChoiceCw()
		self.tct.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetpwri', self.data.GetColour()).baz_vsb()

	def FinalR(self, event):
		conf_db.Ubd_class('fontwrit', self.cfh1.GetValue()).baz_vsb()
		conf_db.Ubd_class('fontrazwrit', int(self.cfh3.GetValue())).baz_vsb()
		frame.Close()

class TabPanel2(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.SetMinSize((100, 200))
# ===============================================================	
		wx.StaticText(self, -1, _("Colour number"), (10, 10))
		self.chc = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(5, 50))
		self.chc.SetBackgroundColour(conf_db.Dobd_class('cvetchc').baz_vst())
		bch = wx.Button(self, label=_("Select"), pos=(185, 50))
		bch.Bind(wx.EVT_BUTTON, self.Chc, bch)
# ===============================================================	
		wx.StaticText(self, -1, _("Colour text"), (350, 10))
		self.cvtxt = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 50))
		self.cvtxt.SetBackgroundColour(conf_db.Dobd_class('cvetcaltxt').baz_vst())
		cvt = wx.Button(self, label=_("Select"), pos=(485, 50))
		cvt.Bind(wx.EVT_BUTTON, self.Cvtxt, cvt)
# ===============================================================	
		wx.StaticText(self, -1, _("Colour day"), (10, 110))
		self.cvdn = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(10, 150))
		self.cvdn.SetBackgroundColour(conf_db.Dobd_class('cvetdney').baz_vst())
		cvd = wx.Button(self, label=_("Select"), pos=(190, 150))
		cvd.Bind(wx.EVT_BUTTON, self.Cvd, cvd)
# ===============================================================			
		wx.StaticText(self, -1, _("Colour day notes"), (350, 110))
		self.cz = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 150))
		self.cz.SetBackgroundColour(conf_db.Dobd_class('cvetzm').baz_vst())
		zc = wx.Button(self, label=_("Select"), pos=(485, 150))
		zc.Bind(wx.EVT_BUTTON, self.Zc, zc)
# ===============================================================	
		wx.StaticText(self, -1, _("Colour background actual day"), (10, 210))
		self.cvseg = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(10, 250))
		self.cvseg.SetBackgroundColour(conf_db.Dobd_class('cvetseg').baz_vst())
		cvseg = wx.Button(self, label=_("Select"), pos=(190, 250))
		cvseg.Bind(wx.EVT_BUTTON, self.Cvseg, cvseg)
# ===============================================================				
		wx.StaticText(self, -1, _("Colour number actual day"), (350, 210))
		self.cvsegtxt = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 250))
		self.cvsegtxt.SetBackgroundColour(conf_db.Dobd_class('cvettseg').baz_vst())
		ctseg = wx.Button(self, label=_("Select"), pos=(485, 250))
		ctseg.Bind(wx.EVT_BUTTON, self.Ctseg, ctseg)
# ===============================================================		
		btno = wx.Button(self, label=_("Exit"), pos=(480, 320))
		btno.Bind(wx.EVT_BUTTON, self.Exit, btno)
		
	def Exit(self, event):
		frame.Close() 
		
	def ChoiceCal(self):
		dialog = wx.ColourDialog(None)
		dialog.GetColourData().SetChooseFull(True)
		if dialog.ShowModal() == wx.ID_OK:
			self.data = dialog.GetColourData()
			return self.data	
			
	def Zc(self, event):
		self.ChoiceCal()
		self.cz.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetzm', self.data.GetColour()).baz_vsb()   
		
	def Ctseg(self, event):
		self.ChoiceCal()
		self.cvsegtxt.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvettseg', self.data.GetColour()).baz_vsb()   
	        
	def Chc(self, event):
		self.ChoiceCal()
		self.chc.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetchc', self.data.GetColour()).baz_vsb()   
		
	def Cvtxt(self, event):
		self.ChoiceCal()
		self.cvtxt.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetcaltxt', self.data.GetColour()).baz_vsb()   
	
	def Cvd(self, event):
		self.ChoiceCal()
		self.cvdn.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetdney', self.data.GetColour()).baz_vsb()  
		
	def Cvseg(self, event):
		self.ChoiceCal()
		self.cvseg.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetseg', self.data.GetColour()).baz_vsb()        


class TabPanel4(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.SetMinSize((100, 200)) 
# ===============================================================			
		wx.StaticText(self, -1, _("Colour day"), (310, 10))
		self.tt = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 50))
		self.tt.SetBackgroundColour(conf_db.Dobd_class('colordn').baz_vst())
		btc = wx.Button(self, label=_("Select"), pos=(485, 50))
		btc.Bind(wx.EVT_BUTTON, self.Pt, btc)
# ===============================================================	
		btno = wx.Button(self, label=_("Exit"), pos=(480, 320))
		btno.Bind(wx.EVT_BUTTON, self.E, btno)
# ===============================================================	
		wx.StaticText(self, -1, _("Choice colour number"), (10, 10))
		self.tct = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(5, 50))
		self.tct.SetBackgroundColour(conf_db.Dobd_class('cvetcal').baz_vst())
		btk = wx.Button(self, label=_("Select"), pos=(185, 50))
		btk.Bind(wx.EVT_BUTTON, self.Rt, btk)
# ===============================================================	
		wx.StaticText(self, -1, _("Choice colour notes day"), (10, 120))
		self.zct = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(5, 150))
		self.zct.SetBackgroundColour(conf_db.Dobd_class('cvetzam').baz_vst())
		btz = wx.Button(self, label=_("Select"), pos=(185, 150))
		btz.Bind(wx.EVT_BUTTON, self.Zt, btz)
# ===============================================================		
		wx.StaticText(self, -1, _("Choice colour saturday"), (310, 120))
		self.csat = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(310, 150))
		self.csat.SetBackgroundColour(conf_db.Dobd_class('cvetsat').baz_vst())
		cs = wx.Button(self, label=_("Select"), pos=(490, 150))
		cs.Bind(wx.EVT_BUTTON, self.Cs, cs)
# ===============================================================			
		wx.StaticText(self, -1, _("Choice colour sunday"), (10, 220))
		self.csun = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(5, 250))	
		self.csun.SetBackgroundColour(conf_db.Dobd_class('cvetsun').baz_vst())
		csu = wx.Button(self, label=_("Select"), pos=(185, 250))
		csu.Bind(wx.EVT_BUTTON, self.Csu, csu)
		
		wx.StaticText(self, -1, _("Colour font notes for Cal UM"), (315, 220))
		self.csf = wx.TextCtrl(self, -1, "", size=(180, 30), pos=(305, 250))	
		self.csf.SetBackgroundColour(conf_db.Dobd_class('cvetnfd').baz_vst())
		csf = wx.Button(self, label=_("Select"), pos=(485, 250))
		csf.Bind(wx.EVT_BUTTON, self.Csf, csf)
		
	def E(self, event):
		frame.Close()
		
	def ChoiceCalk(self):
		dialog = wx.ColourDialog(None)
		dialog.GetColourData().SetChooseFull(True)
		if dialog.ShowModal() == wx.ID_OK:
			self.data = dialog.GetColourData()
			return self.data	

	def Csf(self, event):	
		self.ChoiceCalk()
		self.csf.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetnfd', self.data.GetColour()).baz_vsb()		

	def Csu(self, event):	
		self.ChoiceCalk()
		self.csun.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetsun', self.data.GetColour()).baz_vsb()		
		
	def Cs(self, event):	
		self.ChoiceCalk()
		self.csat.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetsat', self.data.GetColour()).baz_vsb()	
			
	def Zt(self, event):	
		self.ChoiceCalk()
		self.zct.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('cvetzam', self.data.GetColour()).baz_vsb()
			
	def Pt(self, event):
		self.ChoiceCalk()
		self.tt.SetBackgroundColour(self.data.GetColour())
		conf_db.Ubd_class('colordn', self.data.GetColour()).baz_vsb()
		  
	def Rt(self, event):
		self.ChoiceCalk()
		self.tct.SetBackgroundColour( self.data.GetColour())
		conf_db.Ubd_class('cvetcal',  self.data.GetColour()).baz_vsb()
							        
class ConfFrame(wx.Frame):# фрейм - упаковщик в нотебоксы
	def __init__(self):        
		wx.Frame.__init__(self, None, wx.ID_ANY, "ConfigurationUpim",size=(600,400), style=(wx.MINIMIZE_BOX | wx.CLOSE_BOX))	
		self.SetIcon(wx.Icon(ICON_PATH + 'nas1.png', wx.BITMAP_TYPE_PNG))			
		panel = wx.Panel(self)
		notebook = wx.Notebook(panel)
# ===============================================================	
		tabNull = TabPan(notebook)
		notebook.AddPage(tabNull, _("Primary Settings"))
# ===============================================================	
		tabOne = TabPanel(notebook)
		notebook.AddPage(tabOne, "Upim Manager")
# ===============================================================	 
		tabTwo = TabPanel1(notebook)
		notebook.AddPage(tabTwo, "Upim Writer")
# ===============================================================	
		tabTr = TabPanel2(notebook)
		notebook.AddPage(tabTr, "CalendarDiary")
# ===============================================================	        
		tabCts = TabPanel4(notebook)
		notebook.AddPage(tabCts,"CalendarTray")
# ===============================================================		
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
		panel.SetSizer(sizer)
		self.Layout()


app = wx.App(False)
frame = ConfFrame()
frame.Show()
app.MainLoop()
