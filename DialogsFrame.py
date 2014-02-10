# -*- coding: utf-8 -*-
import wx
import MainFrame
import CustomButton
import ScrollDialogPanel
import DialogPanel


class DialogsFrame(MainFrame.MainFrame):
    def __init__(self, parent, id, pos, title):
        MainFrame.MainFrame.__init__(self, parent, id, pos)

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        mainsizer.AddSpacer(wx.Size(0, 11), 0, wx.EXPAND, 5)

        topsizer = wx.BoxSizer(wx.HORIZONTAL)

        self.title = wx.StaticText(self, wx.ID_ANY, title.decode('utf-8'), wx.DefaultPosition, wx.Size( 253,16 ), 0)
        self.title.Wrap(-1)
        self.title.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD,face="Tahoma"))
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))
        self.title.SetBackgroundColour(wx.Colour(63, 63, 63))

        topsizer.Add(self.title, 0, wx.LEFT, 12)

        self.forwardbutton = CustomButton.CustomButton(self, wx.ID_ANY, wx.Bitmap("forwardbutton.png"), wx.DefaultPosition, wx.Size(17, 16), wx.TAB_TRAVERSAL)
        topsizer.Add(self.forwardbutton, 0, wx.LEFT, 5)

        self.closebutton = CustomButton.CustomButton(self, wx.ID_ANY, wx.Bitmap("closebutton.png"), wx.DefaultPosition, wx.Size(17, 16), wx.TAB_TRAVERSAL)
        topsizer.Add(self.closebutton, 0, wx.LEFT, 8)

        mainsizer.Add(topsizer, 0, 0, 5)

        mainsizer.AddSpacer(wx.Size(0, 9), 0, 0, 5)

        self.scrollpanel = ScrollDialogPanel.ScrollDialogPanel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 370), wx.TAB_TRAVERSAL)
        self.scrollpanel.SetMinSize(wx.Size(300, 370))
        mainsizer.Add(self.scrollpanel, 0, wx.LEFT, 12)

        #mainsizer.AddSpacer(wx.Size( 0, 3), 0, 0, 5)

        self.SetSizer(mainsizer)
        self.Layout()
        
        self.closebutton.Bind(wx.EVT_LEFT_UP, self.OnMinimize)
	self.forwardbutton.Bind(wx.EVT_LEFT_UP, self.OnForward) 
	
    def OnMinimize(self, evt=None):
	self.Show(False)
	
    def OnForward(self, evt):
	pass	
    
    def AddDialog(self, user_id, photo, title, friendphoto, text, date, status):
	self.scrollpanel.AddDialog(user_id, photo, title, friendphoto, text, date, status)
	
    def AddDialogs(self, dialogs):
	#dialogs = [(user_id, photo, title, friendphoto, text, date, status)]
	self.scrollpanel.AddDialogs(dialogs)


if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            self.mainframe = DialogsFrame(None, -1, wx.Point(200, 200), "Диалоги")
	    self.mainframe.AddDialog(0, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, False)
	    self.mainframe.AddDialog(1, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, False)
	    self.mainframe.AddDialog(2, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, True)
	    self.mainframe.AddDialog(3, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, True)
	    self.mainframe.AddDialog(4, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, False)
	    self.mainframe.AddDialog(5, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, False)
	    self.mainframe.AddDialog(6, wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), "Hello world!", wx.Bitmap("C:\\Projects\\vk_messenger\\2G3ZSYjqBWw.jpg"), u"1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", 1387711111, False)
	    self.mainframe.Show(True)
            self.SetTopWindow(self.mainframe)
            return True

    app = MyApp(0)
    app.MainLoop()