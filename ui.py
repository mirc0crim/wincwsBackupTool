# -*- coding: cp1252 -*-
import datetime
import os
import time
import wx
import memo

class MyFrame(wx.Frame):

    logger = None
    l = ["Basis Sichern", "Orello Sichern", "Lyss Sichern", "Basis Wiederherstellen", "Orello Wiederherstellen", "Lyss Wiederherstellen", "Basis entfernen", "Orello entfernen", "Lyss entfernen", "Layout sichern"]
    
    def __init__(self, t):
        wx.Frame.__init__(self, None, title=t, size=(1000,400))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        panel = wx.Panel(self)

        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.wincwstext1 = wx.StaticText(panel, label="WinCWS sichern")
        grid.Add(self.wincwstext1, pos=(0,0))
        # 3 Buttons for saving
        self.saveButton1 =wx.Button(panel, size=(130,30), label=MyFrame.l[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick1, self.saveButton1)
        grid.Add(self.saveButton1, pos=(1,0))
        self.saveButton2 =wx.Button(panel, size=(130,30), label=MyFrame.l[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.saveButton2)
        grid.Add(self.saveButton2, pos=(1,1))
        self.saveButton3 =wx.Button(panel, size=(130,30), label=MyFrame.l[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick3, self.saveButton3)
        grid.Add(self.saveButton3, pos=(1,2))

        self.wincwstext2 = wx.StaticText(panel, label="WinCWS-Sicherung wiederherstellen oder entfernen")
        grid.Add(self.wincwstext2, pos=(3,0), span=(1,2))
        # 3 comboboxes for choosing
        saveFiles1 = sorted(os.listdir(memo.netPath + "Basis\\"))
        self.files1 = wx.ComboBox(panel, size=(130,30), choices=saveFiles1, style=wx.CB_DROPDOWN)
        grid.Add(self.files1, pos=(4,0))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox1, self.files1)
        saveFiles2 = sorted(os.listdir(memo.netPath + "Orello\\"))
        self.files2 = wx.ComboBox(panel, size=(130,30), choices=saveFiles2, style=wx.CB_DROPDOWN)
        grid.Add(self.files2, pos=(5,0))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox2, self.files2)
        saveFiles3 = sorted(os.listdir(memo.netPath + "Lyss\\"))
        self.files3 = wx.ComboBox(panel, size=(130,30), choices=saveFiles3, style=wx.CB_DROPDOWN)
        grid.Add(self.files3, pos=(6,0))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox3, self.files3)
        # 3 Buttons for recovering
        self.recoverButton1 =wx.Button(panel, size=(130,30), label=MyFrame.l[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick4, self.recoverButton1)
        grid.Add(self.recoverButton1, pos=(4,1))
        self.recoverButton2 =wx.Button(panel, size=(130,30), label=MyFrame.l[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick5, self.recoverButton2)
        grid.Add(self.recoverButton2, pos=(5,1))
        self.recoverButton3 =wx.Button(panel, size=(130,30), label=MyFrame.l[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick6, self.recoverButton3)
        grid.Add(self.recoverButton3, pos=(6,1))
        # 3 Buttons for deleting
        self.delButton1 =wx.Button(panel, size=(130,30), label=MyFrame.l[6])
        self.Bind(wx.EVT_BUTTON, self.OnClick7, self.delButton1)
        grid.Add(self.delButton1, pos=(4,2))
        self.delButton2 =wx.Button(panel, size=(130,30), label=MyFrame.l[7])
        self.Bind(wx.EVT_BUTTON, self.OnClick8, self.delButton2)
        grid.Add(self.delButton2, pos=(5,2))
        self.delButton3 =wx.Button(panel, size=(130,30), label=MyFrame.l[8])
        self.Bind(wx.EVT_BUTTON, self.OnClick9, self.delButton3)
        grid.Add(self.delButton3, pos=(6,2))

        self.bldtext = wx.StaticText(panel, label="Label Designer sichern")
        grid.Add(self.bldtext, pos=(8,0))
        
        # Button for Layouts
        self.layoutButton =wx.Button(panel, size=(130,30), label=MyFrame.l[9])
        self.Bind(wx.EVT_BUTTON, self.OnClick10, self.layoutButton)
        grid.Add(self.layoutButton, pos=(9,0))

        # A multiline TextCtrl
        MyFrame.logger = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(MyFrame.logger, 1, wx.EXPAND)
        panel.SetSizerAndFit(hSizer)

    def OnClick1(self,event):
        MyFrame.logger.AppendText("Bitte 20s warten.\n")
        self.clicked(memo.saveDB, 1, MyFrame.l[0])
    def OnClick2(self,event):
        MyFrame.logger.AppendText("Bitte 15s warten.\n")
        self.clicked(memo.saveDB, 2, MyFrame.l[1])
    def OnClick3(self,event):
        MyFrame.logger.AppendText("Bitte 15s warten.\n")
        self.clicked(memo.saveDB, 3, MyFrame.l[2])
    def OnClick4(self,event):
        self.clicked(memo.recoverDB, 1, MyFrame.l[3])
    def OnClick5(self,event):
        self.clicked(memo.recoverDB, 2, MyFrame.l[4])
    def OnClick6(self,event):
        self.clicked(memo.recoverDB, 3, MyFrame.l[5])
    def OnClick7(self,event):
        memo.recName = self.files1.GetValue()
        self.clicked(memo.delDB, 1, MyFrame.l[6])
        self.files1.Clear()
        self.files1.AppendItems(sorted(os.listdir(memo.netPath + "Basis\\")))
    def OnClick8(self,event):
        memo.recName = self.files2.GetValue()
        self.clicked(memo.delDB, 2, MyFrame.l[7])
        self.files2.Clear()
        self.files2.AppendItems(sorted(os.listdir(memo.netPath + "Orello\\")))
    def OnClick9(self,event):
        memo.recName = self.files3.GetValue()
        self.clicked(memo.delDB, 3, MyFrame.l[8])
        self.files3.Clear()
        self.files3.AppendItems(sorted(os.listdir(memo.netPath + "Lyss\\")))
    def OnClick10(self,event):
        MyFrame.logger.AppendText("Bitte 7s warten.\n")
        self.clicked(memo.layout, -1, MyFrame.l[9])
    def EvtComboBox1(self, event):
        MyFrame.logger.AppendText("Sicherungsdatei Basis: \n")
        memo.recName = event.GetString()
        MyFrame.logger.AppendText(event.GetString() + " \n")
    def EvtComboBox2(self, event):
        MyFrame.logger.AppendText("Sicherungsdatei Orello: \n")
        memo.recName = event.GetString()
        MyFrame.logger.AppendText(event.GetString() + " \n")
    def EvtComboBox3(self, event):
        MyFrame.logger.AppendText("Sicherungsdatei Lyss: \n")
        memo.recName = event.GetString()
        MyFrame.logger.AppendText(event.GetString() + " \n")
    def OnClose(self, event):
        loggerValue = MyFrame.logger.GetValue()
        if len(loggerValue) > 1:
            now = datetime.datetime.now()
            dateString = "%d%02d%02d" % (now.year, now.month, now.day)
            dateString += "%02d%02d%02d" % (now.hour, now.minute, now.second)
            f = open("D:\\WinCWS Backup Tool\\log\\" + dateString + ".txt", "w")
            f.write(MyFrame.logger.GetValue())
            f.close()
        self.Destroy()
    def clicked(self, f, i, s):
        MyFrame.logger.AppendText(s + "\n")
        start = time.time()
        f(i)
        totalTime = round((time.time() - start)*10)/10
        MyFrame.logger.AppendText("Fertig in " + str(totalTime) + " Sekunden\n\n")

def addText(s):
    MyFrame.logger.AppendText(s + "\n")

def create():
    app = wx.App(False)
    top = MyFrame("Bizerba Backup Tool")
    favicon = wx.Icon("C:\Python27\DLLs\py.ico", wx.BITMAP_TYPE_ICO, 16, 16)
    top.SetIcon(favicon)
    top.Show()
    app.MainLoop()
