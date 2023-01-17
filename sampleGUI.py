import requests    
import json
import sys
import pyodbc
import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.Centre()
        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu()
        viewItem   = wx.Menu()


#       Build a menu entry - text only
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit sample ...')
#        ID_HOST = wx.NewId()
        viewHostItem  = fileButton.Append(wx.ID_ANY, 'Host', 'Retrieve Host ...')
        captureItem  = fileButton.Append(wx.ID_ANY, 'Capture', 'Start Capture Mode ...')
        monitorItem  = fileButton.Append(wx.ID_ANY, 'Monitor', 'Start Monitor Mode ...')

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.Bind(wx.EVT_MENU, self.ViewHost, viewHostItem)
        self.Bind(wx.EVT_MENU, self.CaptureMode, captureItem)
        self.Bind(wx.EVT_MENU, self.MonitorMode, monitorItem)

        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('Waiting To Start')

        self.SetTitle('SAMPLE - My Application ')
        self.Show(True)

    def Quit(self, e):
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to Quit?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_YES:
            self.Close()

    def ViewHost(self, e):
        self.Close()

    def CaptureMode(self, e):
        self.statusbar.SetStatusText('Data Capture Mode')

        self.statusbar.SetStatusText('Exit Capture Mode')


    def MonitorMode(self,e):
        self.statusbar.SetStatusText('Data Monitor Mode')

        self.statusbar.SetStatusText('Exit Monitor Mode')


def main():
    app = wx.App()
    windowClass(None, 0, size=(500,400))

    app.MainLoop()

main()

