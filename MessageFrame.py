import wx
import CustomButton
import TextPanel
import ScrollMessagePanel
import OnlineStatus
import MainFrame


class MessageFrame(MainFrame.MainFrame):
    def __init__(self, parent, id, pos, title, online, messages=[]):
        MainFrame.MainFrame.__init__(self, parent, id, pos)
	
	self.title = title
	self.online = online

	mainsizer = wx.BoxSizer(wx.VERTICAL)
					
	mainsizer.AddSpacer(wx.Size(0, 11), 0, wx.EXPAND, 5)
	
	topsizer = wx.BoxSizer(wx.HORIZONTAL)
	
	self.constsizepanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(253, 16), wx.TAB_TRAVERSAL)
	self.constsizepanel.SetBackgroundColour(wx.Colour(63, 63, 63))
	self.constsizepanel.SetMinSize(wx.Size(253, 16))
	
	titlesizer = wx.BoxSizer(wx.HORIZONTAL)
	
	titlesizer.SetMinSize(wx.Size(253,16)) 
	self.title = wx.StaticText(self.constsizepanel, wx.ID_ANY, cutstr(title, 30), wx.DefaultPosition, wx.DefaultSize, 0)
	self.title.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD,face="Tahoma"))
	self.title.SetForegroundColour(wx.Colour(255, 255, 255))
	self.title.SetBackgroundColour(wx.Colour(63, 63, 63))
	
	titlesizer.Add(self.title, 0, wx.LEFT, 0)
	
	self.onlinestatus = OnlineStatus.OnlineStatus(self.constsizepanel, wx.DefaultPosition, online)
	titlesizer.Add(self.onlinestatus, 0, wx.TOP|wx.LEFT, 3)
	
	self.constsizepanel.SetSizer(titlesizer)
	self.constsizepanel.Layout()
	topsizer.Add(self.constsizepanel, 0, wx.LEFT, 12)
	
	self.backbutton = CustomButton.CustomButton(self, wx.ID_ANY, wx.Bitmap("backbutton.png"), wx.DefaultPosition, wx.Size(17, 16), wx.TAB_TRAVERSAL)
	topsizer.Add(self.backbutton, 0, wx.LEFT, 5)
	
	self.closebutton = CustomButton.CustomButton(self, wx.ID_ANY, wx.Bitmap("closebutton.png"), wx.DefaultPosition, wx.Size(17, 16), wx.TAB_TRAVERSAL)
	topsizer.Add(self.closebutton, 0, wx.LEFT, 8)
	
	mainsizer.Add(topsizer, 0, 0, 5)

	mainsizer.AddSpacer(wx.Size(0, 9), 0, 0, 5)
	
	self.scrollpanel = ScrollMessagePanel.ScrollMessagePanel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 312), wx.TAB_TRAVERSAL)
	self.scrollpanel.SetMinSize(wx.Size(300, 312))
	mainsizer.Add(self.scrollpanel, 0, wx.LEFT, 12)

	mainsizer.AddSpacer(wx.Size(0, 3), 0, 0, 5)
	
	self.textpanel = TextPanel.TextPanel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 45), wx.TAB_TRAVERSAL)
	mainsizer.Add(self.textpanel, 0, wx.LEFT, 12)

	self.SetSizer(mainsizer)
	self.Layout()
	
	self.closebutton.Bind(wx.EVT_LEFT_UP, self.OnMinimize)
	self.backbutton.Bind(wx.EVT_LEFT_UP, self.OnBack)  
	
    def OnMinimize(self, evt=None):
	self.Show(False)
	
    def OnBack(self, evt):
	#self.parent.OnClose()
	pass
    
    def AddMessage(self, photo, text, date, status=True):
	self.scrollpanel.AddMessage(photo, text, date, status)
	
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
	
def cutstr(string, number):
    if len(string) > number:
	return string[:number]
    else:
	return string
	
       
     
if  __name__ ==  "__main__":  
    class MyApp(wx.App):
	def OnInit(self):
	    self.mainframe = MessageFrame(None, -1, wx.Point(200, 200), "abcldmgtlrmlgmglmrgml abcmglrmhmkmhkdnhktnh", True)
	    #--Test-----------------------------------------------------------------
	    self.mainframe.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 ", 1387711111)
	    
	    self.mainframe.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0", 1387711111)
	    self.mainframe.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	    #self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	    #self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	    #self.scrollpanel.AddMessage(wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 7 8 9 0", 1387711111)
	    #self.scrollpanel.AddMessages(messages)
	    #self.scrollpanel.ErrorOn()
	    #self.scrollpanel.ErrorOff()
	    #self.online_status.SetOnline(False)
	    #-----------------------------------------------------------------------	    
	    self.mainframe.Show(True)  
	    self.SetTopWindow(self.mainframe)
	    #self.mainframe.NewDialog('1', '2', False)
	    return True
    
    app = MyApp(0)
    app.MainLoop()           
    