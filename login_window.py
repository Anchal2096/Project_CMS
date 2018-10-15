# This is the first window displayed, asking for login credentials
from tkinter import *
from tkinter import ttk
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

        variable = StringVar(master)
        variable.set("DCS")
        self.drop_down_box = ttk.OptionMenu(self, variable, "DCS", "IT", "HINDI", "B.Ed").grid(row=2, columnspan=8)

        self.checkbox = ttk.Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.login_button = ttk.Button(self, text="Login", command=self._check_login_credentials)
        self.login_button.grid(columnspan=2)

        self.quit_button = ttk.Button(self, text="forgot Password", command=self.exit_app)
        self.quit_button.grid(columnspan=2)

        self.forgotPass_button = ttk.Button(self, text="Quit", command=self.exit_app)
        self.forgotPass_button.grid(columnspan=2)

        self.pack()

    def _check_login_credentials(self):
        # storing username and password when login button is clicked
        username = self.entry_username.get()
        password = self.entry_password.get()

        # verifying login credentials.
        # though following lines are to be replaced completely
        # by info fetched from the database
        if username == "admin" and password == "admin@123":
            tm.showinfo("Login info", "Welcome Admin")
        else:
            tm.showerror("Login error", "Incorrect username")

    @staticmethod
    def _recover_password():
        print("An email must be sent to the admin")

    @staticmethod
    def exit_app():
        exit(0)


# Creating 'login' window with basic properties
root = Tk()
root.geometry("350x200")
lf = LoginWindow(root)
root.resizable(0, 0)
root.mainloop()
