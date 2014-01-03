import datetime
import os
import shutil
import time
import ui
from thread import start_new_thread as snt

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

counter = 0

def memToPc():
    global counter
    cardSave = startLoad(cardPath)
    nb024Save = startLoad(nb024Path)
    year = "\\" + str(datetime.datetime.now().year) + "\\"
    for i in range(len(cardSave)):
        counter += 1
        currPath = nb024Path + year + cardSave[i][:3]
        snt(copyTo,(cardPath, cardSave[i], currPath,onError,onEnd))
    while counter > 0:
        time.sleep(2)
    cardSave = startLoad(cardPath)
    deleteDouble(cardPath, cardSave)

def memToNet():
    global counter
    cardSave = startLoad(cardPath)
    netSave = startLoad(netPath)
    for i in range(len(cardSave)):
        counter += 1
        snt(copyTo,(cardPath, cardSave[i], netPath,onError,onEnd))
    while counter > 0:
        time.sleep(2)
    netSave = startLoad(netPath)
    deleteDouble(netPath, netSave)

def memToMem():
    global counter
    # 1 -> 2
    cardSave = startLoad(cardPath)
    card2Save = startLoad(card2Path)
    for i in range(len(cardSave)):
        counter += 1
        snt(copyTo,(cardPath, cardSave[i], card2Path,onError,onEnd))
    while counter > 0:
        time.sleep(2)
    card2Save = startLoad(card2Path)
    deleteDouble(card2Path, card2Save)
    # 2 -> 1
    cardSave = startLoad(cardPath)
    card2Save = startLoad(card2Path)
    for i in range(len(card2Save)):
        counter += 1
        snt(copyTo,(card2Path, card2Save[i], cardPath,onError,onEnd))
    while counter > 0:
        time.sleep(2)
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
            if saves[i][4:6] == "12" and saves[i-1][4:6] == "01":
                ui.addText("entferne " + saves[i] + " behalte " + saves[i-1])
                if doIt:
                    shutil.rmtree(path + saves[i])
            else:
                ui.addText("entferne " + saves[i-1] + " behalte " + saves[i])
                if doIt:
                    shutil.rmtree(path + saves[i-1])

def copyTo(fromPath, aSave, toPath, onError, onEnd):
    global counter
    if aSave[4:6] != "12" and not os.path.exists(toPath + "\\" + aSave):
        if doIt:
            try:
                shutil.copytree(fromPath + aSave, toPath + "\\" + aSave)
            except:
                onError()
                return
        onEnd(aSave + " nach " + toPath[-33:] + " kopiert")
    else:
        counter -= 1

def onEnd(s):
    global counter
    ui.addText(s)
    counter -= 1

def onError():
    ui.addText("Ein unerwarteter Fehler ist aufgetreten")
    assert False

ui.create()
