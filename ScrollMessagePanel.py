import wx
import ScrollPanel
import MessagePanel
import ErrorMessage


class ScrollMessagePanel(ScrollPanel.ScrollPanel):
    def __init__(self, parent, id, pos, size, style):
        ScrollPanel.ScrollPanel.__init__(self, parent, id, pos, size, style)
	self.scrollbar.Bottom() 
	self.scrolledpanel.SetBackgroundColour(wx.Color(237, 237, 237))
	self.error_message = (False, None)
	self.messages = []       
    
    def AddMessage(self, photo, text, date, status):
	message = MessagePanel.MessagePanel(self.scrolledpanel, wx.DefaultPosition, photo, text, date, status)
	self.messages += [message] 
	self.Add(message, 0, wx.BOTTOM, 1)
	a = self.scrollsizer.GetSize().y - self.scrollsizer.GetMinSize().y
	self.scrolledpanel.ScrollWindow(0, a)
	self.scrollbar.Bottom()
	if a < 0:
	    self.virtualpositiony += a
	
    def AddMessages(sel, messages):
	#messages = [(photo, text, date, status)]
	panels = []
	for mess in messages:
	    message += [MessagePanel.MessagePanel(self.scrolledpanel, wx.DefaultPosition, mess[0], mess[1], mess[2], mess[3])]
	self.Adds(message, 0, wx.BOTTOM, 5)
	self.scrollbar.Bottom()
    
    def DeleteAll(self):
	self.scrollsizer.DeleteWindows()	