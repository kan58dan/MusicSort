import sys
from MusicSort_Ui import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
app = QApplication([])
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())
