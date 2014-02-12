# -*- coding: utf-8 -*-
import wx
from datetime import datetime
import TransparentText


class MessagePanel(wx.Panel):
    def __init__(self, parent, photo, text, date, status):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(290, -1), wx.TAB_TRAVERSAL)		
	self.SetStatus(status)
        
	sizer = wx.BoxSizer(wx.HORIZONTAL)
			
	self.avatar = wx.StaticBitmap(self, wx.ID_ANY, photo, wx.DefaultPosition, wx.DefaultSize, 0)
	sizer.Add(self.avatar, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 5)
	   
	self.message = wx.StaticText(self, wx.ID_ANY, text, wx.DefaultPosition, wx.Size(170, -1), 0)
	self.message.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	self.message.Wrap(170)
	sizer.Add(self.message, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 5)
	
	self.date = wx.StaticText(self, wx.ID_ANY, self.GetDate(date), wx.DefaultPosition, wx.Size(70, -1), 0)
	self.date.SetFont(wx.Font(8, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	self.date.SetForegroundColour(wx.Color(114, 114, 112))
	sizer.Add(self.date, 0, wx.TOP, 5)
	
	self.SetSizer(sizer)
	self.Layout()
    
    def GetDate(self, date):
	time = datetime.fromtimestamp(date)
	now = datetime.now()
	startday = datetime(now.year, now.month, now.day, hour=0, minute=0, second=0)
	endday = datetime(now.year, now.month, now.day, hour=23, minute=59, second=59)
	if startday <= time <= endday: #if a message sent today 
	    return "   " + time.strftime('%H:%M:%S') # return time
	else:
	    return time.strftime('%Y.%m.%d') #return date
	
    def SetStatus(self, status):
	if status:
	    self.SetBackgroundColour(wx.Color(255, 255, 255)) # read
	else:
	    self.SetBackgroundColour(wx.Color(237, 241, 245)) # unread	