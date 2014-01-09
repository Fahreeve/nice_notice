import wx

class TransparentText(wx.StaticText):
  def __init__(self, parent, id, label, pos, size):
    wx.StaticText.__init__(self, parent, id, label, pos, size, wx.TRANSPARENT_WINDOW)
    self.font = wx.Font(10, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_NORMAL, face="Tahoma")
   # self.font_color = self.GetForegroundColour() 

    self.Bind(wx.EVT_PAINT, self.on_paint)
    self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
    self.Bind(wx.EVT_SIZE, self.on_size)

  def on_paint(self, event=None):
    bdc = wx.PaintDC(self)
    dc = wx.GCDC(bdc)

    font_face = self.GetFont()
    font_color = self.GetForegroundColour()

    dc.SetFont(self.font)
    dc.SetTextForeground(font_color)
    dc.DrawText(self.GetLabel(), 0, 0)

  def on_size(self, event):
    self.Refresh()
    event.Skip()