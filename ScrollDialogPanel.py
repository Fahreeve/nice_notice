import wx
import ScrollPanel
import DialogPanel


class ScrollDialogPanel(ScrollPanel.ScrollPanel):
    def __init__(self, parent, id, pos, size, style):
        ScrollPanel.ScrollPanel.__init__(self, parent, id, pos, size, style)
	self.scrolledpanel.SetBackgroundColour(wx.Color(237, 237, 237))
	self.error_message = (False, None)
	self.dialogs = []       
    
    def AddDialog(self, photo, title, friendphoto, text, date, status):
	dialog = DialogPanel.DialogPanel(self.scrolledpanel, photo, title, friendphoto, text, date, status)
	self.dialogs += [dialog] 
	self.Add(dialog, 0, wx.BOTTOM, 1)
	
    #def Adddialogs(sel, dialogs):
	##dialogs = [(photo, text, date, status)]
	#panels = []
	#for mess in dialogs:
	    #self.message += [MessagePanel.MessagePanel(self.scrolledpanel, wx.DefaultPosition, mess[0], mess[1], mess[2], mess[3])]
	#self.Adds(self.message, 0, wx.BOTTOM, 5)
	#self.scrollbar.Bottom()
    
    def DeleteAll(self):
	self.scrollsizer.DeleteWindows()
	self.dialogs = [] 