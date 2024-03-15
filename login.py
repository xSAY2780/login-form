from tkinter import *
import sqlite3

def registerclicked():
    windowlogin.destroy()
    
    def registerusr(username, password):
        if textnpass.get() == textnpassc.get() and textnpass.get() != "" and textnusrnm.get() != "":
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            lblregister.configure(text="Register Success")
        elif textnpass.get() != "" and textnpassc.get() != "" and textnusrnm.get() == "":
            lblregister.configure(text="Please Enter Username")
        elif textnpass.get() != "" and textnusrnm.get() == "":
            lblregister.configure(text="Please Enter Username")
        elif textnusrnm.get() != "" and textnpass.get() != "" and textnpassc.get() == "":
            lblregister.configure(text="Please Confirm Pass")
        elif textnpassc.get() != textnpass.get():
            lblregister.configure(text="Pass Do Not Match")
        elif textnusrnm.get() != "":
            lblregister.configure(text="Please Enter Pass")
    
    global windowregister

    windowregister = Tk()
    windowregister.geometry('400x300')
    windowregister.title("Register")

    lblnusrnm = Label(windowregister, text="New Username: ")
    lblnusrnm.place(x=150, y=40)

    lblnpass = Label(windowregister, text="New Password: ")
    lblnpass.place(x=150, y=90)

    lblnpassc = Label(windowregister, text="Confirm Password: ")
    lblnpassc.place(x=142, y=140)

    lblregister = Label(windowregister, text="Please Register")
    lblregister.place(x=150, y=10)

    textnusrnm = Entry(windowregister, width=10)
    textnusrnm.place(x=150, y=60)

    textnpass = Entry(windowregister, width=10, show='*')
    textnpass.place(x=150, y=110)

    textnpassc = Entry(windowregister, width=10, show='*')
    textnpassc.place(x=150, y=160)

    btnregistern = Button(windowregister, text="Register", command=lambda: registerusr(textnusrnm.get(), textnpass.get()))
    btnregistern.place(x=157, y=190)

    btnrlogin = Button(windowregister, text="Login", command=lambda: [windowregister.destroy(), login_window()])
    btnrlogin.place(x=165, y=220)

def setup_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

#Main Login Window
def login_window():

    global windowlogin

    windowlogin = Tk()
    windowlogin.geometry('400x300')
    windowlogin.title("Login")

    lblusrnm = Label(windowlogin, text="Username: ")
    lblusrnm.place(x=165, y=40)

    lblpass = Label(windowlogin, text="Password: ")
    lblpass.place(x=165, y=90)

    lbldef = Label(windowlogin, text="Please Login")
    lbldef.place(x=160, y=10)

    textusrnm = Entry(windowlogin,width=10)
    textusrnm.place(x=150, y=60)

    textpass = Entry(windowlogin,width=10, show='*')
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
            windowlogin.destroy()
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
            uid = cursor.fetchone()[0]
            conn.close()

            global windowmain

            windowmain = Tk()
            windowmain.geometry('400x300')
            windowmain.title("What Is My User Id")

            lbluid = Label(windowmain, text="")
            lbluid.place(x=14, y=145)

            btnusrid = Button(windowmain, text="What Is My UserID", command=lambda: lbluid.configure(text=f"Your UserID Is {uid}"))
            btnusrid.place(x=125, y=115)
                
        else:
            lbldef.configure(text="User Not Found")

    btnlogin = Button(windowlogin, text="Login", command=loginlicked)
    btnlogin.place(x=125, y=140)

    btnregister = Button(windowlogin, text="Register", command=lambda: registerclicked())
    btnregister.place(x=195, y=140)

    windowlogin.mainloop()


setup_db()
login_window()
