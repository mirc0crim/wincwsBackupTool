# -*- coding: cp1252 -*-
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
locBldPath = "D:\\Bizerba_Daten\\LabelDesignerProjekte\\"
netBldPath = "I:\\Bizerba Sicherungen\\LabelDesigner\\"

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

def delDB(i):
    netSave = startLoad(netPath)
    if len(recName) < 8:
        ui.addText("Zuerst Name der Sicherung angeben")
        return
    if not runs():
        ui.addText("entferne " + recName)
        os.remove(netPath + locs[i-1] + "\\" + recName)

def layout(i):
    bldFiles = [f for f in os.listdir(locBldPath) if f[-4:] == ".bld"]
    for f in bldFiles:
        name = f.replace("ü", "ue")
        ui.addText("kopiere " + name + " nach " + netBldPath)
        shutil.copy(locBldPath + "\\" + f, netBldPath + "\\" + f)
    
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
    if len(recName) < 8:
        ui.addText("Zuerst Name der Sicherung angeben")
        return
    ui.addText("kopiere " + recName + " nach " + toPath)
    shutil.copy(fromPath + "\\" + recName, toPath + "\\" + fName)

def runs():
    cmd = 'WMIC PROCESS get Caption'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for l in proc.stdout:
        if "wincws.exe" in l.lower():
            ui.addText("WinCWS zuerst schliessen")
            return True
        if "bld.exe" in l.lower():
            ui.addText("Label Designer zuerst schliessen")
            return True
    return False

ui.create()
