from TuckShopUI import Ui_MainWindow
from PyQt5.QtWidgets import *

class AddFundsDlg(Ui_MainWindow, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Funds")
        dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QGridLayout()
        #create widgets
        self.fundsLabel = QLabel(
            f'Add funds to {parent.ChanList.currentItem().text()}?'
        )
        self.fundsInput = QDoubleSpinBox()
        self.fundsInput.setMinimum(0)
        self.fundsInput.setSingleStep(0.05)
        self.fundsInput.setPrefix("£")
        self.fundsInput.setValue(10)

        # Add widgets to form 
        self.layout.addWidget(self.fundsLabel)
        self.layout.addWidget(self.fundsInput)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)