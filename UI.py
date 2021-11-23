import main
from tkinter import *
import tkinter as tk

# count variable and initial tkinter gui initizialization
count = 0
root = Tk()

# screens created using frames
loginScreen = tk.Frame(root)
createAccountScreen = tk.Frame(root)
welcomeScreen = tk.Frame(root)
depositScreen = tk.Frame(root)
withdrawScreen = tk.Frame(root)

# screen size set
root.geometry("600x600")

# login screen gui variables and functions stated here
loginScreen.pack(fill='both', expand=1)
ATMLabel = tk.Label(loginScreen, text="ATM", font=('Helvatical bold', 20)).place(relx=0.5, rely=.1, anchor=CENTER)
usernameText = tk.Entry(loginScreen)
usernameText.place(relx=0.5, rely=.3, anchor=CENTER)
usernameText.insert(0, 'Username')
usernameText.config(foreground='gray')
passwordText = tk.Entry(loginScreen)
passwordText.place(relx=0.5, rely=.4, anchor=CENTER)
passwordText.insert(0, 'Password')
passwordText.config(foreground='gray')
loginButton = Button(loginScreen, text="Login", height=3, width=20, command=lambda: main.login(usernameText.get(), passwordText.get(), loginScreen, welcomeScreen, balanceLabel)).place(relx=0.5, rely=.6, anchor=CENTER)
createButton = Button(loginScreen, text="Create an Account", height=3, width=20, command=lambda: main.createScreen(1, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen)).place(relx=0.5, rely=.8,
                                                                                                    anchor=CENTER)
balanceLabel = Label(welcomeScreen, text='', font=('Helvatical bold', 30), fg='green')
balanceLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
loginScreen.pack(fill='both', expand=1)

# welcome screen buttons and labels
companyLabel = Label(welcomeScreen, text="One Touch", font=('Helvatical bold', 15)).place(relx=0, rely=0.05, anchor=W)
depositButton = Button(welcomeScreen, text="Deposit", height=3, width=20, command=lambda: main.createScreen(2, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen)).place(relx=0.05, rely=.90, anchor=W)
withdrawButton = Button(welcomeScreen, text="Withdraw", height=3, width=20, command=lambda: main.createScreen(4, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen)).place(relx=0.95, rely=.90, anchor=E)

# create new account screen with labels, text boxes, and button
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
createAccountButton = Button(createAccountScreen, text="Create Account", height=3, width=20, command = lambda: main.createAccount(createUsernameText.get(), createPasswordText.get(), createEmailText.get(), count, initialDepositText.get(), loginScreen, createAccountScreen, createUsernameText, createPasswordText, createEmailText, initialDepositText)).place(relx=0.5, rely=.8,
                                                                                                    anchor=CENTER)

dAmountText = Label(depositScreen, text="Deposit:", font=('Helvatical bold', 15)).place(relx=.5, rely=0.1, anchor=CENTER)
d5Button = Button(depositScreen, text="$5", height=3, width=20, command=lambda: main.deposit(5, welcomeScreen, dCustomEntry, balanceLabel)).place(relx=0.20, rely=.25, anchor=CENTER)
d10Button = Button(depositScreen, text="$10", height=3, width=20, command=lambda: main.deposit(10, welcomeScreen, dCustomEntry, balanceLabel)).place(relx=0.50, rely=.25, anchor=CENTER)
d25Button = Button(depositScreen, text="$25", height=3, width=20, command=lambda: main.deposit(25, welcomeScreen, dCustomEntry, balanceLabel)).place(relx=0.80, rely=.25, anchor=CENTER)
d50Button = Button(depositScreen, text="$50", height=3, width=20, command=lambda: main.deposit(50, welcomeScreen, dCustomEntry, balanceLabel)).place(relx=0.33, rely=.5, anchor=CENTER)
d100Button = Button(depositScreen, text="$100", height=3, width=20, command=lambda: main.deposit(100, welcomeScreen, dCustomEntry, balanceLabel)).place(relx=0.66, rely=.5, anchor=CENTER)
dCustomButton = Button(depositScreen, text="Custom Amount", height=3, width=20, command=lambda: main.deposit(0, welcomeScreen, dCustomEntry, balanceLabel)).place(relx=0.33, rely=.75, anchor=CENTER)
dCustomEntry = tk.Entry(depositScreen)
dCustomEntry.place(relx=0.66, rely=0.75, anchor=CENTER)
dCustomEntry.insert(0, '$0')
dCustomEntry.config(foreground='gray')
dReturnButton = Button(depositScreen, text="Back", height=2, width=10, command=lambda: main.createScreen(3, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen)).place(relx=0, rely=0)

wAmountText = Label(withdrawScreen, text="Withdraw:", font=('Helvatical bold', 15)).place(relx=.5, rely=0.1, anchor=CENTER)
w5Button = Button(withdrawScreen, text="$5", height=3, width=20, command=lambda: main.withdraw(5, welcomeScreen, wCustomEntry, balanceLabel)).place(relx=0.20, rely=.25, anchor=CENTER)
w10Button = Button(withdrawScreen, text="$10", height=3, width=20, command=lambda: main.withdraw(10, welcomeScreen, wCustomEntry, balanceLabel)).place(relx=0.50, rely=.25, anchor=CENTER)
w25Button = Button(withdrawScreen, text="$25", height=3, width=20, command=lambda: main.withdraw(25, welcomeScreen, wCustomEntry, balanceLabel)).place(relx=0.80, rely=.25, anchor=CENTER)
w50Button = Button(withdrawScreen, text="$50", height=3, width=20, command=lambda: main.withdraw(50, welcomeScreen, wCustomEntry, balanceLabel)).place(relx=0.33, rely=.5, anchor=CENTER)
w100Button = Button(withdrawScreen, text="$100", height=3, width=20, command=lambda: main.withdraw(100, welcomeScreen, wCustomEntry, balanceLabel)).place(relx=0.66, rely=.5, anchor=CENTER)
wCustomButton = Button(withdrawScreen, text="Custom Amount", height=3, width=20, command=lambda: main.withdraw(0, welcomeScreen, wCustomEntry, balanceLabel)).place(relx=0.33, rely=.75, anchor=CENTER)
wCustomEntry = tk.Entry(withdrawScreen)
wCustomEntry.place(relx=0.66, rely=0.75, anchor=CENTER)
wCustomEntry.insert(0, '$0')
wCustomEntry.config(foreground='gray')
wReturnButton = Button(withdrawScreen, text="Back", height=2, width=10, command=lambda: main.createScreen(5, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen)).place(relx=0, rely=0)
# all following functions are used to clear the text within the box once clicked on (ex. gray text for "password"
# within box is removed once box is clicked)
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

def dcustomCallback(event):
    dCustomEntry.delete(0, END)
    return None


dCustomEntry.bind("<Button-1>", dcustomCallback)
root.mainloop()
