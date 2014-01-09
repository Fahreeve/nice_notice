import wx

class ScrollBar(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.parent = parent
	self.scrollpanel = parent.scrolledpanel
	self.InitBuffer()
	#self.buffer = wx.EmptyBitmap(size.x, size.y)
	self.reglaget = self.DrawReglaget(size.x, size.y)
	self.posdown = wx.Point(0, 0)
	
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_PAINT, self.OnPaint)	
        
    #def OnLeftUp(self, evt):
	#self.scrollpanel.ScrollWindow(0, 10)
    def InitBuffer(self):
        self.buffer = wx.EmptyBitmap(self.GetSize().x, self.GetSize().y)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
        dc.Clear()    
		
    def OnLeftDown(self, event):
	self.posdown = event.GetPosition()
        self.CaptureMouse()
           
    def OnLeftUp(self, event):
        if self.HasCapture():
            self.ReleaseMouse()
                                                        
    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            self.DrawMotion(dc, event)
            
        event.Skip()
	
    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)  
	
    def DrawMotion(self, dc, event):
	posy = event.GetPosition().y
	print posy
	if posy - self.posdown.y > 0:
	    dc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
	    dc.Clear()
	    print "---", posy
	    dc.DrawBitmap(self.reglaget, 0, posy - self.posdown.y)   
		
    def DrawReglaget(self, x, y):
	bmp = wx.EmptyBitmap(x, y)
        memdc = wx.MemoryDC()
        memdc.SelectObject(bmp)
        memdc.SetBackground(wx.Brush(wx.Color(154, 154, 154)))
        memdc.Clear()
	memdc.SetPen(wx.Pen(wx.Color(255, 255, 255), 1, wx.SOLID))
        memdc.DrawPoint(0, 0) 	
	memdc.DrawPoint(1, 0)
	memdc.DrawPoint(2, 0)
	memdc.DrawPoint(0, 1)
	memdc.DrawPoint(7, 0)
	memdc.DrawPoint(8, 0)
	memdc.DrawPoint(9, 0)
	memdc.DrawPoint(9, 1)
	memdc.DrawPoint(0, y - 1) 	
	memdc.DrawPoint(1, y - 1)
	memdc.DrawPoint(2, y - 1)
	memdc.DrawPoint(0, y - 2)
	memdc.DrawPoint(7, y - 1)
	memdc.DrawPoint(8, y - 1)
	memdc.DrawPoint(9, y - 1)
	memdc.DrawPoint(9, y - 2)
	memdc.SelectObject(wx.NullBitmap) 
	return bmp