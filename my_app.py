from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_window import *

class Main_win(QWidget):
	def __init__ (self):
		super().__init__()

		self.initUI()
		self.connect()
		self.set_appear()

		self.show()

	def initUI(self):
		#Creación de los elementos graficos
		self.btn_next = QPushButton(txt_next, self)
		self.hello_text = QLabel(txt_hello)
		self.instruction = QLabel(txt_instruction)
		#Creamos un layout vertical
		self.layout_line = QVBoxLayout()
		self.layout_line.addwidget(self.hello_text,alignment = Qt.AlignLeft)
		self.layout_line.addwidget(self.instruction,alignment = Qt.AlignLeft)
		self.layout_line.addwidget(self.btn_next,alignment = Qt.AlignCenter)
		self.setLayout(self.layout_line)
	def next_click(self):
		self.tw = TestWin()
		self.hide()
	def connects(self):
		self.btn_next.clicked.connect(self.next_click)
	#Este metodo nod permite configurar como lucira la ventana
	def set_appear(self):
		self.setWindowTitle(txt_title)#Colocamos el nombre de nuestra ventana
		self.resize(win_width,win_height)#Colocamos elntamaño de nuestra ventana
		self.move(win_x,win_y)

app = QApplication([])
mw = Main_win()
app.exec_()
