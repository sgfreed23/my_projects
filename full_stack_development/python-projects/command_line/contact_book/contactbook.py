# contact_book.py
# Developer:Samuel Freed
# Project Start Date: 7/11/2022

# contact_book.py imports

import PySimpleGUI as sg
import sqlite3

# contact_book.py Database Creation Using pysqlite3

# Use Line Below when program is final
# con = sqlite3.connect('contact_book.db')

# Use Line Below to delete db when program is terminated
con = sqlite3.connect(':memory:')

c = con.cursor()
c.execute('''CREATE TABLE contacts
            (first_name,last_name,phone_number,email,street_address)''')
c.execute("INSERT INTO contacts VALUES ([0], [1], [2], [3], [4])")
c.execute('SELECT * FROM contacts')
data = c.fetchone()


# contact_book.py GUI
sg.theme("Light Blue 2")

enter_contact_column = [
            [sg.Text("Enter Contact:")],
            [sg.Text('First Name', size = (12,1)), sg.InputText(key="first",size=(15,1)),sg.Text('Last Name', size = (12,1)), sg.InputText(key="last",size=(15,1))],
            [sg.Text('Phone Number', size = (12,1)), sg.InputText(key="phone",size = (48,1))],
            [sg.Text('Email', size = (12,1)), sg.InputText(key="email",size=(48,1))],
            [sg.Text('Street Address', size = (12,1)), sg.InputText(key="addy",size = (48,1))],
            [sg.Submit("Add"), sg.Cancel("Clear")]
    ]

contacts_column = [
        [sg.Text("Contacts:")],
        [sg.Text(data)]
           
    ]

layout = [
    [
        sg.Column(enter_contact_column),
        sg.VSeperator(),
        sg.Column(contacts_column)
        ]
    ]
window = sg.Window("Contact Book", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Add":
        con.commit()
        con.close()

window.close()

