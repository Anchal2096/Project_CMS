from Database_Config import check_connection
from cryptography.fernet import Fernet
from pymongo.errors import ServerSelectionTimeoutError


def insert_random_valid_record():
    # name of the database that is to be used
    # connecting to servers
    connect = check_connection()
    database = 'Institute'  # name of the database
    db = connect[database]

    # name of the table/collection
    collection = 'Admin_Records'

    # taking name of the user
    print("The following records will go into Admin_Records collection:")
    name = input(f"Enter the admin name\n")
    password = input("Enter password\n")
    print("List of Departments to select from:\n")

    # delivering the options of all departments
    department_no = [
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
    ]
    for i in department_no:
        print(f"{(department_no.index(i)+1)}) {i}")

    # storing value (neither number, nor index) of the desired option
    dept_no = int(input("\nEnter the number for the department name\n"))
    dept = department_no[(dept_no-1)]
    email = input("Enter the email\n")
    level = 1
    contact = int(input("Enter the contact number\n"))

    # generating a key
    pass_key = Fernet.generate_key()
    magic_box = Fernet(pass_key)
    encrypted_pass = magic_box.encrypt(str.encode(password))

    # creating a record (which will be inserted into DB)
    record = {'Name': name,
              'Password': encrypted_pass,
              'Department': dept,
              'Email': email,
              'Contact': contact,
              'Clearance_Level': level,
              'Key': pass_key
              }

    # inserting data into DB
    try:
        db[collection].insert(record)
    except ServerSelectionTimeoutError:
        text = "Could not connect. Server may be offline"
        print(text)
        return 0
    print("Your data has been successfully inserted.")


insert_random_valid_record()
