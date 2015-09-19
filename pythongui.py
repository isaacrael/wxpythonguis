__author__ = 'grael_000'

import wx

"""

Written By: Gil Rael
The following program can be used as a template for creating the front end frame to a python GUI application

"""

class windowClass(wx.Frame):
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title=title, size=(1200,600) )
        self.Centre
        self.Show()

app = wx.App()
windowClass(None, title="Python Quiz")
app.MainLoop()



