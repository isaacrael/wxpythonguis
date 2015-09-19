__author__ = 'grael_000'
"""
The following program can be used as a template for creating a python GUI for an application

"""

import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status_msg.....')

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome','name')

# Gets userName response

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()

# Gets answer to yes / no question

        yesNoBox = wx.MessageDialog(None, 'Start Python Quiz?', 'Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()



        if yesNoAnswer == wx.ID_NO:
            userName = "Loser!"

        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color',
                                             'Color Question',
                                             ['Green', 'Red', 'Blue', 'Yellow'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

# Sets up the positioning of the text ctrl panel

        wx.TextCtrl(panel, pos=(3,100), size=(150,50))

# Creates awesome text and sets foreground and background colors

        aweText = wx.StaticText(panel, -1, "Awesome Text", (3,3))
        aweText.SetForegroundColour('#67cddc')
        aweText.SetBackgroundColour('black')

# Creates customized awesome text and sets foreground and background colors

        rlyaweText = wx.StaticText(panel, -1, "Customized Awesomeness", (3,30))
        rlyaweText.SetForegroundColour(favColor)
        rlyaweText.SetBackgroundColour('black')


        self.SetTitle("Welcome " + (userName) + " ..... to Python Quiz")
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()