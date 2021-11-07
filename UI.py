import main
from tkinter import *
import tkinter as tk
count = 0
root = Tk()
loginScreen = tk.Frame(root)
createAccountScreen = tk.Frame(root)
welcomeScreen = tk.Frame(root)
root.geometry("600x600")
loginScreen.pack(fill='both', expand=1)
ATMLabel = Label(loginScreen, text="ATM", font=('Helvatical bold', 20)).place(relx=0.5, rely=.1, anchor=CENTER)
usernameText = tk.Entry(loginScreen)
usernameText.place(relx=0.5, rely=.3, anchor=CENTER)
usernameText.insert(0, 'Username')
usernameText.config(foreground='gray')
passwordText = tk.Entry(loginScreen)
passwordText.place(relx=0.5, rely=.4, anchor=CENTER)
passwordText.insert(0, 'Password')
passwordText.config(foreground='gray')
loginButton = Button(loginScreen, text="Login", height=3, width=20, command=lambda: main.login(usernameText.get(), passwordText.get(), loginScreen, welcomeScreen)).place(relx=0.5, rely=.6, anchor=CENTER)
createButton = Button(loginScreen, text="Create an Account", height=3, width=20, command=lambda: main.createAccountScreen(loginScreen, createAccountScreen)).place(relx=0.5, rely=.8,
                                                                                                    anchor=CENTER)
loginScreen.pack(fill='both', expand=1)

companyLabel = Label(welcomeScreen, text="One Touch", font=('Helvatical bold', 15)).place(relx=0, rely=0.05, anchor=W)
depositButton = Button(welcomeScreen, text="Deposit", height=3, width=20).place(relx=0.05, rely=.90, anchor=W)
withdrawButton = Button(welcomeScreen, text="Withdraw", height=3, width=20).place(relx=0.95, rely=.90, anchor=E)

createAccountLabel = Label(createAccountScreen, text="Create an Account", font=('Helvatical bold', 20)).place(relx=0.5, rely=.20, anchor=CENTER)
createUsernameText = tk.Entry(createAccountScreen)
createUsernameText.place(relx=0.5, rely=.4, anchor=CENTER)
createUsernameText.insert(0, 'Username')
createUsernameText.config(foreground='gray')
createPasswordText = tk.Entry(createAccountScreen)
createPasswordText.place(relx=0.5, rely=.5, anchor=CENTER)
createPasswordText.insert(0, 'Password')
createPasswordText.config(foreground='gray')
createEmailText = tk.Entry(createAccountScreen)
createEmailText.place(relx=0.5, rely=.6, anchor=CENTER)
createEmailText.insert(0, 'Email Address')
createEmailText.config(foreground='gray')
initialDepositText = tk.Entry(createAccountScreen)
initialDepositText.place(relx=0.5, rely=.7, anchor=CENTER)
initialDepositText.insert(0, '$0')
initialDepositText.config(foreground='gray')
createAccountButton = Button(createAccountScreen, text="Create Account", height=3, width=20, command = lambda: main.createAccount(createUsernameText.get(), createPasswordText.get(), createEmailText.get(), count,initialDepositText.get(), loginScreen, createAccountScreen, createUsernameText, createPasswordText, createEmailText, initialDepositText)).place(relx=0.5, rely=.8,
                                                                                                    anchor=CENTER)

def usernameCallback(event):
    usernameText.delete(0, END)
    return None


usernameText.bind("<Button-1>", usernameCallback)


def passwordCallback(event):
    passwordText.delete(0, END)
    return None


passwordText.bind("<Button-1>", passwordCallback)

def createUsernameCallback(event):
    createUsernameText.delete(0, END)
    return None


createUsernameText.bind("<Button-1>", createUsernameCallback)

def createPasswordCallback(event):
    createPasswordText.delete(0, END)
    return None


createPasswordText.bind("<Button-1>", createPasswordCallback)

def createEmailCallback(event):
    createEmailText.delete(0, END)
    return None


createEmailText.bind("<Button-1>", createEmailCallback)

def initialDepositCallback(event):
    initialDepositText.delete(0, END)
    return None


initialDepositText.bind("<Button-1>", initialDepositCallback)
root.mainloop()
