from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from pasword import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def generasion():
    digetal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    leter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']



btn_OK.clicked.conect(generasion)

app = QApplication([])
window = Widget()
window.show()
app.exec_()
