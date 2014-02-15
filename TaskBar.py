# -*- coding: utf-8 -*-
import wx


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item


class TaskBar(wx.TaskBarIcon):
    def __init__(self, friend):
	wx.TaskBarIcon.__init__(self)
	self.friend = friend
	self.icon = wx.IconFromBitmap(wx.Bitmap('taskicon.ico'))#wx.Icon('taskicon.ico')
	self.unreadicon = wx.IconFromBitmap(wx.Bitmap('taskiconunread.ico'))#wx.Icon('taskiconunread.ico')
        self.SetIcon(self.icon, u'Нет новых сообщений')
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnLeftDown)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        #create_menu_item(menu, 'Say Hello', self.on_hello) пример кода
        #menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.OnExit)
        return menu        

    def OnLeftDown(self, event):
	self.friend.ShowFrame()
	self.UpdateIcon(1)

    def OnExit(self, event):
        wx.CallAfter(self.Destroy)
	
    def UpdateIcon(self, unread_message=0):
	if unread_message == 0:
	    self.SetIcon(self.icon, u'Нет новых сообщений')
	else:
	    self.SetIcon(self.unreadicon, unicode(unread_message) + u' сообщени' + endword(unread_message))
	    
def endword(number):
    end = number % 10
    if end == 1 and end % 100 != 11:
	return u"е"
    elif end == 2 or end == 3 or end == 4:
	return u"я"
    else:
	return u"й"
    

if __name__ == '__main__':
    class MyApp(wx.App):
	def OnInit(self):
	    self.taskbar = TaskBar(self)
	    #self.taskbar.UpdateIcon(1)
	    return True
	
	def ShowFrame(self):
	    pass
    
    app = MyApp(0)
    app.MainLoop()      