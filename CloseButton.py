import wx


class CloseButton(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.size = size
        self.pos = pos
	self.parent = parent
	self.bmp = self.CreateBacground()
	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.bmp, 0, 0, True)
	self.Bind(wx.EVT_PAINT, self.OnPaint)       
        
    def CreateBacground(self):
        bmp = wx.EmptyBitmap(self.size.x, self.size.y)
        memdc = wx.MemoryDC()
        memdc.SelectObject(bmp)
        memdc.SetBackground(wx.Brush(wx.Color(20, 20, 20)))
        memdc.Clear()
	
	memdc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	memdc.DrawPoint(0, 0)
	memdc.DrawPoint(self.size.x - 1, self.size.y - 1)
	memdc.DrawPoint(self.size.x - 1, 0)
	memdc.DrawPoint(0, self.size.y - 1)
	
        memdc.SetPen(wx.Pen(wx.Color(120, 120, 120), 2, wx.SOLID))
        memdc.DrawLine(4, 4, 12, 12) 
        memdc.DrawLine(4, 12, 12, 4)
        memdc.SelectObject(wx.NullBitmap)
        return bmp

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)