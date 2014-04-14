import memo
import datetime
import time
import wx

class MyFrame(wx.Frame):

    logger = None
    l = ["Basis Sichern", "Lyss Sichern", "Orello Sichern"]
    
    def __init__(self, t):
        wx.Frame.__init__(self, None, title=t, size=(800,400))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        panel = wx.Panel(self)

        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # 3 Buttons
        self.button1 =wx.Button(panel, size=(150,30), label=MyFrame.l[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick1, self.button1)
        grid.Add(self.button1, pos=(6,0))
        self.button2 =wx.Button(panel, size=(150,30), label=MyFrame.l[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.button2)
        grid.Add(self.button2, pos=(7,0))
        self.button3 =wx.Button(panel, size=(150,30), label=MyFrame.l[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick3, self.button3)
        grid.Add(self.button3, pos=(8,0))

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
