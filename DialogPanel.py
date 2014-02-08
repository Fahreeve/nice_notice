# -*- coding: utf-8 -*-
import wx
from datetime import datetime


class DialogPanel(wx.Panel):
    def __init__(self, parent, photo, title, friendphoto, text, date, status):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(290, -1), wx.TAB_TRAVERSAL)		
	self.SetStatus(status)

	sizer = wx.BoxSizer(wx.HORIZONTAL)
			
	self.avatar = wx.StaticBitmap(self, wx.ID_ANY, photo, wx.DefaultPosition, wx.DefaultSize, 0)
	sizer.Add(self.avatar, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 5)	
	
	sizer2 = wx.BoxSizer(wx.VERTICAL)
	
	sizer6 = wx.BoxSizer(wx.HORIZONTAL)
	
	self.title = wx.StaticText(self, wx.ID_ANY, cutstr(title, 22), wx.DefaultPosition, wx.Size(170, -1), 0)
	self.title.Wrap(-1)
	self.title.SetFont(wx.Font(11, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	#sizer2.Add(self.title, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 5)
	sizer6.Add(self.title, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 5)
	
	self.date = wx.StaticText(self, wx.ID_ANY, self.GetDate(date), wx.DefaultPosition, wx.Size(70, -1), 0)
	self.date.SetFont(wx.Font(8, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	self.date.SetForegroundColour(wx.Color(114, 114, 112))
	sizer6.Add(self.date, 0, wx.TOP, 5)	
	
	sizer2.Add(sizer6, 1, wx.EXPAND, 0)
	   
	sizer4 = wx.BoxSizer(wx.HORIZONTAL)
	
	if friendphoto != None:
	    self.friendphoto = wx.StaticBitmap( self, wx.ID_ANY, friendphoto, wx.DefaultPosition, wx.Size(25, 25), 0)
	    sizer4.Add(self.friendphoto, 0, wx.LEFT | wx.BOTTOM, 5)	
	
	self.textpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
	sizer5 = wx.BoxSizer(wx.VERTICAL)
	
	self.text = wx.StaticText(self.textpanel, wx.ID_ANY, cutstr(text, 43), wx.DefaultPosition, wx.DefaultSize, 0)
	self.text.Wrap(-1)
	#self.text.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	self.text.SetForegroundColour(wx.Color(104, 104, 102))
	sizer5.Add(self.text, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 5)
	
	
	self.textpanel.SetSizer(sizer5)
	self.textpanel.Layout()
	sizer4.Add(self.textpanel, 1, wx.ALL, 0)	

	sizer2.Add(sizer4, 1, wx.EXPAND, 0)
		
	sizer.Add(sizer2, 1, wx.EXPAND, 0)	
	
	#self.date = wx.StaticText(self, wx.ID_ANY, self.GetDate(date), wx.DefaultPosition, wx.Size(70, -1), 0)
	#self.date.SetFont(wx.Font(8, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	#self.date.SetForegroundColour(wx.Color(114, 114, 112))
	#sizer.Add(self.date, 0, wx.TOP, 5)
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
	#if status == 0: # если полхователь не прочитал последнее сообщение
	    #self.SetBackgroundColour(wx.Color(237, 241, 245))
	#elif status == 1: # если друг не прочитал последнее сообщение
	    #self.textpanel.SetBackgroundColour(wx.Color(237, 241, 245))
	#else: # если последнее сообщение прочитано
	    #self.SetBackgroundColour(wx.Color(255, 255, 255))
	    
def cutstr(string, number):
    if len(string) > number:
	return string[:number]
    else:
	return string
	    
if  __name__ ==  "__main__":  
    class TestFrame(wx.Frame):
	def __init__(self, parent):
	    wx.Frame.__init__(self, parent, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(310, 212), wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
	    
	    self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
	    
	    bSizer1 = wx.BoxSizer(wx.VERTICAL)
	    
	    self.dialog = DialogPanel(self, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, False)
	    bSizer1.Add(self.dialog, 0, wx.EXPAND, 0)	
	    
	    self.SetSizer(bSizer1)
	    self.Layout()
	    
	    self.Centre(wx.BOTH)    
		    
    
    class MyApp(wx.App):
	def OnInit(self):
	    self.testframe = TestFrame(None)    
	    self.testframe.Show(True)  
	    self.SetTopWindow(self.testframe)
	    return True
    
    app = MyApp(0)
    app.MainLoop()           
    