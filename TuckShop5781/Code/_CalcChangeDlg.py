from TuckShopUI import Ui_MainWindow
from PyQt5.QtWidgets import *

class CalcChangeDlg(Ui_MainWindow, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculate Change")
        dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QGridLayout()
        #create widgets
        self.minChangeLabel = QLabel(
            f'Minimum amount of change.'
        )
        self.minChange = QDoubleSpinBox()
        self.minChange.setMinimum(0)
        self.minChange.setSingleStep(0.05)
        self.minChange.setPrefix("£")
        self.minChange.setValue(5)
        self.roundAmountLabel = QLabel(
            f'Round to nearest'
        )
        self.roundAmount = QDoubleSpinBox()
        self.roundAmount.setMinimum(0)
        self.roundAmount.setSingleStep(0.01)
        self.roundAmount.setPrefix("£")
        self.roundAmount.setValue(0.05)

        # Add widgets to form 
        self.layout.addWidget(self.minChangeLabel)
        self.layout.addWidget(self.minChange)
        self.layout.addWidget(self.roundAmountLabel)
        self.layout.addWidget(self.roundAmount)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)