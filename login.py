from tkinter import *
import sqlite3
import time

def registerclicked():
    window = Tk()
    window.geometry('400x300')
    window.title("Register")

    lblnusrnm = Label(window, text="New Username: ")
    lblnusrnm.place(x=150, y=40)

    lblnpass = Label(window, text="New Password: ")
    lblnpass.place(x=150, y=90)

    lblnpassc = Label(window, text="Confirm Password: ")
    lblnpassc.place(x=142, y=140)

    lblregister = Label(window, text="Please Register")
    lblregister.place(x=150, y=10)

    textnusrnm = Entry(window, width=10)
    textnusrnm.place(x=150, y=60)

    textnpass = Entry(window, width=10, show='*')
    textnpass.place(x=150, y=110)

    textnpassc = Entry(window, width=10, show='*')
    textnpassc.place(x=150, y=160)

    def registerusr(username, password):
        if textnpass.get() == textnpassc.get():
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            lblregister.configure(text="Register Succses")
        else:
            lblregister.configure(text="Pass Do Not Match")

    btnregistern = Button(window, text="Register", command=lambda: registerusr(textnusrnm.get(), textnpass.get()))
    btnregistern.place(x=157, y=190)

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()
conn.close()

window = Tk()
window.geometry('400x300')
window.title("Login")

lblusrnm = Label(window, text="Username: ")
lblusrnm.place(x=165, y=40)

lblpass = Label(window, text="Password: ")
lblpass.place(x=165, y=90)

lbldef = Label(window, text="Please Login")
lbldef.place(x=160, y=10)

textusrnm = Entry(window,width=10)
textusrnm.place(x=150, y=60)

textpass = Entry(window,width=10, show='*')
textpass.place(x=150, y=110)

def loginlicked():
    username = textusrnm.get()
    password = textpass.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        lbldef.configure(text="Login Succes")
    else:
        lbldef.configure(text="User Do Not Found")


btnlogin = Button(window, text="Login", command=loginlicked)
btnlogin.place(x=125, y=140)

btnregister = Button(window, text="Register", command=registerclicked)
btnregister.place(x=195, y=140)

window.mainloop()
