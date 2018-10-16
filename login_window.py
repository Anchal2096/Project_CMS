# This is the first window displayed, asking for login credentials
from tkinter import *
from tkinter import ttk
import smtplib                      # for sending mail
from Database_Config import db      # for database connectivity
import tkinter.messagebox as tm


class LoginWindow(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Text displayed for various fields
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")
        self.label_department = Label(self, text="Department")

        # Entry fields for username and password
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")

        # alignment of each text and field in the 'login' window
        self.label_username.grid(row=0, column=0)
        self.label_password.grid(row=1, column=0)
        self.label_department.grid(row=2, column=0)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        # changed into self.variable for getting dept. value otherwise was a local variable in function
        self.variable = StringVar(master)
        # self.variable.set("DCS") irrelevant line
        self.drop_down = ttk.OptionMenu(self, self.variable, 'DCS', 'DCS', 'DIT', 'DOH', "DOE")
        self.drop_down.grid(row=2, columnspan=8)

        self.checkbox = ttk.Checkbutton(self, text="Keep Me Logged In.")
        self.checkbox.grid(columnspan=2)

        self.login_button = ttk.Button(self, text="Login", command=self._check_login_credentials)
        self.login_button.grid(columnspan=2)

        self.quit_button = ttk.Button(self, text="Forgot Password", command=self._recover_password)
        self.quit_button.grid(columnspan=2)

        self.forgotPass_button = ttk.Button(self, text="Quit", command=self.exit_app)
        self.forgotPass_button.grid(columnspan=2)

        self.pack()

    def _check_login_credentials(self):
        # storing username and password when login button is clicked
        username = self.entry_username.get()
        password = self.entry_password.get()
        department = self.variable.get()

        # Verifying the username and password from the database
        verify_uname_passwd = db.department_admins.find_one({"fullname": username,
                                                             "password": password,
                                                             "department": department})

        if verify_uname_passwd:
            tm.showinfo("Login info", "Welcome Admin")
        else:
            tm.showerror("Login error", "Incorrect username")

    def _recover_password(self):
        department = self.variable.get()

        # try with your own email id
        sender = "atrivedi397@gmail.com"

        # command below returns a cursor object hence to find values one must iterate over it
        all_values = db.department_admins.find({"department": department})
        receiver, message = None, None

        # so iterating over it to get the required values
        for value in all_values:
            receiver = value['email']
            message = "Your Username is " + str(value["fullname"]) + " Your Password is " + str(value["password"])

        # Actual mailing logic
        smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_obj.login(sender, "*******")  # sender and sender's password
        try:
            smtp_obj.sendmail(sender, receiver, message)
            tm.showinfo('Account Recovery', 'An Email for your password recovery has been sent to your Email-Id.')
        except smtplib.SMTPException as error:
            tm.showerror("Error", "SMTP Server Error" + str(error))
        finally:
            smtp_obj.quit()

    @staticmethod
    def exit_app():
        exit(0)


# Creating 'login' window with basic properties
root = Tk()
root.geometry("350x200")
lf = LoginWindow(root)
root.resizable(0, 0)
root.mainloop()
