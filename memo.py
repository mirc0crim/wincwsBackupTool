import datetime
import os
import shutil
import ui

nb024Path = "C:\\Dokumente und Einstellungen\\bizerba\\Desktop\\Datensicherungen"
cardPath = "-:\\BACKUP\\"
card2Path = "-:\\BACKUP\\"
netPath = "I:\\Bizerba Sicherungen\\"

doIt = False
verbose = False

nb024Save = False
cardSave = False
card2Save = False
netSave = False

def memToPc():
    cardSave = startLoad(cardPath)
    nb024Save = startLoad(nb024Path)
    year = "\\" + str(datetime.datetime.now().year) + "\\"
    for i in range(len(cardSave)):
        currPath = nb024Path + year + cardSave[i][:3]
        copyTo(cardPath, cardSave[i], currPath)
    cardSave = startLoad(cardPath)
    deleteDouble(cardPath, cardSave)

def memToNet():
    cardSave = startLoad(cardPath)
    netSave = startLoad(netPath)
    for i in range(len(cardSave)):
        copyTo(cardPath, cardSave[i], netPath)
    netSave = startLoad(netPath)
    deleteDouble(netPath, netSave)

def memToMem():
    # 1 -> 2
    cardSave = startLoad(cardPath)
    card2Save = startLoad(card2Path)
    for i in range(len(cardSave)):
        copyTo(cardPath, cardSave[i], card2Path)
    card2Save = startLoad(card2Path)
    deleteDouble(card2Path, card2Save)
    # 2 -> 1
    cardSave = startLoad(cardPath)
    card2Save = startLoad(card2Path)
    for i in range(len(card2Save)):
        copyTo(card2Path, card2Save[i], cardPath)
    cardSave = startLoad(cardPath)
    deleteDouble(cardPath, cardSave)

def startLoad(path):
    saves = False
    try:
        saves = sorted(os.listdir(path))
        if verbose:
            ui.addText(path + " erreichbar")
    except WindowsError:
        ui.addText(path + " nicht erreichbar")
        assert False
    return saves

def deleteDouble(path, saves):
    for i in range(len(saves)):
        if i == 0:
            continue
        if saves[i-1][:3] == saves[i][:3]:
            if saves[i][4:6] == "12" and (saves[i-1][4:6] == "01" or saves[i-1][4:6] == "00"):
                ui.addText("entferne " + saves[i] + " behalte " + saves[i-1])
                if doIt:
                    shutil.rmtree(path + saves[i])
            else:
                ui.addText("entferne " + saves[i-1] + " behalte " + saves[i])
                if doIt:
                    shutil.rmtree(path + saves[i-1])
            if saves[i-1][4:6] == "00"
                ui.addText("entferne " + saves[i-1]
                if doIt:
                    shutil.rmtree(path + saves[i-1])

def copyTo(fromPath, aSave, toPath):
        if not os.path.exists(toPath + "\\" + aSave):
            ui.addText("kopiere " + aSave + " nach " + toPath[-33:])
            if doIt:
                shutil.copytree(fromPath + aSave, toPath + "\\" + aSave)

ui.create()
