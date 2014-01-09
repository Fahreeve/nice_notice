import wx
import pyvk
import os
import urllib
import CloseButton
import BackButton
import TextPanel
import ScrollMessagePanel
import TransparentText
import OnlineStatus


def save_photos(urls, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    #print urls
    names = urls[urls.rfind('/')+ 1:]
    filename = os.path.join(directory, names)
    #print "Downloading %s" % filename
    urllib.urlretrieve(urls, filename)
    return wx.Bitmap(filename, wx.BITMAP_TYPE_JPEG)
        

class MainFrame(wx.Frame):
    def __init__(self, parent, id, pos, title, first_name, last_name, online, messages=[]):
        wx.Frame.__init__(self, parent, id, title, pos, size=(325, 420), 
                        style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER |
                        wx.FRAME_NO_TASKBAR)
	
        self.first_name = first_name
        self.last_name = last_name
	self.online = online
        self.bmp = self.CreateBackground(325, 420)
        
        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        self.SetWindowShape()
        
	self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		
	mainsizer = wx.BoxSizer(wx.VERTICAL)
	
	mainsizer.AddSpacer((0, 11), 0, wx.EXPAND, 5)
	
	topsizer = wx.BoxSizer(wx.HORIZONTAL)
	
	self.backbutton = BackButton.BackButton(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(17, 16), wx.TAB_TRAVERSAL)
	topsizer.Add(self.backbutton, 0, wx.LEFT, 265)
	
	self.closebutton = CloseButton.CloseButton(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(17, 16), wx.TAB_TRAVERSAL)
	topsizer.Add(self.closebutton, 0, wx.LEFT, 10)
	
	mainsizer.Add(topsizer, 0, 0, 5)
	
	mainsizer.AddSpacer((0, 9), 0, 0, 5)
	
	self.scrollpanel = ScrollMessagePanel.ScrollMessagePanel(self, wx.ID_ANY, wx.Point(12, 35), wx.Size(300, 312), wx.TAB_TRAVERSAL)
	self.scrollpanel.SetMinSize(wx.Size(300, 312))
	mainsizer.Add(self.scrollpanel, 0, wx.LEFT, 12)
	
	#--Test-----------------------------------------------------------------
	self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 ", 1387711111)
	
	self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0", 1387711111)
	self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	#self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	#self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	#self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	#self.scrollpanel.AddMessages(messages)
	#self.scrollpanel.ErrorOn()
	#self.scrollpanel.ErrorOff()
	#self.online_status.SetOnline(False)
	#-----------------------------------------------------------------------
	
	mainsizer.AddSpacer((0, 3), 0, 0, 5)
	
	self.textpanel = TextPanel.TextPanel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, -1), wx.TAB_TRAVERSAL)
	mainsizer.Add(self.textpanel, 0, wx.LEFT, 12)
	
	self.SetSizer(mainsizer)
	self.Layout()
	
	self.Centre(wx.BOTH)  
	
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)    
	self.closebutton.Bind(wx.EVT_LEFT_UP, self.OnMinimize)
	self.backbutton.Bind(wx.EVT_LEFT_UP, self.OnBack)
    
    def SetWindowShape(self, evt=None):                  
        r = wx.RegionFromBitmap(self.bmp)                
        self.SetShape(r)
            
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)  
        
    #def OnClose(self, evt=None):
	#self.mytsk.Destroy()
        #self.Destroy()
	
    def OnMinimize(self, evt=None):
	self.Show(False)
	
    def OnBack(self, evt):
	#self.parent.OnClose()
	pass
        
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
        
        memdc.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD,face="Tahoma"))
        memdc.SetTextBackground(wx.Color(63, 63, 63))
        memdc.SetTextForeground(wx.Color(255, 255, 255))
	string = self.cutstr(self.first_name + " " + self.last_name, 28)
        memdc.DrawText(string, 16, 11)
	
	if self.online:
	    memdc.SetBrush(wx.Brush(wx.Color(179, 179,179)))
	    memdc.SetPen(wx.Pen(wx.Color(179, 179,179), 1, wx.SOLID))
	    memdc.DrawCircle(16 + (2 + len(string)) * 7, 20, 4)
        
        memdc.SelectObject(wx.NullBitmap) 
        image = bmp.ConvertToImage()
        image.SetMaskColour(0, 255, 0)
        image.SetMask(True)            
        bmp = wx.BitmapFromImage(image) 
        return bmp
    
    def AddMessage(self, photo, text, date, status=True):
	self.scrollpanel.AddMessage(self, photo, text, date, status)
	
    def cutstr(self, string, number):
	if len(string) > number:
	    return string[:number]
	else:
	    return string
	
    def NewDialog(self, first_name, last_name, online):
	self.first_name = first_name
	self.last_name = last_name
	self.online = online
	
	self.scrollpanel.ErrorOff()
	self.scrollpanel.DeleteAll()
	
	self.bmp = self.CreateBackground(325, 420)
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        self.SetWindowShape()	
	
       
     
if  __name__ ==  "__main__":  
    class MyApp(wx.App):
	def OnInit(self):
	    self.mainframe = MainFrame(None, -1, wx.Point(200, 200), 'vk_chat', "abcldmgtlrmlgmglmrgml", "abcmglrmhmkmhkdnhktnh", True)
	    self.mainframe.Show(True)  
	    self.SetTopWindow(self.mainframe)
	    #self.mainframe.NewDialog('1', '2', False)
	    return True
    
    app = MyApp(0)
    app.MainLoop()           
	    