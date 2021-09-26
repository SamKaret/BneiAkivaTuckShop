from PyQt5.QtWidgets import *

class AddTuckDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Tuck")
        dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QGridLayout()
        #create widgets
        self.tuckLabel = QLabel("Tuck Name")
        self.tuckInput = QLineEdit()
        self.tuckInput.setPlaceholderText("Diet Coke")
        self.priceLabel = QLabel("Price (£)")
        self.priceInput = QDoubleSpinBox()     
        self.priceInput.setMinimum(0)
        self.priceInput.setSingleStep(0.05)
        self.priceInput.setPrefix("£")
        self.priceInput.setValue(1)

        # Add widgets to form 
        self.layout.addWidget(self.tuckLabel)
        self.layout.addWidget(self.tuckInput)
        self.layout.addWidget(self.priceLabel)
        self.layout.addWidget(self.priceInput)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)