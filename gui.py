# -*- coding: UTF-8 -*-
import wx
import MainFrame
import NoticeFrame

#self.myvk = pyvk.pyvk("login", "password", "2951857", "messages") "4089578"
  
#self.userdata = self.myvk.get(self.myvk.user_id, ["uid", "first_name", "last_name","online", "photo"]) #comment if you dont have internet!

#self.mytsk = MyTaskBarIcon(self)
    
    
class MyApp(wx.App):
    def OnInit(self):
        self.mainframe = MainFrame.MainFrame(None, -1, wx.Point(200, 200), 'vk_chat', "Fahreev", "Eldar", True)
	#frame = NoticeFrame.NoticeFrame(None, -1, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "vk_chat", "Fahreev", "Eldar", "hello!")
        self.mainframe.Show(True)
        self.SetTopWindow(self.mainframe)
        return True

app = MyApp(0)
app.MainLoop()