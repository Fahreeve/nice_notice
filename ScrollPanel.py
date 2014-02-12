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
		
	self.scrolledpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(size.x - 11, size.y), wx.TAB_TRAVERSAL)
	self.scrolledpanel.SetBackgroundColour(wx.Color(255, 255, 255))
	self.scrollsizer = wx.BoxSizer(wx.VERTICAL)
	self.scrolledpanel.SetSizer(self.scrollsizer)
	self.scrollsizer.FitInside(self.scrolledpanel)
	mainsizer.Add(self.scrolledpanel, 1, wx.EXPAND | wx.LEFT, 1)
	
	self.scrollbar = ScrollBar.ScrollBar(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(10, size.y), wx.TAB_TRAVERSAL)
	mainsizer.Add(self.scrollbar, 0, wx.EXPAND, 0)	
	
	self.SetSizer(mainsizer)
	self.Layout()
	self.Bind(wx.EVT_PAINT, self.OnPaint)
    
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
	dc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	size = self.GetSize()
	# рисуется левая верхняя и левая нижняя точки, остальные две рисуются в скроллбаре
	dc.DrawPoint(0, 0)
	dc.DrawPoint(0, size.y - 1)    
    
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
	
    def Scroll(self, y):
	self.virtualpositiony += y
	self.scrolledpanel.ScrollWindow(0, y)
    
    def ScrollMaxUp(self):
	self.scrolledpanel.ScrollWindow(0, - self.virtualpositiony)
	self.virtualpositiony = 0
	    
    
    def ScrollMaxDown(self):
	# self.virtualpositiony должно быть меньше 0, т.к смещаемся вниз
	if self.virtualpositiony > - self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y:  
	    self.scrolledpanel.ScrollWindow(0, - self.virtualpositiony - self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y) # смещаемся на разность текущенго смещения вниз и максимального смещения вниз
	    self.virtualpositiony = - self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y # панель находится в самом низу 
	    
    def DeletePanel(self, panel):
	self.scrollsizer.Remove(panel)
	self.scrollsizer.Layout()