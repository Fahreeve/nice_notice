# -*- coding: utf-8 -*-
import wx
import ScrollBar
import ErrorMessage


class ScrollPanel(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
	self.virtualsize = wx.Size(size.x, 0) # размер скролящейся области
	self.virtualpositiony = 0 # смещение скролящихся данных отнсительно 
				#начального положения. если больше нуля, то сместилось вверх
	self.pos = pos
	self.parent = parent	
	
	mainsizer = wx.BoxSizer(wx.HORIZONTAL)
		
	self.scrolledpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(size.x - 10, size.y), wx.TAB_TRAVERSAL)
	self.scrolledpanel.SetBackgroundColour(wx.Color(255, 255, 255))
	self.scrollsizer = wx.BoxSizer(wx.VERTICAL)
	self.scrolledpanel.SetSizer(self.scrollsizer)
	self.scrollsizer.FitInside(self.scrolledpanel)
	mainsizer.Add(self.scrolledpanel, 1, wx.EXPAND | wx.ALL, 0)
	
	self.scrollbar = ScrollBar.ScrollBar(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(10, size.y), wx.TAB_TRAVERSAL)
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
	self.scrollsizer.Add(panel, proportion, flag, border)
	self.scrolledpanel.Layout()
	self.virtualsize = self.scrollsizer.GetMinSize()
	self.scrollbar.Resize(self.virtualsize)

    def Adds(self, panels, proportion, flag, border):
	for panel in panels:
	    self.scrollsizer.Add(panel, proportion, flag, border)
	self.virtualsize = self.scrollsizer.GetMinSize()
	self.scrollsizer.Layout()
	self.scrollbar.Resize(self.virtualsize)
	
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)
	
    def Scroll(self, y):
	self.virtualpositiony += y
	self.scrolledpanel.ScrollWindow(0, y)
    
    def ScrollMaxUp(self):
	self.scrolledpanel.ScrollWindow(0, -self.virtualpositiony)
	self.virtualpositiony = 0
    
    def ScrollMaxDown(self):
	# self.virtualpositiony должно быть меньше 0, т.к смещаемся вниз
	if self.virtualpositiony > - self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y:  
	    self.scrolledpanel.ScrollWindow(0, - self.virtualpositiony - self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y) # смещаемся на разность текущенго смещения вниз и максимального смещения вниз
	    self.virtualpositiony = - self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y # панель находится в самом низу
	
    #def ErrorOn(self, text="Error"):
	#if not self.error_message[0]:
	    ##pass
	    ##self.currentposition -= 44
	    ##for mess in self.message:
		##self.currentposition -= mess.size.y
		##mess.SetPosition(wx.Point(0, self.currentposition))
	    ##self.currentposition = self.size.y	
	    #error = ErrorMessage.ErrorMessage(self, text)
	    #self.error_message = (True, error)	
	    #self.scrollsizer.Add(panel, proportion, flag, border)
	    #self.scrolledpanel.Layout()
	    #self.virtualsize = self.scrollsizer.GetMinSize()
	    #self.scrollbar.Resize(self.virtualsize)
	
    #def ErrorOff(self):
	#if self.error_message[0]:
	    ##pass
	    ##self.error_message[1].Destroy()
	    ##for mess in self.message:
		##self.currentposition -= mess.size.y 
		##mess.SetPosition(wx.Point(0, self.currentposition))
	    ##self.currentposition = self.size.y	
	    #self.error_message = (False, None)	    