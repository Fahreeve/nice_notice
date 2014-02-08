import wx


class ErrorMessage(wx.Panel):
    def __init__(self, parent, text):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(280, 39), wx.TAB_TRAVERSAL)
	self.text = text
	self.size = wx.Size(280, 39)
	
	self.background = self.CreateBackground()
	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.background, 0, 0)	
	
	self.Bind(wx.EVT_PAINT, self.OnPaint)        
	
    def OnPaint(self, evt):
	dc = wx.PaintDC(self)
	dc.DrawBitmap(self.background, 0, 0) 	
	
    def CreateBackground(self):
	bmp = wx.EmptyBitmap(self.size.x, self.size.y)
	memdc = wx.MemoryDC()
	memdc.SelectObject(bmp)
	
	memdc.SetBackground(wx.Brush(wx.Color(255, 239, 232)))
	memdc.Clear()

	memdc.SetPen(wx.Pen(wx.Color(232, 155, 136), 1, wx.SOLID))
	memdc.DrawLine(0, 0, self.size.x, 0)
	memdc.DrawLine(self.size.x - 1, 0, self.size.x -1, self.size.y - 1)
	memdc.DrawLine(self.size.x - 1, self.size.y - 1, 0, self.size.y - 1)
	memdc.DrawLine(0, self.size.y - 1, 0, 0)
	
	memdc.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma"))
	memdc.SetTextForeground(wx.Color(0, 0, 0))
	memdc.DrawText(self.text, 20, 10)	
	
	memdc.SelectObject(wx.NullBitmap)
	return bmp    