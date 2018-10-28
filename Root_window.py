import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Root_Window(QWidget):
    def __init__(self):
        super(Root_Window, self).__init__()
        self.widgets_used()


    def widgets_used(self):
        hbox = QHBoxLayout(self)
        frame1 = QFrame()
        frame2 = QFrame()
        frame3 = QFrame()

        frame1.setFrameShape(QFrame.StyledPanel)
        frame1.setFixedSize(QSize(300, 800))
        frame2.setFrameShape(QFrame.StyledPanel)
        #frame2.setFixedSize(QSize(400, 300))

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(frame1)
        splitter1.addWidget(frame2)
        splitter1.setSizes([1000, 2000])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(frame3)

        hbox.addWidget(splitter2)

        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('Root_Window')
        self.show()


def main():
    win = QApplication(sys.argv)
    obj = Root_Window()
    sys.exit(win.exec_())


if __name__ == '__main__':
    main()
