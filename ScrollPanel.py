import wx
import ScrollBar


class ScrollPanel(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
	#self.size = size
	self.virtualsize = wx.Size(size.x, 0)
	self.pos = pos
	self.parent = parent	
	
	mainsizer = wx.BoxSizer(wx.HORIZONTAL)
		
	self.scrolledpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(290, 312), wx.TAB_TRAVERSAL)
	self.scrolledpanel.SetBackgroundColour(wx.Color(255, 255, 255))
	self.scrollsizer = wx.BoxSizer(wx.VERTICAL)
	self.scrolledpanel.SetSizer(self.scrollsizer)
	self.scrollsizer.FitInside(self.scrolledpanel)
	mainsizer.Add(self.scrolledpanel, 1, wx.EXPAND | wx.ALL, 0)
	
	self.scrollbar = ScrollBar.ScrollBar(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(10, 312), wx.TAB_TRAVERSAL)
	mainsizer.Add(self.scrollbar, 0, wx.EXPAND, 0)	
	
	self.SetSizer(mainsizer)
	self.Layout()
	self.bmp = self.CreateBacground()
	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.bmp, 0, 0, True)
	self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        
    def CreateBacground(self):
	size = self.GetSize()
        bmp = wx.EmptyBitmap(size.x, size.y)
        memdc = wx.MemoryDC()
        memdc.SelectObject(bmp)
        memdc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
        memdc.Clear()
	
	memdc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	memdc.DrawPoint(0, 0)
	memdc.DrawPoint(size.x - 1, size.y - 1)
	memdc.DrawPoint(size.x - 1, 0)
	memdc.DrawPoint(0, size.y - 1)
        return bmp
    
    def Add(self, panel, proportion, flag, border):
	a = self.scrollsizer.GetMinSize()
	self.scrollsizer.Add(panel, proportion, flag, border)
	self.scrolledpanel.Layout()
	self.virtualsize = self.scrollsizer.GetMinSize()

    def Adds(self, panels, proportion, flag, border):
	for panel in panels:
	    self.scrollsizer.Add(panel, proportion, flag, border)
	self.virtualsize = self.scrollsizer.GetMinSize()
	self.scrollsizer.Layout()
	
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)
	
    def ErrorOn(self, text="Error"):
	if not self.error_message[0]:
	    #pass
	    #self.currentposition -= 44
	    #for mess in self.message:
		#self.currentposition -= mess.size.y
		#mess.SetPosition(wx.Point(0, self.currentposition))
	    #self.currentposition = self.size.y	
	    self.error_message = (True, ErrorMessage.ErrorMessage(self, wx.DefaultPosition))	
	
    def ErrorOff(self):
	if self.error_message[0]:
	    #pass
	    #self.error_message[1].Destroy()
	    #for mess in self.message:
		#self.currentposition -= mess.size.y 
		#mess.SetPosition(wx.Point(0, self.currentposition))
	    #self.currentposition = self.size.y	
	    self.error_message = (False, None)	    