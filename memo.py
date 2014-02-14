import datetime
import os
import shutil
import ui

nb024Path = "C:\\Dokumente und Einstellungen\\bizerba\\Desktop\\Datensicherungen"
cardPath = "F:\\BACKUP\\"
card2Path = "G:\\BACKUP\\"
netPath = "I:\\Bizerba Sicherungen\\"

doIt = False

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
    except WindowsError:
        ui.addText(path + " nicht erreichbar")
        assert False
    return saves

def deleteDouble(path, saves):
    for i in range(len(saves)):
        if i == 0:
            continue
        if saves[i-1][:3] <> saves[i][:3]:
            continue
        currMonth = datetime.datetime.now().month
        if int(saves[i][4:6]) > currMonth: # e.g: 505-0102 and 505-1214 after new year
            if os.path.isdir(path + saves[i-1]):
                myRemove(path + saves[i], saves[i], saves[i-1])
            else:
                myRemove(path + saves[i-1], saves[i-1], saves[i])
        else: # e.g: 505-0714 and 505-0721
            if os.path.isdir(path + saves[i]):
                myRemove(path + saves[i-1], saves[i-1], saves[i])
            else:
                myRemove(path + saves[i], saves[i], saves[i-1])

def copyTo(fromPath, aSave, toPath):
    currMonth = datetime.datetime.now().month
    if (not os.path.exists(toPath + "\\" + aSave) and int(aSave[4:6]) <= currMonth and
            os.path.isdir(fromPath + "\\" + aSave)):
        ui.addText("kopiere " + aSave + " nach " + toPath[-33:])
        if doIt:
            shutil.copytree(fromPath + aSave, toPath + "\\" + aSave)

def myRemove(path, remName, keepName):
    ui.addText("entferne " + remName + " behalte " + keepName)
    if doIt:
        if os.path.isdir(path):
            shutil.rmtree(path)
        if os.path.isfile(path):
            os.remove(path)

def tryRepair():
    ui.addText("Versuche " + cardPath[:2] + " zu reparieren")
    ui.addText("Bei Frage \"Ordner oder Verlorene Kette in Datei umwandeln\" mit \"J\" antworten")
    os.system('chkdsk /f ' + cardPath[:2])

ui.create()
