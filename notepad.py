import sys
import os
from tkinter import Menu
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
from click import open_file

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.text_area=QTextEdit()
        self.clear=QPushButton("Clear")
        self.open=QPushButton("Open")
        self.save=QPushButton("Save")

        hbox=QHBoxLayout()
        hbox.addWidget(self.clear)
        hbox.addWidget(self.open)
        hbox.addWidget(self.save)

        vbox=QVBoxLayout()
        vbox.addWidget(self.text_area)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle("Notepad")
        self.clear.clicked.connect(self.clearfonk)
        self.open.clicked.connect(self.openfonk)
        self.save.clicked.connect(self.savefonk)

    def clearfonk(self):
        self.text_area.clear()

    def openfonk(self):
        file_name=QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())
    
    def savefonk(self):
        file_name=QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        with open(file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wndw=Notepad()
        self.setCentralWidget(self.wndw)
        self.create_menu()
    
    def create_menu(self):
        menubar=self.menuBar()
        file=menubar.addMenu("File")
        opn_file=QAction("Open File",self)
        sv_file=QAction("Save File",self)
        clr=QAction("Clear File",self)
        ext=QAction("Exit",self)

        file.addAction(opn_file)
        file.addAction(sv_file)
        file.addAction(clr)
        file.addAction(ext)
        file.triggered.connect(self.response)

        self.setWindowTitle("NotePad")
        self.show()

    def response(self,action):
        if action.text()=="Open File":
            self.wndw.openfonk()
        elif action.text()=="Save File":
            self.wndw.savefonk()
        elif action.text()=="Clear File":
            self.wndw.clearfonk()
        elif action.text()=="Exit":
            qApp.quit()

app=QApplication(sys.argv)
menu=Menu()
sys.exit(app.exec_())