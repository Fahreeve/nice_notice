import wx


class MyTaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)

        self.frame = frame
        self.SetIcon(wx.Icon('taskicon.ico', wx.BITMAP_TYPE_ICO))
	self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=2)

    def CreatePopupMenu(self):
        menu = wx.Menu()
	menu.Append(1, 'Show')
        menu.Append(2, 'Close')
        return menu

    def OnTaskBarClose(self, event): #close the programs
        self.frame.OnClose()

    def OnTaskBarActivate(self, event):
        if not self.frame.IsShown():
            self.frame.Show()

    def OnTaskBarDeactivate(self, event):
        if self.frame.IsShown():
            self.frame.Hide()