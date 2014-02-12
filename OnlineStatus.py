# -*- coding: utf-8 -*-
import wx


class OnlineStatus(wx.Panel):
    def __init__(self, parent, pos, online):
        wx.Panel.__init__(self, parent, wx.ID_ANY, pos, wx.Size(8, 8), wx.TAB_TRAVERSAL|wx.TRANSPARENT_WINDOW)
        self.online = online
	self.Bind(wx.EVT_PAINT, self.OnPaint) 
	self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnErase)
	
    def OnPaint(self, evt=None):
        pdc = wx.PaintDC(self)
        dc = wx.GCDC(pdc)
	dc.SetBackground(wx.Brush(wx.Color(63, 63, 63, 0)))
	dc.Clear()	
	if self.online:
	    dc.SetBrush(wx.Brush(wx.Color(179, 179,179)))
	    dc.SetPen(wx.Pen(wx.Color(179, 179,179), 1, wx.SOLID))
	    dc.DrawCircle(4, 4, 4)	  
	
    def SetOnline(self, online):
	self.online = online
	self.Refresh()
	
    def OnErase(self, evt):
	pass
    
if  __name__ ==  "__main__":  
    class MyApp(wx.App):
	def OnInit(self):
	    frame = wx.Frame(None, -1, "", wx.Point(200, 200), size=(40, 40), style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER |
                        wx.FRAME_NO_TASKBAR)
	    panel = OnlineStatus(frame, wx.Point(5, 5), True)
	    panel2 = OnlineStatus(frame, wx.Point(15, 5), False)
	    panel3 = OnlineStatus(frame, wx.Point(25, 5), False)
	    panel3.SetOnline(True)
	    frame.Show(True)
	    self.SetTopWindow(frame)
	    return True
    
    app = MyApp(0)
    app.MainLoop()  