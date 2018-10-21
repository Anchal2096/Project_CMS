# the main window implementfation
import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_interface()

    @staticmethod
    def logout():
        print("Admin logged out successfully")

    def create_interface(self):
        # main window properties
        self.setWindowTitle('FoxABH')
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)

        # creating a (blank) menu bar at top
        # and status bar at the bottom
        main_menu = self.menuBar()
        self.statusBar().showMessage('Logged in as Admin')

        # adding tabs to the blank menu bar
        app_tab = main_menu.addMenu('&App')
        settings_tab = main_menu.addMenu('&Settings')
        help_tab = main_menu.addMenu('&Help')

        # adding action(s) to the above tabs:
        # 'App' tab's logOut properties
        app_logout = QAction('&LogOut', self)
        app_logout.setStatusTip('Logout as current user')
        app_logout.setShortcut('Ctrl+L')
        app_logout.triggered.connect(self.logout)
        app_tab.addAction(app_logout)

        # 'App' tab's Exit properties
        app_exit = QAction('E&xit', self)
        app_exit.setStatusTip('Exit this Application')
        app_exit.setShortcut('Ctrl+Q')
        app_exit.triggered.connect(qApp.exit)
        app_tab.addAction(app_exit)


# execution starts from here
if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())
