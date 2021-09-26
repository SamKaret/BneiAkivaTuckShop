from PyQt5.QtWidgets import *


class AddChanDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Chanich")
        dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        #Create input form
        self.layout = QFormLayout()
        #create widgets
        self.firstNameLabel = QLabel("First Name")
        self.firstNameInput = QLineEdit()
        self.firstNameInput.setPlaceholderText("Name")
        self.lastNameLabel = QLabel("Last Name")
        self.lastNameInput = QLineEdit()
        self.lastNameInput.setPlaceholderText("Surname")
        self.fundsLabel = QLabel("Funds (£)")
        self.fundsInput = QDoubleSpinBox()

        self.fundsInput.setMinimum(0)
        self.fundsInput.setSingleStep(0.05)
        self.fundsInput.setPrefix("£")
        self.fundsInput.setValue(10)

        # Add widgets to form 
        self.layout.addWidget(self.firstNameLabel)
        self.layout.addWidget(self.firstNameInput)
        self.layout.addWidget(self.lastNameLabel)
        self.layout.addWidget(self.lastNameInput)
        self.layout.addWidget(self.fundsLabel)
        self.layout.addWidget(self.fundsInput)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


# Code for Validating QLineEdit to 2 decimal float.
# Idiot me should have started with a QDoubleSpinBox in the first place

# from PyQt5.QtGui import QDoubleValidator

        # self.validFloat = QDoubleValidator()
        # self.validFloat.setBottom(0) #in case line edit works better
        # self.validFloat.setDecimals(2)
        # self.validFloat.setNotation(QDoubleValidator.StandardNotation)
        # self.fundsInput.setValidator(self.validFloat)
        # self.fundsInput.setPlaceholderText("0.00")