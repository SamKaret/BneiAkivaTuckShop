#import necessary pyqt modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#import Ui class from qtdesigner file converted from .ui to .py 
from TuckShopUI import Ui_MainWindow
#Import dialog box classes
from _AddTuckDlg import AddTuckDlg
from _AddChanDlg import AddChanDlg
from _RemoveChanDlg import RemoveChanDlg
from _SearchDlg import SearchDlg
from _AddFundsDlg import AddFundsDlg
from _RemoveTuckDlg import RemoveTuckDlg
from _CalcChangeDlg import CalcChangeDlg
#Import Object Classes
from _Chanich import Chanich
from _TuckItem import TuckItem
# Import Pandas for excel compatability
import pandas as pd
#Import json for saving chan/tuck lists
import json

class TuckShopWindow(QMainWindow, Ui_MainWindow):
    singleton: 'TuckShopWindow' = None # For restarting

    from jsonFuncs import startWindow, saveJson
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #call qtdesigner ui setup
        self.setupUi(self)
        #Create List variables for holding Chans/Tuck
        self.jsonDict = {}
        self.jsonDict['listOfChans'] = []
        self.jsonDict['listOfTuck'] = []      

        # Add connections to buttons/on changes for edits
        self.SearchButton.clicked.connect(self.searchButtonPressed)
        self.SubmitOrderButton.clicked.connect(self.submitButtonPressed)
        self.LastNameSortButton.clicked.connect(self.sortByLastButtonPressed)
        self.FirstNameSortButton.clicked.connect(self.sortByFirstButtonPressed)
        self.AddChanichButton.clicked.connect(self.addChanButtonPressed)
        self.RemoveChanichButton.clicked.connect(self.removeChanButtonPressed)
        self.AddTuckButton.clicked.connect(self.addTuckButtonPressed)
        self.RemoveTuckButton.clicked.connect(self.removeTuckButtonPressed)
        self.AddFundsButton.clicked.connect(self.addFundsButtonPressed)
        self.ChanList.itemClicked.connect(self.changeLabels)
        self.actionHelp_Page.triggered.connect(self.helpClicked)
        self.actionNew_Machane.triggered.connect(self.newMachaneClicked)
        self.actionCalculate_Change.triggered.connect(self.calcChangeClicked)
        self.actionImport_Chans.triggered.connect(self.importChansClicked)
        self.actionImport_Tuck.triggered.connect(self.importTuckClicked)
        self.actionView_Tuck_List.triggered.connect(self.viewTuckListClicked)
        
        self.show() # Debugging Line 
        '''Ignore the comment on the above line, it's the most important line
            in this file to keep the menubar working'''
        #Load lists from save file or create new lists
        self.startWindow(application_path)
        


    ##Define Functions
        ##Buttons when pressed functions

    #Search Button
    def searchButtonPressed(self):
        if items:= self.ChanList.findItems(
                self.SearchBoxLineEdit.text(), Qt.MatchContains
            ):
            self.dlg = SearchDlg(items)
            if self.dlg.exec():
                item = self.ChanList.findItems(
                        self.dlg.searchList.currentItem().text(),
                        Qt.MatchContains)
                self.ChanList.setCurrentItem(item[0])
            else:
                """Uncomment to clear searchbox between searches"""
                # self.SearchBoxLineEdit.setText("")
                pass
        
    #Sort by last name button
    def sortByLastButtonPressed(self):
        #Can't iterate through QListWidget so need to use .item workaround
        namelist=[]
        for i in range(self.ChanList.count()):
            namelist.append([
                self.ChanList.item(i).data(34),  # Last Name
                self.ChanList.item(i).text()    # Full Name
            ])
        namelist.sort()
        for name in namelist:
            # print(name)
            for i in range(self.ChanList.count()):
                currentChan = self.ChanList.item(i)
                if name[1] == currentChan.text():
                    self.ChanList.takeItem(self.ChanList.row(currentChan))
                    self.ChanList.addItem(currentChan)

    #Sort by First Name
    def sortByFirstButtonPressed(self):
        self.ChanList.sortItems()

    # Add Chanich Button
    def addChanButtonPressed(self):
        self.dlg = AddChanDlg()
        
        if self.dlg.exec():
            #Check Inputs are correct and add them to chanList widget
            newChan = Chanich(
                self.dlg.firstNameInput.text(), 
                self.dlg.lastNameInput.text(), 
                self.dlg.fundsInput.value()
            )
            self.addChan(newChan)
       
    #Remove chanich button
    def removeChanButtonPressed(self):
        if self.ChanList.currentRow() != -1 and self.ChanList.count():    
            self.dlg = RemoveChanDlg(self)
            
            if self.dlg.exec():
                #Check if correct chanich being removed then remove from list 
                # and delete QListWidgetItem/dictionary pair
                currentChan = self.ChanList.currentItem()
                self.jsonDict['listOfChans'] = [
                    i for i in self.jsonDict['listOfChans']
                    if not (
                        i['firstName'] == currentChan.data(33)
                        and
                        i['lastName'] == currentChan.data(34)
                    )
                ]
                self.ChanList.takeItem(self.ChanList.currentRow())
                self.changeLabels()
                self.saveJson()

    # Add tuck button
    def addTuckButtonPressed(self):
        #self.x. for x in widgetsAdded 
        self.dlg = AddTuckDlg()
        if self.dlg.exec():
            newTuck = TuckItem(
                self.dlg.tuckInput.text(), self.dlg.priceInput.value(), self
            )
            self.addTuck(newTuck)
            self.saveJson()

    #Remove Tuck Button
    def removeTuckButtonPressed(self):
        # print(self.TuckCounterFrame.findChildren(QLabel))
        if self.jsonDict['listOfChans'] != []:
            self.dlg = RemoveTuckDlg(self)
            if self.dlg.exec():
                #delete relevant widgets from tuckCounterLayout
                widgetList = self.TuckCounterFrame.findChildren(QLabel)
                for widget in widgetList:
                    if widget.text() == self.dlg.tuckList.currentItem().text():
                        # print(self.jsonDict['listOfTuck'])
                        self.jsonDict['listOfTuck'] = [
                            i for i in self.jsonDict['listOfTuck'] 
                            if not (i['item'] == widget.text())
                        ]
                        self.tuckCounterLayout.removeRow(widgetList.index(widget))
                        self.saveJson()

    # Add Funds Button
    def addFundsButtonPressed(self):
        if self.ChanList.currentRow() != -1 and self.ChanList.count():    
            self.dlg = AddFundsDlg(self)
            if self.dlg.exec():
                currentChan = self.ChanList.currentItem()
                currentChan.setData(
                    32, (currentChan.data(32) + self.dlg.fundsInput.value())
                )
                self.changeLabels()
                for chan in self.jsonDict['listOfChans']:
                    if (
                        chan['firstName'] == currentChan.data(33)
                        and
                        chan['lastName'] == currentChan.data(34)
                    ):
                        chan['funds'] = currentChan.data(32)
                self.saveJson()

    #Submit Order Button
    def submitButtonPressed(self):
        if self.ChanList.currentRow() != -1 and self.ChanList.count(): 
            # Adjust Chan funds
            currentChan = self.ChanList.currentItem()
            currentChan.setData(32, (currentChan.data(32) - self.calcCost()))
            for chan in self.jsonDict['listOfChans']:
                    if (
                        chan['firstName'] == currentChan.data(33)
                        and
                        chan['lastName'] == currentChan.data(34)
                    ):
                        chan['funds'] = currentChan.data(32)
            self.saveJson()
            # Reset all spinBoxes to 0
            for tuck in self.jsonDict['listOfTuck']:
                for i in range(self.tuckCounterLayout.count()):
                    if self.checkSpinBox(tuck, i):
                        self.tuckCounterLayout.itemAt(i).widget().setValue(0)
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Tuck Shop Error Message")
            self.msg.setText(
                "Error: Select a Chanich"
            )
            self.msg.exec()
        
    ## Other Functions

    # Add chan to list and widget
    def addChan(self, newChan):
        self.jsonDict['listOfChans'].append({
            'firstName': newChan.firstName,
            'lastName': newChan.lastName,
            'funds': newChan.funds
        })
        currentChan = QListWidgetItem(newChan.name, self.ChanList)
        currentChan.setText(newChan.name)
        currentChan.setData(32, newChan.funds)
        currentChan.setData(33, newChan.firstName)
        currentChan.setData(34, newChan.lastName)
    
    # Add tuck to list
    def addTuck(self,newTuck):
        self.jsonDict['listOfTuck'].append({
            'item': newTuck.item,
            'price': newTuck.price
        })
    
    ## Change Labels

    # Change Name/fund labels when new name in line edit is selected
    def changeLabels(self):
        currentChan = self.ChanList.currentItem()
        self.NameLabel.setText(
            f"Name: {currentChan.data(33)} "
            f"{currentChan.data(34)}")
        self.CurrentFundsLabel.setText(
            f'Current Funds: £'
            f'{currentChan.data(32):.2f}')
        self.changeCost()

    # Change Cost label according to items in spinboxes
    def changeCost(self):
        currentChan = self.ChanList.currentItem()
        self.CostLabel.setText(
            f"Cost: £{self.calcCost():.2f}")
        if self.ChanList.currentRow() != -1: 
            self.NewFundsLabel.setText(
                f'New Funds: £'
                f'{currentChan.data(32) - self.calcCost():.2f}')

    # Compares spinBox at index i to name (item) from tuck object.
    # Returns True or False
    def checkSpinBox(self, tuck, i):
        return(
            self.tuckCounterLayout.itemAt(i).widget().objectName() 
            ==
            f'{tuck["item"].replace(" ", "")}_spinBox')

    # Calculates cost from spinboxes / tuck list
    def calcCost(self): 
        cost = 0
        for tuck in self.jsonDict['listOfTuck']:
            for j in range(self.tuckCounterLayout.count()):
                if self.checkSpinBox(tuck, j):
                    cost += (
                        tuck["price"] * 
                        self.tuckCounterLayout.itemAt(j).widget().value()
                    )
        return(cost)

     

    ## Define Menu Actions
    def importChansClicked(self):
        importFileName, _ = QFileDialog.getOpenFileName(
            self, "Select excel file",
            "",
            "Excel Files (*.xlsx *.xls *.xlsm *.xlsb, *.odf *.ods *.odt)",
        )
        if importFileName:
            importFile = pd.read_excel(
                importFileName
                )
            for row in importFile.itertuples(index=False, name=None):
                newChan = Chanich(
                    row[0],
                    row[1],
                    float(row[2].replace('£', ''))
                )
                self.addChan(newChan)

    def importTuckClicked(self):
        importFileName, _ = QFileDialog.getOpenFileName(
            self, "Select excel file",
            "",
            "Excel Files (*.xlsx *.xls *.xlsm *.xlsb, *.odf *.ods *.odt)",
        )
        if importFileName:
            importFile = pd.read_excel(
                importFileName
                )
            for row in importFile.itertuples(index=False, name=None):
                newTuck = TuckItem(
                    row[0],
                    float(row[1].replace('£','')),
                    self
                )
                self.addTuck(newTuck)

    def newMachaneClicked(self):
        # Now the New/Load Machane option
        '''Restarts the whole app'''
        os.execv(
            sys.executable,
            ['python'] + sys.argv
        )
    
    # def loadMachaneClicked(self):
    #     pass

    def calcChangeClicked(self):
        self.dlg = CalcChangeDlg()
        if self.dlg.exec():
            rows = [
                [chan['firstName'],
                 chan['lastName'],
                 self.get_change(chan['funds'])
                ]
                if chan['funds'] >= self.dlg.minChange.value() else [None] * 3
                for chan in self.jsonDict['listOfChans']
            ]
            pd.DataFrame(
                rows, columns=['First Name', 'Surname', 'Change']
            ).dropna().to_excel(
                self.fname.replace('.json','change.xlsx'),
                index=False,
            )

    def get_change(self, fund):
        return (self.dlg.roundAmount.value()* round(
                fund / self.dlg.roundAmount.value()
            ))            

    def viewTuckListClicked(self):
        rows = [
            [tuck['item'], f"£{tuck['price']}"]
            for tuck in self.jsonDict['listOfTuck']    
        ]
        pd.DataFrame(
            rows, columns=['Tuck','Price']
        ).to_excel(
            self.fname.replace('.json','tuckList.xlsx'),
            index=False
        )

    def helpClicked(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("HAHAHAHAHAHAHAHAH")
        self.msg.setText(
            "BITCH YOU THOUGHT"
        )
        self.msg.exec()

        
if __name__ == "__main__":
    import sys, os
    # Find current application PATH
    if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
        # print(application_path)
    
    # Run app
    app = QApplication(sys.argv)
    shop = TuckShopWindow()
    shop.show()
    sys.exit(app.exec_())
        