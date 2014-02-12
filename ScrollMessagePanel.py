# -*- coding: utf-8 -*-
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
	self.messages = dict()       
    
    def AddMessage(self, id, photo, text, date, status):
	message = MessagePanel.MessagePanel(self.scrolledpanel, photo, text, date, status)
	self.messages[id] = message # доавляю панель в словарь 
	self.Add(message, 0, wx.BOTTOM, 1)
	if -self.virtualpositiony <= self.scrollsizer.GetSize().y: 
	    # если размер смещения меньше, чем размер окна
	    if -self.virtualpositiony + message.GetSize().y + 1 > self.scrollsizer.GetSize().y \
	       or self.scrollsizer.GetMinSize().y > self.scrollsizer.GetSize().y: 
		# если после добавления элемента размер окна
		# меньше размера смещения или вирутальный размер окна больше реального,
		# то проскролисть вниз на разность смещения и размера окна
		self.virtualpositiony = -self.scrollsizer.GetMinSize().y + self.scrollsizer.GetSize().y
		self.scrolledpanel.ScrollWindow(0, self.virtualpositiony)
	else: 
	    # если больше, то смещаем на размер только что добавленной панели и 
	    #плюс 1 пиксель для горизонтальной линии разделения
	    delta = self.scrollsizer.GetMinSize().y - self.scrollsizer.GetSize().y
	    self.scrolledpanel.ScrollWindow(0, -delta)
	    self.virtualpositiony -= delta  
	self.scrollbar.Bottom()
	
    def AddMessages(sel, messages):
	#messages = [(id, photo, text, date, status)]
	# функция недописана, self.virtualpositiony должно изменяться!
	message = []
	for mess in messages:
	    panel = MessagePanel.MessagePanel(self.scrolledpanel, mess[0], mess[1], mess[2], mess[3])
	    self.messages[id] = panel
	    message += [panel]
	self.Adds(message, 0, wx.BOTTOM, 5)
	self.scrollbar.Bottom()
    
    def DeleteAll(self):
	self.scrollsizer.DeleteWindows()
	self.messages = dict()
	
    def DeleteMessagePanel(self, id):
	self.DeletePanel(self.messages[id])
	del self.messages[id]
	
    def GetMessagePanel(self, id):
	return self.messages[id]