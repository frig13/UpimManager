#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx, os, time
import  wx.calendar
import sys_inf
sys_inf.GetTxt()

class Soxr(wx.Panel):
	def __init__(self, parent, ID, x):
		self.x = x
		wx.Panel.__init__(self, parent, -1, size=(280, wx.EXPAND))
		self.SetBackgroundColour('black')
		self.fonts = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Sans')
		cal = wx.calendar.CalendarCtrl(self, -1, wx.DateTime_Now(), pos = (0, 0), size=(280, 210), style=wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SEQUENTIAL_MONTH_SELECTION)
		cal.SetHeaderColours('blue', '#A49565')
		cal.SetHighlightColours('black', 'cyan')
		cal.SetFont(self.fonts)
		cal.SetBackgroundColour('black')
		self.cal = cal
		self.Bind(wx.calendar.EVT_CALENDAR, self.OnCalSelected, id=cal.GetId())
		self.basicText = wx.TextCtrl(self, -1, _("Two click to number and write name"), size=(270, 30), pos=(5,220))
		patch = sys_inf.DATA_PATH + 'Data/'
		self.list = []
		for i in os.listdir(patch):
			self.z = patch + i
			if os.path.isfile(self.z):
				pass
			else:
				self.list.append(self.z.split('/')[5])
		
		buttons = wx.Button(self, 2, _("Save"), size=(120,30), pos=(5, 290))
		buttons.SetForegroundColour('lightgray')
		buttons.Bind(wx.EVT_BUTTON, self.Sav, id=2)
		bu = wx.Button(self, 2, _("Exit"), size=(120,30), pos=(154, 290))
		bu.SetForegroundColour('lightgray')
		bu.Bind(wx.EVT_BUTTON, self.Ex, id=2)

	def OnCalSelected(self, event):
		ll = event.GetDate()
		self.goos = str(ll).split(' ')[3] + ':' + str(ll).split(' ')[2]
		self.opps = str(ll).split(' ')[1] + ':' + str(ll).split(' ')[2] + _(':[+ choice name]')
		self.datnam = str(ll).split(' ')[1] + ':' + str(ll).split(' ')[2]
		stt = wx.TextCtrl(self, -1, self.opps, size=(270, 30), pos=(5, 250))
		stt.SetFont(self.fonts)
	
	def Ex(self, event):
		self.Destroy()

				
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
				sas = self.path + self.goos + '/' + self.datnam + ':' + 'no name' + '.ox'	
				
			else:
				if self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1').find('_') != -1:
					self.DiaTire()
				elif self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1').find('.') != -1:
					self.DiaToch()	
				else:
					sas = self.path + self.goos + '/' + self.datnam + ':' + self.basicText.GetValue().encode('utf-8').decode('latin-1').encode('latin-1') + '.ox'
		except:
			dlg = wx.MessageDialog(None, _("Not number to save!"))
			dlg.ShowModal()
		self.x.SaveFile(sas)
		self.Destroy()
	
	def DiaTire(self):
		dlg = wx.MessageDialog(None, 'Error name: \"_\" not valid symbol\n No save notes!')
		dlg.ShowModal()
		
	def DiaToch(self):
		dlg = wx.MessageDialog(None, 'Error name: \".\" not valid symbol\n No save notes!')
		dlg.ShowModal()