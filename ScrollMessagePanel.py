import wx
import ScrollPanel
import MessagePanel
import ErrorMessage


class ScrollMessagePanel(ScrollPanel.ScrollPanel):
    def __init__(self, parent, id, pos, size, style):
        ScrollPanel.ScrollPanel.__init__(self, parent, id, pos, size, style)
	self.scrolledpanel.SetBackgroundColour(wx.Color(237, 237, 237))
	self.error_message = (False, None)
	self.messages = []       
    
    def AddMessage(self, photo, text, date, status=True):
	message = MessagePanel.MessagePanel(self.scrolledpanel, wx.DefaultPosition, photo, text, date, status)
	self.messages += [message] 
	a = self.scrollsizer.GetMinSize()
	self.Add(message, 0, wx.BOTTOM, 1)
	self.scrolledpanel.ScrollWindow(0, self.scrollsizer.GetSize().y - self.scrollsizer.GetMinSize().y)	
	
    def AddMessages(sel, messages):
	#[(photo, text, date, status)]
	panels = []
	for mess in messages:
	    self.message += [MessagePanel.MessagePanel(self.scrolledpanel, wx.DefaultPosition, mess[0], mess[1], mess[2], mess[3])]
	self.Adds(self.message, 0, wx.BOTTOM, 5)
    
    def DeleteAll(self):
	self.scrollsizer.DeleteWindows()	