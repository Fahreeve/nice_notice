import wx


class TextCtrl(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
	self.size = self.GetSize()
	self.acground = self.CreateBacground()
	#self.bmp = self.bacground
	dc = wx.ClientDC(self)
	#dc.DrawBitmap(self.bmp, 0, 0, True)
	self.Bind(wx.EVT_PAINT, self.OnPaint)
	#self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
	self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
	
    def OnKeyDown(self, evt):
	char = evt.GetUniChar()
	print unicode(chr(char))
        
        
    def GetChar(number, language, shift=False):
	if language == "eng":
	    return unicode(chr(char))
        
    def CreateBacground(self):
        bmp = wx.EmptyBitmap(self.size.x, self.size.y)
        memdc = wx.MemoryDC()
        memdc.SelectObject(bmp)
        memdc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
        memdc.Clear()
        return bmp  