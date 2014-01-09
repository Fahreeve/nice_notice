import wx
import TransparentText
import CloseButton


class NoticeFrame(wx.Frame):
    def __init__(self, parent, id, pos, avatar, title, first_name, last_name, text):
        wx.Frame.__init__(self, parent, id, "title", pos, size=(380, 120), 
                            style=wx.FRAME_SHAPED | wx.SIMPLE_BORDER |
                            wx.FRAME_NO_TASKBAR)  
	self.first_name = first_name
        self.last_name = last_name
	self.title = title
	self.text = text
	self.avatar = wx.StaticBitmap(self, wx.ID_ANY, avatar, wx.Point(13, 43), wx.DefaultSize, 0)
	self.size = self.GetSize()
	
	n = len(first_name) + len(last_name)
	
	self.closebutton = CloseButton.CloseButton(self, wx.ID_ANY, wx.Point(345, 17), wx.Size(17, 16), wx.TAB_TRAVERSAL)	
	
	self.text = TransparentText.TransparentText(self, wx.ID_ANY, self.EditText(text, n), wx.Point(76, 45), wx.Size(290, -1))
	self.text.Wrap(230)
	self.text.SetForegroundColour(wx.Color(255, 255, 255))
	number_lines = len(self.text.GetLabel().split("\n"))
	if 10 + 16 * number_lines > 100:
	    self.size = wx.Size(380, 55 + 16 * number_lines)
	    self.text.SetSize(wx.Size(290, 10 + 16 * number_lines))
	    self.SetSize(self.size)
	else:
	    self.size = wx.Size(380, 120)
	    
	self.bmp = self.CreateBackground(self.size.x, self.size.y) 
	#print self.text.GetSize(), self.GetSize(), 16 * number_lines 
	#self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
	#dc = wx.ClientDC(self)
	#dc.DrawBitmap(self.bmp, 0, 0, True)	
	
	self.SetWindowShape()
	
	self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
	self.closebutton.Bind(wx.EVT_LEFT_UP, self.OnMinimize)
    
    def SetWindowShape(self, evt=None):                  
        r = wx.RegionFromBitmap(self.bmp)                
        self.SetShape(r)	
	
    def OnMinimize(self, evt=None):
	self.Show(False)
    
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
        memdc.DrawPoint(size_x - 2, 0)
        memdc.DrawPoint(size_x - 3, 0)
        memdc.DrawPoint(size_x - 4, 0)
        memdc.DrawPoint(size_x - 2, 1)
        memdc.DrawPoint(size_x - 3, 1)
        memdc.DrawPoint(size_x - 2, 2)
        memdc.DrawPoint(size_x - 2, size_y - 4)
        memdc.DrawPoint(size_x - 2, size_y - 3)
        memdc.DrawPoint(size_x - 3, size_y - 3)
        memdc.DrawPoint(size_x - 2, size_y - 2)
        memdc.DrawPoint(size_x - 3, size_y - 2)
        memdc.DrawPoint(size_x - 4, size_y - 2)
        memdc.DrawPoint(0, size_y - 4)
        memdc.DrawPoint(0, size_y - 3)
        memdc.DrawPoint(1, size_y - 3)
        memdc.DrawPoint(0, size_y - 2)
        memdc.DrawPoint(1, size_y - 2)
        memdc.DrawPoint(2, size_y - 2)
        
        memdc.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD,face="Tahoma"))
	memdc.SetTextForeground(wx.Color(188, 222, 249))
	memdc.DrawText(self.first_name + " " + self.last_name, 75, 45)
	
	memdc.SetTextForeground(wx.Color(255, 255, 255))
	memdc.DrawText(self.title, 13, 17)	
	
        memdc.SelectObject(wx.NullBitmap) 
        image = bmp.ConvertToImage()
        image.SetMaskColour(0, 255, 0)
        image.SetMask(True)            
        bmp = wx.BitmapFromImage(image) 
        return bmp    
    
    def EditText(self, text, n):
	return " " * int(1.85 * n) + text
 
 
if  __name__ ==  "__main__":
    class MyApp(wx.App):
	def OnInit(self):
	    frame = NoticeFrame(None, wx.ID_ANY,wx.Point(500, 500), wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "New Message", "Fahreev", "Eldar", "1 2 3 4 5 6 7 8 9 0 ")
	    frame.Show(True)
	    self.SetTopWindow(frame)
	    return True
    
    app = MyApp(0)
    app.MainLoop()    