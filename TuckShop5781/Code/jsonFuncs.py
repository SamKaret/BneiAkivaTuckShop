from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#Import dialog box classes
from _OpenDlg import OpenDlg, NewDlg
#Import Object Classes
from _Chanich import Chanich
from _TuckItem import TuckItem
#Import json for saving chan/tuck lists
import json
import sys

#Load lists from save file or create new lists
def startWindow(self, application_path):
    self.openDlg = OpenDlg()
    # Load file selected
    if self.openDlg.exec():
        #Call json file selection
        self.fname, _ = QFileDialog.getOpenFileName(
            self, "Select Machane",
            application_path,
            "Machane Files (*.json)"
        )
        # file selected
        if self.fname:   #Load selected json file
            with open(self.fname, 'r') as file:
                data = json.load(file)
            # Load list of chanichim as QListWidgetItems
            for chan in data["listOfChans"]:
                newChan = Chanich(
                    chan["firstName"],
                    chan["lastName"],
                    chan["funds"]
                )
                self.addChan(newChan)
            # Load Tuck Items in as TuckItem objects
            for tuck in data["listOfTuck"]:
                # print(tuck["item"], tuck["price"])
                newTuck = TuckItem(
                    tuck["item"], tuck["price"], self
                    )
                self.addTuck(newTuck)       
        # No file selected (cancel/exit)
        else:
            #Call original load/create new dialog again
            startWindow(self, application_path)
    # New file selected
    else:
        #Call json file creation
        self.newDlg = NewDlg()
        if self.newDlg.exec():
            self.fname = (
                f'{self.newDlg.machaneInput.currentText()}'
                f'_'
                f'{self.newDlg.yearInput.value()}'
                f'.json'
            )
            try:
                with open(self.fname, 'x') as file:
                    json.dump(self.jsonDict, file, indent=6)
            except:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setWindowTitle("Tuck Shop Error Message")
                self.msg.setText(
                    "Error: Database already exists for that machane."
                )
                self.msg.exec()
                startWindow(self, application_path)
        else:
            sys.exit()

#Update Json file
def saveJson(self):
    with open(self.fname, 'w') as file:
        json.dump(self.jsonDict, file, indent=6)
    pass