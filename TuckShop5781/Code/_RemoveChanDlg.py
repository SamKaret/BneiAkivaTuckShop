from PyQt5.QtWidgets import *
from TuckShopUI import Ui_MainWindow

class RemoveChanDlg(Ui_MainWindow, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Remove Chanich")
        self.dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(self.dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QFormLayout()
        #create widgets
        self.nameLabel = QLabel(
            f"Delete {parent.ChanList.currentItem().text()}?"
        )
        # Add widgets to form 
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)