from PyQt5.QtWidgets import *
from TuckShopUI import Ui_MainWindow

class RemoveTuckDlg(Ui_MainWindow, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Remove Tuck Item")
        self.dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(self.dlgBtn)
        self.buttonBox.accepted.connect(self.confirm)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QFormLayout()
        #create widgets
        self.tuckList = QListWidget()
        self.labelList = parent.TuckCounterFrame.findChildren(QLabel)
        self.labelListStr = []
        for item in self.labelList:
            self.labelListStr.append(item.text())
        self.tuckList.addItems(self.labelListStr)
        # Add widgets to form 
        self.layout.addWidget(self.tuckList)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
    
    def confirm(self):
        self.dlg = RemoveTuckConfDlg(self.tuckList.currentItem().text())
        if self.dlg.exec():
            self.accept()


class RemoveTuckConfDlg(QDialog):
    def __init__(self, tuck):
        super().__init__()
        self.setWindowTitle("Remove Tuck Item")
        self.dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(self.dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QFormLayout()
        #create widgets
        self.nameLabel = QLabel(
            f"Delete {tuck}?"
        )
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)