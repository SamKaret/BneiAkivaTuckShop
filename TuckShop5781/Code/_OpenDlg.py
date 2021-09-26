from PyQt5.QtWidgets import *
import sys

class OpenDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bnei Akiva Tuck Shop")
        self.setMinimumWidth(300)
        self.loadButton = QPushButton("Load Machane")
        self.newButton = QPushButton("Create New Machane")
        self.loadButton.clicked.connect(self.accept)
        self.newButton.clicked.connect(self.reject)
        self.layout = QFormLayout()
        self.layout.addWidget(self.loadButton)
        self.layout.addWidget(self.newButton)
        self.setLayout(self.layout)
        
    def closeEvent(self, event):
        sys.exit()

class NewDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Machane File")
        self.setMinimumWidth(300)
        dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #Declare dialog buttons
        self.buttonBox = QDialogButtonBox(dlgBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QFormLayout()
        self.machaneInput = QComboBox()
        self.machanotList = [
            "Ari",
            "Aleph_Summer",
            "Aleph_Winter",
            "AlephChalutzi",
            "BetBase",
            "BetChalutzi",
            "Gimmel",
            "Maapilim",
            "Haroeh",
            "Gimmel",
            "HCourse",
        ]
        
        self.yearInput = QSpinBox()
        self.yearLabel = QLabel("Year:")
        self.machaneLabel = QLabel("Machane:")
        self.layout.addRow(self.machaneLabel, self.machaneInput)
        self.layout.addRow(self.yearLabel, self.yearInput)
        self.layout.addWidget(self.buttonBox)        
        self.setLayout(self.layout)
        self.yearInput.setRange(5781, 6000)
        self.machaneInput.setEditable(True)
        self.machaneInput.lineEdit().setPlaceholderText(
            "Select machane from list or type new"
        )
        self.machaneInput.addItems(self.machanotList)
