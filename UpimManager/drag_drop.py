#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:14:33 2016

@author: Prohodimec 
"""
from wx import MessageDialog
from wx import FileDropTarget
# примерный класс...
class FileDrop(FileDropTarget):
	def __init__(self, window):
		FileDropTarget.__init__(self)
		self.window = window
	def OnDropFiles(self, x, y, filenames):
		for name in filenames:
			try:
				file = open(name, 'r')
				text = file.read()
				self.window.WriteText(text)
				file.close()
			except IOError, error:
				dlg = MessageDialog(None, 'Error open file\n' + str(error))
				dlg.ShowModal()
			except UnicodeDecodeError, error:
				dlg = MessageDialog(None, 'Non ascii file\n' + str(error))
				dlg.ShowModal()