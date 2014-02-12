# -*- coding: utf-8 -*-
import wx
from datetime import datetime

class TextPanel(wx.Panel):
    def __init__(self, parent, id, avatar, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.pos = pos
	self.parent = parent
	bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
		
	self.avatar = wx.StaticBitmap( self, wx.ID_ANY, avatar, wx.DefaultPosition, wx.DefaultSize, 0)
	bSizer3.Add(self.avatar, 0, wx.ALL, 5)
	
	self.textctrl = wx.TextCtrl(self, wx.ID_ANY, size=wx.Size(235, -1), style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_RICH2|wx.BORDER_NONE)
	font = wx.Font(10, wx.MODERN, wx.NORMAL,wx.FONTWEIGHT_NORMAL, face="Tahoma")
	self.textctrl.SetFont(font)	
	
	bSizer3.Add(self.textctrl, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5)
	
	self.SetSizer(bSizer3)
	self.Layout()
	
	self.SetBackgroundColour(wx.Color(255, 255, 255))
	self.Bind(wx.EVT_PAINT, self.OnPaint)
	self.textctrl.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
	dc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	size = self.GetSize()
	dc.DrawPoint(0, 0)
	dc.DrawPoint(size.x - 1, size.y - 1)
	dc.DrawPoint(size.x - 1, 0)
	dc.DrawPoint(0, size.y - 1)
	
    def OnEnter(self, evt):
	text = self.textctrl.GetValue() # получаю введенный текст
	self.textctrl.Clear() # стираю весь введенный текст
	now = (datetime.now() - datetime(year=1970, month=1, day=1)).total_seconds()
	self.parent.AddMyMessage(self.parent.myavatar, text, int(now))
	
    
if  __name__ ==  "__main__":  
    class TestFrame(wx.Frame):
	def __init__(self, parent):
	    wx.Frame.__init__(self, parent, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(412, 100), wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
	    
	    self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
	    bSizer1 = wx.BoxSizer(wx.VERTICAL)
	    
	    self.textpanel = TextPanel(self, wx.ID_ANY, wx.Bitmap( u"C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size(300, 45), wx.TAB_TRAVERSAL)    
	    bSizer1.Add(self.textpanel, 0, wx.EXPAND, 0)	
	    
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
    