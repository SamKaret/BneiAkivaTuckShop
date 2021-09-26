from PyQt5.QtWidgets import *
from TuckShopUI import Ui_MainWindow
from PyQt5.QtGui import QFont


#Class for creating Tuck Item widgets and info
class TuckItem(Ui_MainWindow, QWidget):
    def __init__(self, item, price, parent=None):
        super().__init__(parent)
        self.item = item
        self.price = price
        self.label = QLabel(parent.TuckCounterFrame)
        self.spinBox = QSpinBox(parent.TuckCounterFrame)
        # self.tuckCounterLayout = QFormLayout(parent.TuckCounterFrame)
        self.label.setText(self.item)
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.spinBox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label.adjustSize()
        self.label.setObjectName(f'{self.item.replace(" ", "")}_label')
        self.spinBox.setObjectName(f'{self.item.replace(" ", "")}_spinBox')
        self.spinBox.valueChanged.connect(parent.changeCost)
        parent.tuckCounterLayout.addRow(self.label, self.spinBox)
        # parent.listOfTuck.append([self.item, self.price])
        # parent.tuckCounterLayout.addWidget(self.spinBox)
        # self.setLayout(parent.tuckCounterLayout)


    # def __del__(self): 
    #     self.label.deleteLater()
    #     self.spinBox.deleteLater()
        