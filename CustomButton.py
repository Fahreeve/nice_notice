import wx


class CustomButton(wx.Panel):
    def __init__(self, parent, id, bmp, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.size = size
        self.pos = pos
	self.parent = parent
	self.bmp = bmp
	dc = wx.ClientDC(self)
	dc.DrawBitmap(bmp, 0, 0)
	self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)    