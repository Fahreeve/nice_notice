import wx
import TextCtrl

class TextPanel(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.size = size
        self.pos = pos
	self.parent = parent
	#self.bmp = save_photos(self.parent.userdata[0]["photo"], "C:\\Projects\\vk_messenger")
    	#TextCtrl
	bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
	self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
	bSizer3.Add( self.m_bitmap1, 0, wx.ALL, 3 )
	
	self.m_panel8 = TextCtrl.TextCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	bSizer3.Add( self.m_panel8, 1, wx.EXPAND, 5 )
	
	
	self.SetSizer( bSizer3 )
	self.Layout()	
	self.bmp = self.CreateBacground()
	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.bmp, 0, 0, True)
	self.Bind(wx.EVT_PAINT, self.OnPaint)
	self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        
        
    def CreateBacground(self):
        bmp = wx.EmptyBitmap(self.size.x, self.size.y)
        memdc = wx.MemoryDC()
        memdc.SelectObject(bmp)
        memdc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
        memdc.Clear()
	
	memdc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	memdc.DrawPoint(0, 0)
	memdc.DrawPoint(self.size.x - 1, self.size.y - 1)
	memdc.DrawPoint(self.size.x - 1, 0)
	memdc.DrawPoint(0, self.size.y - 1)
	
	#memdc.DrawBitmap(self.bmp, 4, 4, True)
        return bmp

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)
	
    def OnLeftUp(self, evt):
	#self.parent.OnClose()
	pass