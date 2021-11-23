from tkinter import messagebox
from tkinter import *
import mySQLconnection
import tkinter as tk

# global variables defined here
username = ''
password = ''
email = ''
balance = ''
enterBalance = ''
id = ''

# dictionary userInformation initialized here
userInformation = {0: {'username': 'johnny', 'password': 'luc', 'email': 'jith@gmail.com', 'balance': '10000'}}

# create account function will use the user input on create account screen to store account information within the
# dictionary for later recall
def createAccount(username, password, email, count, balance, loginScreen, createAccountScreen, createUsernameText,
                  createPasswordText, createEmailText, initialDepositText):
    balance = balance
    count = count + 1

    if '$' in balance:
        temp = balance.split("$")
        balance = temp[1]

    if not balance.isnumeric():
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
def login(username, password, loginScreen, welcomeScreen, balanceLabel):
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

            balanceLabel.config(text = '$' + userInformation[i]["balance"])
            global id
            id = i
            return

    messagebox.showerror('Error', 'Login Invalid')

def createScreen(screenNumber, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen):

    if screenNumber == 1:
        loginScreen.forget()
        createAccountScreen.pack(fill='both', expand=1)
    elif screenNumber == 2:
        welcomeScreen.forget()
        depositScreen.pack(fill='both', expand=1)
    elif screenNumber == 3:
        depositScreen.forget()
        welcomeScreen.pack(fill='both', expand=1)
    elif screenNumber == 4:
        welcomeScreen.forget()
        withdrawScreen.pack(fill='both', expand=1)
    elif screenNumber == 5:
        withdrawScreen.forget()
        welcomeScreen.pack(fill='both', expand=1)



def deposit(userDepValue, welcomeScreen, dCustomEntry, balanceLabel):

    if userDepValue == 0:
        customAmount = dCustomEntry.get()

        if '$' in customAmount:
            temp = customAmount.split("$")
            customAmount = temp[1]

        if not customAmount.isnumeric():
            messagebox.showerror('Error', 'Invalid Deposit Value.')
        intBal = int(userInformation[id]["balance"])
        intBal += int(customAmount)
        stringBal = str(intBal)
    else:
        intBal = int(userInformation[id]["balance"])
        intBal += userDepValue
        print(intBal)
        stringBal = str(intBal)
    userInformation[id]["balance"] = stringBal
    balanceLabel.config(text = '$' + userInformation[id]["balance"])


def withdraw(userWithValue, welcomeScreen, wCustomEntry, balanceLabel):

    if userWithValue == 0:
        customAmount = wCustomEntry.get()

        if '$' in customAmount:
            temp = customAmount.split("$")
            customAmount = temp[1]

        if not customAmount.isnumeric():
            messagebox.showerror('Error', 'Invalid Deposit Value.')
        intBal = int(userInformation[id]["balance"])
        intBal -= int(customAmount)
        if intBal < 0:
            messagebox.showerror('Error', 'Balance will go negative!')
        stringBal = str(intBal)
    else:
        intBal = int(userInformation[id]["balance"])
        intBal -= userWithValue
        print(intBal)
        stringBal = str(intBal)
    userInformation[id]["balance"] = stringBal
    balanceLabel.config(text = '$' + userInformation[id]["balance"])
