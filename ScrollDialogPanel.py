# -*- coding: utf-8 -*-
import wx
import ScrollPanel
import DialogPanel


class ScrollDialogPanel(ScrollPanel.ScrollPanel):
    def __init__(self, parent, id, pos, size, style):
        ScrollPanel.ScrollPanel.__init__(self, parent, id, pos, size, style)
	self.scrolledpanel.SetBackgroundColour(wx.Color(237, 237, 237))
	self.error_message = (False, None)
	self.dialogs = dict()      
    
    def AddDialog(self, user_id, photo, title, friendphoto, text, date, status):
	dialog = DialogPanel.DialogPanel(self.scrolledpanel, photo, title, friendphoto, text, date, status)
	self.dialogs[user_id] = dialog 
	self.Add(dialog, 0, wx.BOTTOM, 1)
	
    def AddDialogs(sel, dialogs):
	#dialogs = [(user_id, photo, title, friendphoto, text, date, status)]
	dialog = []
	for dial in dialogs:
	    panel += [MessagePanel.MessagePanel(self.scrolledpanel, dial[0], dial[1], dial[2], dial[3], dial[4], dial[5])]
	    self.dialogs[user_id] = panel
	    dialog += [panel]
	self.Adds(dialog, 0, wx.BOTTOM, 5)
    
    def DeleteAll(self):
	self.scrollsizer.DeleteWindows()
	self.dialogs = dict()
	
    def DeleteDialogPanel(self, user_id):
	self.DeletePanel(self.dialogs[user_id])
	del self.dialogs[user_id]
	
    def GetDialogPanel(self, user_id):
	return self.dialogs[user_id]