import datetime
import os
import time
import wx
import memo

class MyFrame(wx.Frame):

    logger = None
    l = ["Basis Sichern", "Orello Sichern", "Lyss Sichern", "Basis Wiederherstellen", "Orello Wiederherstellen", "Lyss Wiederherstellen"]
    
    def __init__(self, t):
        wx.Frame.__init__(self, None, title=t, size=(1000,400))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        panel = wx.Panel(self)

        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # 3 Buttons for saving
        self.saveButton1 =wx.Button(panel, size=(150,30), label=MyFrame.l[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick1, self.saveButton1)
        grid.Add(self.saveButton1, pos=(1,0))
        self.saveButton2 =wx.Button(panel, size=(150,30), label=MyFrame.l[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.saveButton2)
        grid.Add(self.saveButton2, pos=(1,1))
        self.saveButton3 =wx.Button(panel, size=(150,30), label=MyFrame.l[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick3, self.saveButton3)
        grid.Add(self.saveButton3, pos=(1,2))
        # 3 comboboxes for choosing
        saveFiles1 = sorted(os.listdir(memo.netPath + "Basis\\"))
        self.files1 = wx.ComboBox(panel, size=(150, -1), choices=saveFiles1, style=wx.CB_DROPDOWN)
        self.files1.SetValue(saveFiles1[0])
        grid.Add(self.files1, pos=(5,0))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox1, self.files1)
        saveFiles2 = sorted(os.listdir(memo.netPath + "Orello\\"))
        self.files2 = wx.ComboBox(panel, size=(150, -1), choices=saveFiles2, style=wx.CB_DROPDOWN)
        self.files2.SetValue(saveFiles2[0])
        grid.Add(self.files2, pos=(5,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox2, self.files2)
        saveFiles3 = sorted(os.listdir(memo.netPath + "Lyss\\"))
        self.files3 = wx.ComboBox(panel, size=(150, -1), choices=saveFiles3, style=wx.CB_DROPDOWN)
        self.files3.SetValue(saveFiles3[0])
        grid.Add(self.files3, pos=(5,2))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox3, self.files3)
        # 3 Buttons for recovering
        self.recoverButton1 =wx.Button(panel, size=(150,30), label=MyFrame.l[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick4, self.recoverButton1)
        grid.Add(self.recoverButton1, pos=(6,0))
        self.recoverButton2 =wx.Button(panel, size=(150,30), label=MyFrame.l[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick5, self.recoverButton2)
        grid.Add(self.recoverButton2, pos=(6,1))
        self.recoverButton3 =wx.Button(panel, size=(150,30), label=MyFrame.l[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick6, self.recoverButton3)
        grid.Add(self.recoverButton3, pos=(6,2))

        # A multiline TextCtrl
        MyFrame.logger = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(MyFrame.logger, 1, wx.EXPAND)
        panel.SetSizerAndFit(hSizer)

    def OnClick1(self,event):
        self.clicked(memo.saveDB, 1, MyFrame.l[0])
    def OnClick2(self,event):
        self.clicked(memo.saveDB, 2, MyFrame.l[1])
    def OnClick3(self,event):
        self.clicked(memo.saveDB, 3, MyFrame.l[2])
    def OnClick4(self,event):
        self.clicked(memo.recoverDB, 1, MyFrame.l[3])
    def OnClick5(self,event):
        self.clicked(memo.recoverDB, 2, MyFrame.l[4])
    def OnClick6(self,event):
        self.clicked(memo.recoverDB, 3, MyFrame.l[5])
    def EvtComboBox1(self, event):
        MyFrame.logger.AppendText("Wiederherstellungsdatei Basis: \n")
        memo.recName = event.GetString()
        MyFrame.logger.AppendText(event.GetString() + " \n")
    def EvtComboBox2(self, event):
        MyFrame.logger.AppendText("Wiederherstellungsdatei Orello: \n")
        memo.recName = event.GetString()
        MyFrame.logger.AppendText(event.GetString() + " \n")
    def EvtComboBox3(self, event):
        MyFrame.logger.AppendText("Wiederherstellungsdatei Lyss: \n")
        memo.recName = event.GetString()
        MyFrame.logger.AppendText(event.GetString() + " \n")
    def OnClose(self, event):
        loggerValue = MyFrame.logger.GetValue()
        if len(loggerValue) > 1:
            now = datetime.datetime.now()
            dateString = "%d%02d%02d" % (now.year, now.month, now.day)
            dateString += "%02d%02d%02d" % (now.hour, now.minute, now.second)
            f = open("D:\\WinCWS Backup Tool\\log\\" + dateString + ".txt", "w+")
            f.write(MyFrame.logger.GetValue())
            f.close()
        self.Destroy()
    def clicked(self, f, i, s):
        MyFrame.logger.AppendText(s + "\n")
        start = time.time()
        f(i)
        totalTime = round((time.time() - start)*10)/10
        MyFrame.logger.AppendText("Fertig in " + str(totalTime) + " Sekunden\n")

def addText(s):
    MyFrame.logger.AppendText(s + "\n")

def create():
    app = wx.App(False)
    top = MyFrame("WinCWS Backup Tool")
    favicon = wx.Icon("C:\Python27\DLLs\py.ico", wx.BITMAP_TYPE_ICO, 16, 16)
    top.SetIcon(favicon)
    top.Show()
    app.MainLoop()
