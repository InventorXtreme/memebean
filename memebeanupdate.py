
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

global version
version = "0"
def mempkg():
    global blockliste
    blocklist = 0
    global tbcm
    tbcm = 0
    global outcode
    outcode = 0
    global qplaye
    qplaye = 0
    global qcor
    qcor = 0


    def gets():
        global qcor
        global qplaye
        global outcode
        global tbcm
        if tbcm == 1:
            outcode = outcode + 1

        qplayer = qplaye - 1
        qcout = str(qcor)
        qpo = str(qplayer)
        messagebox.showinfo("Results", "" + qcout + " out of " + qpo + "")


    def c():
        global qcor
        qcor = qcor + 1
        print("c")
        nxtf()


    def i():
        print("i")
        nxtf()


    def que(q, ans):
        global qplaye
        qplaye = qplaye + 1

        questionl.config(text=q)

        anspos(ans)


    def anspos(anstxt):
        pos = random.randint(1, 4)
        ml = ["illuminati", "dogo", "Doge", "somebody one told me", "To be continued", "Vines"]
        ml.append("Moth")
        oI = random.choice(ml)
        if oI == anstxt:
            oI = "blank"

        o2 = random.choice(ml)
        if o2 == anstxt:
            o2 = "blank"

        o3 = random.choice(ml)
        if o3 == anstxt:
            o3 = "blank"

        if pos == 1:
            but1.config(text=anstxt, command=c)
            but2.config(text=oI, command=i)
            but3.config(text=o2, command=i)
            but4.config(text=o3, command=i)
        if pos == 2:
            but2.config(text=anstxt, command=c)
            but1.config(text=oI, command=i)
            but3.config(text=o2, command=i)
            but4.config(text=o3, command=i)
        if pos == 3:
            but3.config(text=anstxt, command=c)
            but1.config(text=oI, command=i)
            but2.config(text=o2, command=i)
            but4.config(text=o3, command=i)
        if pos == 4:
            but4.config(text=anstxt, command=c)
            but3.config(text=oI, command=i)
            but2.config(text=o2, command=i)
            but1.config(text=o3, command=i)


    def get():
        global tcbm
        global blockliste
        #blockliste = blocklist.get()
        #print(blockliste)
        #if blockliste[0] == "1":
            #tcbm = 1
        #menu.pack()
        #login.pack_forget()


    def practice():
        menu.pack_forget()
        practicef.pack()


    def imdone():
        global qcor
        global qplaye
        global outcode
        global tbcm
        if tbcm == 1:
            outcode = outcode + 1

        qplayer = qplaye - 1
        qcout = str(qcor)
        qpo = str(qplayer)
        messagebox.showinfo("Results", "" + qcout + " out of " + qpo + "")
        root.destroy()


    root = tk.Tk()

    #login = Frame(root)
    #login.pack()

    # request block need list

    #titlelbl = tk.Label(login, text="Enter ID CODE 1 if you do not have a code type 0")
    #titlelbl.pack(side=tk.TOP)

    #blocklist = Entry(login, bd=4, width=50)
    #blocklist.pack(side=tk.TOP)

    #ok = Button(login, text="OK", command=get)
    #ok.pack()

    menu = Frame(root)
    menu.pack()



    # dont use in showcase/update vids
    # lgo = PhotoImage(file="logo.gif")

    # lg = tk.Label(menu, image=lgo)
    # lg.pack()

    menuchose = tk.Label(menu, text="chose an option:")
    menuchose.pack()

    practice = Button(menu, text="Practice", command=practice)
    practice.pack()

    practicef = Frame(root)


    def nxtf():
        pm = -1

        question = random.randint(0, 6)
        if question == pm:
            question = random.randint(0, 6)

        if question == 0:
            que("this meme has a triangle in it", "illuminati")
            pm = 0
        if question == 1:
            que("This memes includes the song roundabout", "To be continued")
            pm = 1
        if question == 2:
            que("Fill in the blank. Gabe the _____.", "dogo")
            pm = 2
        if question == 3:
            que("This meme includes odd, sarcstic sayings with bad grammer written in comic sans EX:Such meme.", "Doge")
            pm = 3
        if question == 4:
            que("This meme frome the movie shreck has the opening lyrics of ______", "somebody one told me")
            pm = 4
        if question == 5:
            que("This meme is a very popular subset of memes and has its own subsets", "Vines")
        if question == 6:
            que("This dead meme features a _____", "Moth")
        #if question == 7:
            


    questionl = tk.Label(practicef, text="loading")
    questionl.pack()

    toolbar = Frame(practicef, relief="raised", borderwidth=2, width=400, height=30)
    toolbar.pack(side=tk.TOP)
    toolbar.pack_propagate(0)

    imdone = Button(toolbar, text="I'm done", command=imdone)
    imdone.pack(side=tk.LEFT, anchor=E)

    score = Button(toolbar, text="See your score", command=gets)
    score.pack(anchor=N, side=tk.RIGHT)

    but1 = Button(practicef, text="loading...")
    but1.pack()

    but2 = Button(practicef, text="loading...")
    but2.pack()

    but3 = Button(practicef, text="loading...")
    but3.pack()

    but4 = Button(practicef, text="loading...")
    but4.pack()

    nxt = Button(practicef, text="NEXT", command=nxtf)
    nxt.pack()

    root.mainloop()

