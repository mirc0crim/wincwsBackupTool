import datetime
import os
import shutil
import ui

locPath = "C:\\ProgramData\\BIZERBA\\WinCWS_SQL\\"
locs = ["Basis", "Orello", "Lyss"]
fName = "WINCWS.FDB"
netPath = "I:\\Bizerba Sicherungen\\WinCWS DB Backups\\"

netSave = False
locSave = False

def saveDB(i):
    netSave = startLoad(netPath)
    locSave = startLoad(locPath)
    copyTo(locPath + str(i) + locs[i-1] + "\\Database", fName, netPath + locs[i-1])

def startLoad(path):
    saves = False
    try:
        saves = sorted(os.listdir(path))
    except WindowsError:
        ui.addText(path + " nicht erreichbar")
        assert False
    return saves

def copyTo(fromPath, fName, toPath):
    currYear = str(datetime.datetime.now().year)
    currMonth = "0" + str(datetime.datetime.now().month)
    currDay = "0" + str(datetime.datetime.now().day)
    currDate = currYear + currMonth[:2] + currDay[:2]
    ui.addText("kopiere " + fName + " nach " + toPath)
    newName = fName[:-4] + " " + currDate + fName[-4:]
    shutil.copy(fromPath + "\\" + fName, toPath + "\\" + newName)

ui.create()
