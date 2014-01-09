# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import time



###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		#bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button25 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.Point(0, 0), wx.DefaultSize, 0 )
		#bSizer4.Add( self.m_button25, 0, 0, 5 )
		
		
		#self.m_button25.Hide()
		
		
		#self.m_panel3.SetSizer( bSizer4 )
		#self.m_panel3.Layout()
		#bSizer4.Fit( self.m_panel3 )
		bSizer3.Add( self.m_panel3, 1, wx.EXPAND, 5 )
		
		
		#self.SetSizer( bSizer3 )
		#self.Layout()
		
		self.Centre( wx.BOTH )
		
		for i in range(30):
			self.m_button25.SetPosition(wx.Point(i, 30))
			time.sleep(0.1)
	


class MyApp(wx.App):
    def OnInit(self):
	frame = MyFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()
