# -*- coding: utf-8 -*-
import wx


class ScrollBar(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.parent = parent
	self.k = 1 # отношение размера прокручиваемой области к размеру полосы проркутки
	self.sizereglaget = wx.Size(size.x, int(size.y / self.k)) # размер каретки
	self.posreglaget = wx.Point(0, 0) # текущая позиция каретки
	self.reglaget = self.DrawReglaget(self.sizereglaget) # картинка каретки 
	self.posdown = wx.Point(0, 0) # координата точки нажатия
	self.deltay = 0 # расстояние между точкой нажатия и левым верхним углом каретки
	self.InitBuffer()
	
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_PAINT, self.OnPaint)	
	
    def Resize(self, size):
	if size.y == 0:
	    self.k = 1
	else:
	    self.k = float(size.y) / self.GetSize().y
	if self.k <= 1:
	    self.sizereglaget = self.GetSize() 
	else:
	    self.sizereglaget = wx.Size(size.x, int(self.GetSize().y / self.k))
	self.reglaget = self.DrawReglaget(self.sizereglaget)
	self.InitBuffer()
	
    def InitBuffer(self):
        self.buffer = wx.EmptyBitmap(self.GetSize().x, self.GetSize().y)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
        dc.Clear()  
	dc.DrawBitmap(self.reglaget, self.posreglaget.x, self.posreglaget.y)
	# рисуются правая верхняя и правая нижняя точки, остальные рисуются в scrollpanel.py
	dc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	size = self.GetSize()
	dc.DrawPoint(size.x - 1, size.y - 1)
	dc.DrawPoint(size.x - 1, 0)	
	
    def OnLeftDown(self, event):
	self.posdown = event.GetPosition()
	if self.posreglaget.y < self.posdown.y < self.posreglaget.y + self.sizereglaget.y:
	    self.deltay = self.posdown.y - self.posreglaget.y
	    self.CaptureMouse()       
           
    def OnLeftUp(self, event):
        if self.HasCapture():
            self.ReleaseMouse()
                                                        
    def OnMotion(self, event):
	# так как отношение K - нецелое число, то если много двигать ползунок скролящаяся панель в исходное состояние не вернется в исходное положение. Поэтому я создал функции ScrollMaxUp и ScrollMaxDown, которые принудительно будут возвращать панель в исходное состояние
	posy = event.GetPosition().y - self.deltay
	dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
	if event.Dragging() and event.LeftIsDown():
	    if 0 < posy < self.GetSize().y - self.sizereglaget.y:
		self.DrawMotion(dc, posy)
		self.parent.Scroll(int((-posy + self.posreglaget.y) * self.k))
		self.posreglaget.y = posy
	    elif 0 >= posy:
		self.DrawMotion(dc, 0)
		self.parent.ScrollMaxUp() 
		self.posreglaget.y = 0
	    elif posy >= self.GetSize().y - self.sizereglaget.y:
		self.DrawMotion(dc, self.GetSize().y - self.sizereglaget.y)
		self.parent.ScrollMaxDown()
		self.posreglaget.y = self.GetSize().y - self.sizereglaget.y
        event.Skip()
	
    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)  	
	
    def DrawMotion(self, dc, posy):
	dc.SetBackground(wx.Brush(wx.Color(255, 255, 255)))
	dc.Clear()
	dc.DrawBitmap(self.reglaget, 0, posy)
	dc.SetPen(wx.Pen(wx.Color(63, 63, 63), 1, wx.SOLID))
	size = self.GetSize()
	dc.DrawPoint(size.x - 1, size.y - 1)
	dc.DrawPoint(size.x - 1, 0)	
	
    def Bottom(self):
	self.posreglaget.y = self.GetSize().y - self.sizereglaget.y
	self.InitBuffer()
		
    def DrawReglaget(self, size):
	x = size.x
	y = size.y
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
    
    
if  __name__ ==  "__main__":  
    class TestFrame(wx.Frame):
	def __init__(self, parent):
	    wx.Frame.__init__(self, parent, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 412), wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
	    
	    self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
	    
	    bSizer1 = wx.BoxSizer(wx.VERTICAL)
	    
	    self.scrollbar = ScrollBar(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(10, 312), wx.TAB_TRAVERSAL)
	    self.scrollbar.Resize(wx.Size(10, 700))
	    self.scrollbar.Bottom()
	    bSizer1.Add(self.scrollbar, 0, wx.EXPAND, 0)	
	    
	    self.SetSizer(bSizer1)
	    self.Layout()
	    
	    self.Centre(wx.BOTH)    
	    
	def ScrollMaxUp(self):
	    pass
	
	def ScrollMaxDown(self):
	    pass
	
	def Scroll(self, y):
	    pass
		    
    
    class MyApp(wx.App):
	def OnInit(self):
	    self.testframe = TestFrame(None)    
	    self.testframe.Show(True)  
	    self.SetTopWindow(self.testframe)
	    return True
    
    app = MyApp(0)
    app.MainLoop()           
    