# -*- coding: utf-8 -*-
import wx
        

class MainFrame(wx.Frame):
    def __init__(self, parent, id, pos):
	size = wx.Size(324, 423)
        wx.Frame.__init__(self, parent, id, "", pos, size, 
                        style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER |
                        wx.FRAME_NO_TASKBAR)
	
        self.bmp = self.CreateBackground(size.x, size.y)
        
        self.SetClientSize(size)
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        self.SetWindowShape()  
	
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)    
    
    def SetWindowShape(self, evt=None):                  
        r = wx.RegionFromBitmap(self.bmp)                
        self.SetShape(r)
            
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)  
        
    def CreateBackground(self, size_x, size_y):
        bmp = wx.EmptyBitmap(size_x, size_y)
        memdc = wx.MemoryDC()
        memdc.SelectObject(bmp)
        memdc.SetBackground(wx.Brush(wx.Color(63, 63, 63)))
        memdc.Clear()
        memdc.SetPen(wx.Pen(wx.Color(0,255,0), 1, wx.SOLID))
        memdc.DrawPoint(0, 0) 
        memdc.DrawPoint(0, 1)
        memdc.DrawPoint(0, 2)
        memdc.DrawPoint(1, 0)
        memdc.DrawPoint(1, 1)
        memdc.DrawPoint(2, 0)
        memdc.DrawPoint(size_x - 1, 0)
        memdc.DrawPoint(size_x - 2, 0)
        memdc.DrawPoint(size_x - 3, 0)
        memdc.DrawPoint(size_x - 1, 1)
        memdc.DrawPoint(size_x - 2, 1)
        memdc.DrawPoint(size_x - 1, 2)
        memdc.DrawPoint(size_x - 1, size_y - 3)
        memdc.DrawPoint(size_x - 1, size_y - 2)
        memdc.DrawPoint(size_x - 2, size_y - 2)
        memdc.DrawPoint(size_x - 1, size_y - 1)
        memdc.DrawPoint(size_x - 2, size_y - 1)
        memdc.DrawPoint(size_x - 3, size_y - 1)
        memdc.DrawPoint(0, size_y - 3)
        memdc.DrawPoint(0, size_y - 2)
        memdc.DrawPoint(1, size_y - 2)
        memdc.DrawPoint(0, size_y - 1)
        memdc.DrawPoint(1, size_y - 1)
        memdc.DrawPoint(2, size_y - 1)
	
        memdc.SelectObject(wx.NullBitmap) 
        image = bmp.ConvertToImage()
        image.SetMaskColour(0, 255, 0)
        image.SetMask(True)            
        bmp = wx.BitmapFromImage(image) 
        return bmp


if  __name__ ==  "__main__":  
    class MyApp(wx.App):
	def OnInit(self):
	    self.mainframe = MainFrame(None, -1, wx.Point(200, 200))
	    self.mainframe.Show(True)  
	    self.SetTopWindow(self.mainframe)
	    return True
    
    app = MyApp(0)
    app.MainLoop()	    