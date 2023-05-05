from tkinter import *
import os, csv
from tkinter import ttk

window = Tk()
window.geometry('400x250')
window.resizable(width=False, height=False)
window.config(bg = "#556ee6")
window.title("Database Login")
value = 1

def loginSelected():
    global databaseText
    global usernameText
    global passwordText
    databaseText = b.get()
    usernameText = c.get()
    passwordText = d.get()

    
#Title:
b_text = Label(window, text="Login:", bg = '#556ee6', fg = "black", highlightbackground="Black", font=('Arial',10,"bold"))
b_text.place(x=170, y=0)


#Database Selector
b_text = Label(window, text="Database Name:", bg = '#556ee6', fg = "black", highlightbackground="Black", font=('Arial',10,"bold"))
b_text.place(x=50, y=48)
b = Entry(window, width=25,bg = '#778beb', fg='black', highlightbackground="Black", font=('Arial',10,'bold'))
b.place(x=180, y=50)

#username
c_text = Label(window, text="Username:", bg = '#556ee6', fg = "black", highlightbackground="Black", font=('Arial',10,"bold"))
c_text.place(x=50, y=97)
c = Entry(window, width=25,bg = '#778beb', fg='black', highlightbackground="Black", font=('Arial',10,'bold'))
c.place(x=180, y=100)

#password
d_text = Label(window, text="Password:", bg = '#556ee6', fg = "black", highlightbackground="Black", font=('Arial',10,"bold"))
d_text.place(x=50, y=148)
d = Entry(window, width=25,show="*",bg = '#778beb', fg='black', highlightbackground="Black", font=('Arial',10,'bold'))
d.place(x=180, y=150)

#Login Button
LoginButton = Button(window, text="Login", bg = '#778beb', highlightbackground="Black", font=('Arial',10,'bold'), command=loginSelected)
LoginButton.place(x=180, y=180)

window.mainloop()