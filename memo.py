import datetime
import os
import shutil
import subprocess
import ui

locPath = "C:\\ProgramData\\BIZERBA\\WinCWS_SQL\\"
locs = ["Basis", "Orello", "Lyss"]
fName = "WINCWS.FDB"
recName = ""
netPath = "I:\\Bizerba Sicherungen\\WinCWS DB Backups\\"

netSave = False
locSave = False

def saveDB(i):
    netSave = startLoad(netPath)
    locSave = startLoad(locPath)
    if not runs():
        saveTo(locPath + str(i) + locs[i-1] + "\\Database", fName, netPath + locs[i-1])

def recoverDB(i):
    netSave = startLoad(netPath)
    locSave = startLoad(locPath)
    if not runs():
        recoverTo(netPath + locs[i-1], recName, fName, locPath + str(i) + locs[i-1] + "\\Database")

def startLoad(path):
    saves = False
    try:
        saves = sorted(os.listdir(path))
    except WindowsError:
        ui.addText(path + " nicht erreichbar")
        assert False
    return saves

def saveTo(fromPath, fName, toPath):
    currYear = str(datetime.datetime.now().year)
    currMonth = "0" + str(datetime.datetime.now().month)
    currDay = "0" + str(datetime.datetime.now().day)
    currDate = currYear + currMonth[-2:] + currDay[-2:]
    ui.addText("kopiere " + fName + " nach " + toPath)
    newName = toPath[41:] + " " + currDate + fName[-4:]
    shutil.copy(fromPath + "\\" + fName, toPath + "\\" + newName)
    ui.addText("Sicherungsname: " + newName)

def recoverTo(fromPath, recName, fName, toPath):
    ui.addText("kopiere " + recName + " nach " + toPath)
    shutil.copy(fromPath + "\\" + recName, toPath + "\\" + fName)

def runs():
    cmd = 'WMIC PROCESS get Caption'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for l in proc.stdout:
        if "wincws.exe" in l.lower():
            ui.addText("WinCWS zuerst schliessen")
            return True
    return False

ui.create()
