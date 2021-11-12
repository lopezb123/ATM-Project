from tkinter import messagebox
from tkinter import *
import tkinter as tk

# global variables defined here
username = ''
password = ''
email = ''
balance = ''
enterBalance = ''

# dictionary userInformation initialized here
userInformation = {0: {'username': 'jith', 'password': 'luc', 'email': 'jith@gmail.com', 'balance': '100000000'}}


# create account screen function will switch login screen to create account screen
def createAccountScreen(loginScreen, createAccountScreen):
    loginScreen.forget()
    createAccountScreen.pack(fill='both', expand=1)


# create account function will use the user input on create account screen to store account information within the
# dictionary for later recall
def createAccount(username, password, email, count, balance, loginScreen, createAccountScreen, createUsernameText,
                  createPasswordText, createEmailText, initialDepositText):
    balance = balance
    count = count + 1

    if '$' in balance:
        temp = balance.split("$")
        balance = temp[1]

    if balance.isnumeric() == False:
        messagebox.showerror('Error', 'Invalid Deposit Value.')
        return

    for i in range(len(userInformation)):
        if username == userInformation[i]['username']:
            messagebox.showinfo('Error', 'Username Taken')
            return
        if email == userInformation[i]['email']:
            messagebox.showinfo('Error', 'Email Already in Use')
            return
    userInformation[count] = {'username': username, 'password': password, 'email': email, 'balance': balance}

    createAccountScreen.forget()
    loginScreen.pack(fill='both', expand=1)
    createUsernameText.delete(0, END)
    createPasswordText.delete(0, END)
    createEmailText.delete(0, END)
    initialDepositText.delete(0, END)
    createUsernameText.insert(0, 'Username')
    createPasswordText.insert(0, 'Password')
    createEmailText.insert(0, 'Email Address')
    initialDepositText.insert(0, '$0')

# login function will use the user data entered in login screen to ensure a valid login was entered, and if so,
# the login screen will be changed to the welcome screen
def login(username, password, loginScreen, welcomeScreen):
    tempUsername = username
    tempPassword = password
    for i in range(len(userInformation)):
        if tempUsername == userInformation[i]['username'] and tempPassword == userInformation[i]['password']:
            loginScreen.forget()
            welcomeScreen.pack(fill='both', expand=1)

            usernameLabel = Label(welcomeScreen, text=tempUsername, font=('Helvatical bold', 15)).place(relx=0.95,
                                                                                                        rely=0.05,
                                                                                                        anchor=E)
            emailLabel = Label(welcomeScreen, text=userInformation[i]['email'], font=('Helvatical bold', 15)).place(
                relx=0.95,
                rely=0.1, anchor=E)

            balanceLabel = Label(welcomeScreen, text='$' + userInformation[i]['balance'], font=('Helvatical bold', 30),
                                 fg='green').place(relx=0.5,
                                                   rely=0.5, anchor=CENTER)
            return

    messagebox.showerror('Error', 'Login Invalid')
