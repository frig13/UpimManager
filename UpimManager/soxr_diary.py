#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import os
import  wx.calendar
import sys_inf
import conf_db
sys_inf.GetTxt()

class Soxr(wx.Panel):
	def __init__(self, parent, x):
		self.x = x
		self.dis = sys_inf.Sizer()
		wx.Panel.__init__(self, parent, -1, size=(self.dis[6], self.dis[2]))
		self.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.fonts = wx.Font(int(conf_db.Dobd_class('fontwxcal').baz_vst()), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, conf_db.Dobd_class('fontwxc').baz_vst())
		cal = wx.calendar.CalendarCtrl(self, -1, wx.DateTime_Now(), pos = (0, 0), size=(self.dis[6], 210), style=wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SEQUENTIAL_MONTH_SELECTION)
		cal.SetHeaderColours('blue', conf_db.Dobd_class('cvetdney').baz_vst())
		cal.SetHighlightColours('black', 'cyan')
		cal.SetFont(self.fonts)
		cal.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.cal = cal
		self.Bind(wx.calendar.EVT_CALENDAR, self.OnCalSelected, id=cal.GetId())
		self.basicText = wx.TextCtrl(self, -1, _("Two click to number and write name"), size=(self.dis[6]-15, 30), pos=(5,self.dis[2] - 110))

		self.basicText.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.basicText.SetForegroundColour(str(conf_db.Dobd_class('cvetmencr').baz_vst()))
		self.stt = wx.StaticText(self, -1, "                  " + _("Zero!"), size=(self.dis[6]-15, 50), pos=(5, self.dis[2] - 70))
		self.stt.SetFont(self.fonts)
		self.stt.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		self.stt.SetForegroundColour(str(conf_db.Dobd_class('cvetmencr').baz_vst()))
		buttons = wx.Button(self, 2, _("Save"), size=(self.dis[6]-15,36), pos=(5, self.dis[2] - 38))
		buttons.SetBackgroundColour(str(conf_db.Dobd_class('cvettr').baz_vst()))
		buttons.SetForegroundColour(str(conf_db.Dobd_class('cvetmencr').baz_vst()))
		buttons.SetFont(self.fonts)
		buttons.Bind(wx.EVT_BUTTON, self.Sav, id=2)
		

	def OnCalSelected(self, event):
		ll = event.GetDate()
		
		self.goos = str(ll).split(' ')[3] + ':' + str(ll).split(' ')[2]
		if self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _("Two click to number and write name"):
			self.opps = '   ' + str(ll).split(' ')[1] + ':' + str(ll).split(' ')[2] + _(':[+ choice name]')
		else:
			self.opps = '     ' + str(ll).split(' ')[1] + ':' + str(ll).split(' ')[2] + ':' + self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') + '.ox'
		self.datnam = str(ll).split(' ')[1] + ':' + str(ll).split(' ')[2]

		self.stt.SetLabel(self.opps)
		self.stt.SetFont(self.fonts)


				
	def Sav(self, event):			
		self.path = sys_inf.DATA_PATH + 'Data/'
		try:
			if self.goos:
				patchs = self.path + self.goos
				if os.path.exists(patchs):
					pass
				else:
					os.mkdir(patchs)				
				if self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') == _("Two click to number and write name"):
					self.sas = self.path + self.goos + '/' + self.datnam + ':' + 'no name' + '.ox'	
				else:
					if self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1').find('_') != -1:
						dlg = wx.MessageDialog(None, 'Error name: \"_\" not valid symbol\n No save notes!')
						dlg.ShowModal()
					elif self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1').find('.') != -1:
						dlg = wx.MessageDialog(None, 'Error name: \".\" not valid symbol\n No save notes!')
						dlg.ShowModal()
					else:	
						self.sas = self.path + self.goos + '/' + self.datnam + ':' + self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') + '.ox'
		except:
			pass
		try:
			if self.sas:
				self.x.SaveFile(self.sas)
				p = self.sas.split('/')[6]
				n = self.x.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')
				conf_db.dobdb(p, n)
		except AttributeError:
			self.stt.SetLabel("        " + _("Not number to save!"))
			self.stt.SetFont(self.fonts)
