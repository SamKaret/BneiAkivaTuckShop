from PyQt5.QtWidgets import *

class SearchDlg(QDialog):
    def __init__(self, list=None):
        super().__init__()
        self.setWindowTitle("Searh Results")
        self.setMinimumWidth(300)
        self.layout = QFormLayout()
        if list is None:
            dlgBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            '''Yes I know in this instance it doesn't matter if they press ok 
             or cancel but I can't be bothered to make a separate messagebox'''
            self.buttonBox = QDialogButtonBox(dlgBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            self.label = QLabel("No search Results")
            self.layout.addWidget(self.label)
            self.layout.addWidget(self.buttonBox)
        else:
            self.loadButton = QPushButton("Select Chanich")
            self.newButton = QPushButton("Cancel")
            self.searchList = QListWidget()
            for item in list:

                self.inSearchList = QListWidgetItem(
                    item.text(),
                    self.searchList
                )
            self.loadButton.clicked.connect(self.accept)
            self.newButton.clicked.connect(self.reject)    
            self.layout.addWidget(self.loadButton)
            self.layout.addWidget(self.newButton)
            self.layout.addWidget(self.searchList)
        self.setLayout(self.layout)