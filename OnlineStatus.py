import wx


class OnlineStatus(wx.Panel):
    def __init__(self, parent, pos, online):
        wx.Panel.__init__(self, parent, wx.ID_ANY, pos, wx.Size(8, 8), wx.TAB_TRAVERSAL)
        self.online = online
	self.size = wx.Size(8, 8)
        self.pos = pos
	self.parent = parent
	self.bmp = self.CreateBackground()
	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.bmp, 0, 0, True)
	self.Bind(wx.EVT_PAINT, self.OnPaint)  
	
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)   
	
    def SetOnline(self, online):
	self.online = online
	self.bmp = self.CreateBackground()
	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.bmp, 0, 0, True)	
	
    def CreateBackground(self):
	bmp = wx.EmptyBitmap(self.size.x, self.size.y)
	memdc = wx.MemoryDC()
	memdc.SelectObject(bmp)	
	
	memdc.SetBackground(wx.Brush(wx.Color(63, 63, 63)))
	memdc.Clear()	
	if self.online:
	    memdc.SetBrush(wx.Brush(wx.Color(179, 179,179)))
	    memdc.SetPen(wx.Pen(wx.Color(179, 179,179), 1, wx.SOLID))
	    memdc.DrawCircle(4, 4, 4)
	
	memdc.SelectObject(wx.NullBitmap)  
        return bmp	
    
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