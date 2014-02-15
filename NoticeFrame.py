import wx
import TransparentText
import CustomButton
import MainFrame


class NoticeFrame(MainFrame.MainFrame):
    def __init__(self, parent, id, pos, avatar, title, first_name, last_name, text):
	MainFrame.MainFrame.__init__(self, parent, id, pos, size=wx.Size(380, 100))
	self.first_name = first_name
        self.last_name = last_name
	self.title = title
	self.text = text
	
	mainsizer = wx.BoxSizer(wx.VERTICAL)
			
	titlesizer = wx.BoxSizer(wx.HORIZONTAL)
	
	titlesizer.AddSpacer((13, 0), 0, 0, 0)
	
	self.title = wx.StaticText( self, wx.ID_ANY, self.title, wx.DefaultPosition, wx.Size(335, -1), 0)
	self.title.Wrap(-1)
	self.title.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD, face="Tahoma"))
	self.title.SetForegroundColour(wx.Color(255, 255, 255))
	self.title.SetBackgroundColour(wx.Color(63, 63, 63))
	titlesizer.Add(self.title, 0, wx.TOP, 15)

	self.closebutton = CustomButton.CustomButton(self, wx.ID_ANY, wx.Bitmap("closebutton.png"), wx.DefaultPosition, wx.Size(17,16), wx.TAB_TRAVERSAL)
	titlesizer.Add(self.closebutton, 1, wx.TOP, 15)
	
	mainsizer.Add(titlesizer, 0, 0, 0)
	
	bodysizer = wx.BoxSizer(wx.HORIZONTAL)
	
	bodysizer.AddSpacer((12, 0), 0, 0, 0)
	
	self.avatar = wx.StaticBitmap(self, wx.ID_ANY, avatar, wx.DefaultPosition, wx.Size(50,50), 0)
	bodysizer.Add(self.avatar, 0, wx.TOP, 7)
	
	bodysizer.AddSpacer((7, 0), 0, 0, 0)
	
	textsizer = wx.BoxSizer(wx.VERTICAL)
	
	self.first_last_name = wx.StaticText(self, wx.ID_ANY, first_name + " " + last_name, wx.DefaultPosition, wx.DefaultSize, 0)
	self.first_last_name.Wrap(-1)
	self.first_last_name.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD, face="Tahoma"))
	self.first_last_name.SetForegroundColour(wx.Color(188, 222, 249))
	self.first_last_name.SetBackgroundColour(wx.Color(63, 63, 63))	
	textsizer.Add(self.first_last_name, 0, wx.TOP, 5)
	
	self.text = wx.StaticText(self, wx.ID_ANY, text, wx.DefaultPosition, wx.DefaultSize, 0)
	self.text.Wrap(-1)
	self.text.SetForegroundColour(wx.Color(255, 255, 255))
	self.text.SetBackgroundColour(wx.Color(63, 63, 63))		
	textsizer.Add(self.text, 0, wx.TOP, 5)
	
	bodysizer.Add(textsizer, 0, 0, 0)
	
	mainsizer.Add(bodysizer, 0, 0, 0)
	
	self.SetSizer(mainsizer)
	self.Layout()
	
	self.PlaySound()
	
	self.closebutton.Bind(wx.EVT_LEFT_UP, self.OnMinimize)	
	
    def OnMinimize(self, evt=None):
	self.Show(False)
    
    def PlaySound(self):
	self.sound = wx.Sound("new_message.wav")
	self.sound.Play(wx.SOUND_ASYNC)
 
 
if  __name__ ==  "__main__":
    class MyApp(wx.App):
	def OnInit(self):
	    frame = NoticeFrame(None, wx.ID_ANY,wx.Point(500, 500), wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "New Message", "Fahreev", "Eldar", "1 2 3 4 5 6 7 8 9 0 ")
	    frame.Show(True)
	    self.SetTopWindow(frame)
	    return True
    
    app = MyApp(0)
    app.MainLoop()    