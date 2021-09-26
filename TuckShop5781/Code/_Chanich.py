from PyQt5.QtWidgets  import *
#Class for storing Chanich Names and Funds
class Chanich(QListWidgetItem):
    def __init__(self, firstName, lastName, funds,parent=None):
        super().__init__(parent)
        self.firstName = firstName
        self.lastName = lastName
        self.funds = funds
        self.name = f"{firstName} {lastName}"  

