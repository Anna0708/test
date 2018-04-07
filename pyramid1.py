
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import (Qt, pyqtSignal, QRect)


class Card1(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)
        self.setPixmap(QPixmap("Heart_king.png"))
        self.setScaledContents(True)
        self.opened = True

    def mousePressEvent(self, ev):
        self.clicked.emit()

    def rotate(self):
        image = "cardback.jpg" if self.opened else "Heart_king.png"
        self.setPixmap(QPixmap(image))
        self.opened = not self.opened

class Card2(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)
        self.setPixmap(QPixmap("Heart_ace.png"))
        self.setScaledContents(True)
        self.opened = True

    def mousePressEvent(self, ev):
        self.clicked.emit()

    def rotate(self):
        image = "cardback.jpg" if self.opened else "Heart_ace.png"
        self.setPixmap(QPixmap(image))
        self.opened = not self.opened


class Card(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)
        self.setPixmap(QPixmap("Heart_queen.png"))
        self.setScaledContents(True)
        self.opened = True



    def mousePressEvent(self, ev):
        self.clicked.emit()

    def rotate(self):
        image = "cardback.jpg" if self.opened else "Heart_queen.png"
        self.setPixmap(QPixmap(image))
        self.opened = not self.opened

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("background.png"))
        QWidget.paintEvent(self, event)

    def init_ui(self):
        card1 = Card1(self)
        card2 = Card2(self)
        card = Card(self)
        card.clicked.connect(card.rotate)
        card1.clicked.connect(card1.rotate)
        card2.clicked.connect(card2.rotate)
        card.move(590,90)
        card1.move(540,200)
        card2.move(640,200)

        self.show()



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setCentralWidget(Widget(self))
        self.setGeometry(300,300,350,350)
        self.setWindowTitle('Pyramid Solitaire')
        self.init_ui()

    def init_ui(self):
        main_menu = self.menuBar()
        main_menu.addMenu('Help')

        exitAct = QAction( '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit ')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Exit')
        fileMenu.addAction(exitAct)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())