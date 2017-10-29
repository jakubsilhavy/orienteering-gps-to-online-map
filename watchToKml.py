# -*- coding: utf-8 -*-
import os, shutil
from datetime import datetime, timedelta
# configurace
drives = ["e", "f", "g"]
foldersPrefix = r":\GARMIN\ACTIVITY" + "\\"
gpsBabelFolder = r"c:\Program Files (x86)\GPSBabel" + "\\"
gpsBabel = r"gpsbabel.exe"
# men tuto cestu dle potreb
eventFolder = r"c:\Users\jsilhavy\Documents\OB\Treninky\1021_Sklarna"+ "\\"


# prevede fit na KML
def fitToKml(fitFilePath, kmlFilePath):
    command = 'cd {3} && {0} -t -i garmin_fit -f {1} -o kml,line_color=99ff0000 -F {2}'.format(gpsBabel, fitFilePath, kmlFilePath, gpsBabelFolder)
    print command
    os.system(command)

# program
fitFolder = ""
for drive in drives:
    testFitFolder = drive + foldersPrefix
    if os.path.exists(testFitFolder):
        fitFolder = testFitFolder
        break

count = 0
if os.path.exists(fitFolder):
    runnerName = raw_input("Zadej jmeno bezce: ")
    dayOffset = 0 #int(raw_input("Zadej pocet dni zpet, muzes i nulu: "))
    fitFolderContent = os.listdir(fitFolder)
    for fitFolderFile in fitFolderContent:
        if fitFolderFile[-4:].lower() == ".fit".lower():
            fitFilePath =fitFolder+"\\"+fitFolderFile
            creationTime = os.path.getmtime(fitFilePath)
            creationDate = datetime.fromtimestamp(creationTime).date()
            if creationDate == datetime.now().date() - timedelta(dayOffset):
                # fit soubory z dnesniho dne
                print fitFilePath
                kmlFolderPath = eventFolder + runnerName +"_{0}.kml".format(count)
                shutil.copy(fitFilePath, eventFolder + "fit\\" + runnerName +"_{0}.fit".format(count))
                fitToKml(fitFilePath, kmlFolderPath)
                count+=1
