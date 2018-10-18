import sys
from PyQt5.QtWidgets import *
from variables import color
from Database_Config import mongo_connection
from cryptography.fernet import Fernet  # for encryption and decryption


# Main login window class
class LoginWindow(QWidget):

    def __init__(self, main_window=None):
        super().__init__(main_window)

        # root window properties
        self.setFixedSize(360, 240)
        self.setWindowTitle('Login Credentials')

        # Message of the Login window
        self.message = QLabel('Enter your administrative credentials')
        self.message.setStyleSheet("font-size: 15px;"
                                   "font-family: verdana;")

        # widgets for UserID on root window
        self.label_name = QLabel('Admin Name')           # label
        self.label_name.setStyleSheet("font-size: 13px;"
                                      "font-family: verdana;")
        self.field_username = QLineEdit(main_window)     # field

        # widgets for Password on root window
        self.label_password = QLabel('Password ')         # label
        self.label_password.setStyleSheet("font-size: 13px;"
                                          "font-family: verdana;")
        self.field_password = QLineEdit(main_window)      # field
        self.field_password.setEchoMode(QLineEdit.Password)

        # widgets for Department on root window
        self.label_department = QLabel('Department')  # label
        self.label_department.setStyleSheet("font-size: 13px;"
                                            "font-family: verdana;")
        self.options_department = QComboBox()         # drop down options

        # This would be dynamic data, fetched from DB
        self.options_department.addItems([
            '--- Select Your Department ---',
            'Applied Animal Science',
            'Applied Chemistry',
            'Applied Physics',
            'Applied Plant Science',
            'Biotechnology',
            'Computer Science',
            'Economics',
            'Environmental Biology',
            'Environmental Science',
            'Information Technology',
            'Pharmaceutical Science',
            'Rural Management',
            'Sociology'
        ])

        # buttons for login and password recovery options on root window
        self.button_login = QPushButton('Login')
        self.button_login.clicked.connect(self.admin_authentication)
        self.button_forgotPass = QPushButton('Forgot Password')

        # toggling message/text (to be displayed as login status)
        self.login_message = QLabel()
        self.login_message.setHidden(True)

        """
        The layout is of 6x4 row-column matrix, where the 1st row 
        would display message, 2nd row will have widgets for username.
        3rd row will contain widgets for Passwords, 4th row will
        have widgets for Department. The 5th row will contain 
        'login' and 'forgot pass' buttons and lastly 6th row
        be again be blank.
        """

        # 1st row alignment containing the message
        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.message)

        # 2nd row alignment containing 'Username' widgets
        self.layout = QFormLayout()
        self.layout.addRow(self.label_name, self.field_username)

        # 3rd row alignment containing 'Password' widgets
        self.layout.addRow(self.label_password, self.field_password)

        # 4th row alignment containing 'Department' widget
        self.layout.addRow(self.label_department, self.options_department)

        # 5th row alignment containing 'login' and 'forgot password' buttons
        self.row5 = QHBoxLayout()
        self.row5.addStretch()
        self.row5.addWidget(self.button_login)
        self.row5.addStretch()
        self.row5.addWidget(self.button_forgotPass)
        self.row5.addStretch()
        self.layout.addRow(self.row5)

        # 6th row alignment containing login message
        self.row6 = QHBoxLayout()
        self.row6.addWidget(self.login_message)

        # vertical alignments of above widgets
        self.V_align = QVBoxLayout()
        self.V_align.addLayout(self.row1)
        self.V_align.addStretch(1)
        self.V_align.addLayout(self.layout)
        self.V_align.addStretch(1)
        self.V_align.addLayout(self.row6)

        self.setLayout(self.V_align)

    # display login messages
    def display_message(self, status, message):

        # displaying the required message
        if status:
            self.login_message.setText("Login was successful. Proceeding...")

            # setting style to the message area
            style = "color: {text};" \
                    "background-color: {bg};" \
                    "border: 1px solid {b_color};" \
                    "text-align: right;" \
                    .format(text=color['normalGreen'],
                            bg=color['lightGreen'],
                            b_color=color['normalGreen'])

            self.login_message.setStyleSheet(style)
            self.login_message.setHidden(False)

        else:
            self.login_message.setText(message)

            # setting style to the message area
            style = "color: {text};" \
                    "background-color: {bg};" \
                    "border: 1px solid {b_color};" \
                    "text-align: right;" \
                    .format(text=color['crimson'],
                            bg=color['lightRed'],
                            b_color=color['crimson'])

            self.login_message.setStyleSheet(style)
            self.login_message.setHidden(False)

    # verifying administrator credentials from respective DB
    def admin_authentication(self):
        admin_name = self.field_username.text()
        password = self.field_password.text()
        department = self.options_department.currentText()
        index_department = self.options_department.currentIndex()

        # checking if fields are left blank or un-selected
        if admin_name == '':
            # in case of blank user/admin name
            text = "Error: Please fill up your name"
            print(text)
            self.display_message(False, text)   # displaying on window

        elif password == '':
            # in case of blank password
            text = "Error: Please your password"
            print(text)
            self.display_message(False, text)  # displaying on window

        elif index_department is 0:
            # in case of blank user/admin name
            text = "Error: Please select a department"
            print(text)
            self.display_message(False, text)  # displaying on window

        else:
            # processing given data
            database = 'Institute'      # name of the database
            db = mongo_connection[database]

            # name of the table/collection
            collection = 'Admin_Records'

            # fetching key and password from the database for authentication
            results = db[collection].find_one({"Name": admin_name, "Department": department},
                                              {"_id": 0, "Key": 1, "Password": 1})

            # in case the above query return something
            if results is not None:
                # decrypting password so it can be matched
                magic_box = Fernet(results['Key'])
                byte_decrypted_pass = magic_box.decrypt(results['Password'])
                decrypted_pass = byte_decrypted_pass.decode()

                # matching given password with DB password
                if decrypted_pass == self.field_password.text():

                    # creating desired message
                    text = 'Login was successful. Proceeding...'
                    print(text)                         # displaying to console
                    self.display_message(True, text)    # displaying on window
                    exit(0)                             # should redirected instead
                else:
                    print("Wrong Password")
                    self.display_message(False)

            else:
                # creating desired message
                text = 'Invalid User: Please check your credentials'
                print(text)                         # displaying to console
                self.display_message(False, text)   # displaying on window


# main execution starts from here
if __name__ == '__main__':
    application = QApplication(sys.argv)
    loginBox = LoginWindow()
    loginBox.show()
    sys.exit(application.exec_())
