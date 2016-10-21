#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:14:33 2016

@author: Prohodimec 
"""
import sys_inf
import wx, os, time
sys_inf.GetTxt()
# Напоминание в diarus.ini
class Soxr_Pan(wx.Panel):
	def __init__(self, parent, ID):
		wx.Panel.__init__(self, parent, -1, size=(450, 340))
		#self.SetBackgroundColour('#161627')
		wx.StaticText(self, -1,_("Create remember"),pos=(140, 4))
		self.day = wx.TextCtrl(self, pos=(6, 34), size=(50, 30))
		self.day.AppendText(time.strftime('%d'))
		wx.StaticText(self, -1,_("Days"),pos=(57, 34))
		self.mec = wx.TextCtrl(self, pos=(95, 34), size=(50, 30))
		self.mec.AppendText(time.strftime('%m'))
		wx.StaticText(self, -1,_("Month"),pos=(146, 34))
		self.god = wx.TextCtrl(self, pos=(189, 34), size=(50, 30))
		self.god.AppendText('16')
		wx.StaticText(self, -1,_("Year"),pos=(241, 34))
		self.chas = wx.TextCtrl(self, pos=(269, 34), size=(50, 30))
		self.chas.AppendText('00')
		wx.StaticText(self, -1,_("Hour"),pos=(322, 34))
		self.min = wx.TextCtrl(self, pos=(352, 34), size=(50, 30))
		self.min.AppendText('00')
		wx.StaticText(self, -1,_("Min"),pos=(404, 34))
		wx.StaticText(self, -1,_("Choice file"),pos=(177, 84))
		self.file = wx.TextCtrl(self, pos=(26, 110), size=(350, 30))
		self.file.AppendText('Not file')
		wx.StaticText(self, -1,_("Write command"),pos=(177, 155))
		self.comm = wx.TextCtrl(self, pos=(26, 185), size=(402, 30))
		self.comm.AppendText('Not command')
		wx.StaticText(self, -1,_("Choice melody"),pos=(177, 225))
		self.muz = wx.TextCtrl(self, pos=(26, 250), size=(350, 30))
		self.muz.AppendText('Not music')
		bue = wx.Button(self, -1, _("Exit"), size=(80,30), pos=(365, 300))
		bue.Bind(wx.EVT_BUTTON, self.Ex, bue)
		buf = wx.Button(self, -1, _("File"), size=(50,30), pos=(380, 110))
		buf.Bind(wx.EVT_BUTTON, self.Fil, buf)
		bum = wx.Button(self, -1, _("Mel"), size=(45,30), pos=(380, 250))
		bum.Bind(wx.EVT_BUTTON, self.Muz, bum)
		fin = wx.Button(self, -1, _("Save"), size=(80,30), pos=(6, 300))
		fin.Bind(wx.EVT_BUTTON, self.SoxR, fin)
		
	def Ex(self, event):
		fr.Destroy()
	
	def Fil(self, event):
		folders = sys_inf.DATA_PATH + 'Other'
		dlg = wx.FileDialog(self, "Choice file", folders, wildcard='*.ox', style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			if path:
				self.file.Clear()
				self.file.AppendText(path)    
		dlg.Destroy()
	
	def Muz(self, event):
		folderm = sys_inf.CONF_PATH + 'Music'
		dlg = wx.FileDialog(self, "Choice file", folderm, wildcard='*.mp3', style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			if path:
				self.muz.Clear()
				self.muz.AppendText(path)    
		dlg.Destroy()
		
	def SoxR(self, event):
		try:
			int(self.chas.GetValue())
			int(self.min.GetValue())
			int(self.day.GetValue())
			int(self.mec.GetValue())
			int(self.god.GetValue())
			god = '20' + str(self.god.GetValue())
			line = str(self.day.GetValue()) + '\:' + str(self.mec.GetValue()) + '\:' + god + '\:' + str(self.chas.GetValue()) + '\:' + str(self.min.GetValue()) + '\:' + '00' + '\;' + str(self.comm.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')) + '\;' + str(self.file.GetValue().encode('utf-8').decode('latin-1').encode('latin-1')) + '\;' + str(self.muz.GetValue().encode('utf-8').decode('latin-1').encode('latin-1'))		
			os.system('echo ' + line + ' >> ' + sys_inf.CONF_PATH + '.diarus.ini')
			fr.Destroy()
		except ValueError:
			lg = wx.MessageDialog(None, _("Error: not INT enter!"), 'A Message Box',wx.YES_NO | wx.ICON_QUESTION)
			retCode = lg.ShowModal()
			if (retCode == wx.ID_YES):
				fr.Destroy()

class Soxr_Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, _("Configuration Remember Upim"),size=(450, 340), style=(wx.MINIMIZE_BOX | wx.CLOSE_BOX))
		sq = sys_inf.ICON_PATH + 'np.png'
		self.SetIcon(wx.Icon(sq, wx.BITMAP_TYPE_PNG))
		Soxr_Pan(self, None)
app = wx.App()
fr = Soxr_Frame()
fr.Show()
app.MainLoop()
