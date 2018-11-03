import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

global version
version = "1.0.0"
def mempkg():
    global pm
    pm = -1
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
    global quiz
    quiz = 0
    global iftest
    iftest = -1

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
        #print("c")
        nxtf()


    def i():
        #print("i")
        nxtf()


    def que(q, ans):
        global qplaye
        qplaye = qplaye + 1

        questionl.config(text=q)

        anspos(ans)


    def anspos(anstxt):
        pos = random.randint(1, 4)
        ml = ["Illuminati", "Dogo", "Doge", "Somebody Once Told Me", "To be Continued", "Vines"]
        ml.append("Moth")
        ml.append("Spaget")
        ml.append("Wii Sports")
        ml.append("Sandwich")
        ml.append("Oof")
        ml.append("LeBron James")
        ml.append("Anime")
        ml.append("Johnny Johnny, Yes Papa")
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

    def test():
        global iftest
        menu.pack_forget()
        practicef.pack()
        iftest = 1


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

    testbutton = Button(menu, text="Test", command=test)
    testbutton.pack()

    practicef = Frame(root)

    
    
    def nxtf():
        global pm
        global qcor
        global qplayer
        global quiz
        global iftest
        if iftest == 1:
            quiz = quiz + 1

            if quiz == 21:
                if qcor == 20 or qcor == 19:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" + "\nYou are a Dank Memer!")
                if qcor == 18 or qcor == 17:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" + "\nYou are a Memer!")
                if qcor == 16 or qcor == 15:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" + "\nYou're not bad.")
                if qcor == 14 or qcor == 13:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" + "\nYou are a Novice Memer.")
                if qcor == 12 or qcor == 11:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" +  "\nYou're not great.")
                if qcor == 10 or qcor == 9:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" + "\nYou're sad.")
                if qcor == 8 or qcor == 7 or qcor == 6 or qcor == 5 or qcor == 4 or qcor == 3 or qcor == 2 or qcor == 1 or qcor == 0:
                    messagebox.showinfo("Results", "" + str(qcor) + " out of 20" + "\nYou're a grandma who still doesn't know what the internet is.")

        question = random.randint(0, 12)
        if question == pm:
            question = random.randint(0, 12)

        if question == 0:
            que("This meme has a triangle in it", "Illuminati")
            pm = 0
        if question == 1:
            que("This memes includes the song roundabout", "To be Continued")
            pm = 1
        if question == 2:
            que("Fill in the blank. Gabe the _____.", "Dogo")
            pm = 2
        if question == 3:
            que("This meme includes odd, sarcstic sayings with bad grammer written in comic sans EX:Such meme.", "Doge")
            pm = 3
        if question == 4:
            que("This meme frome the movie shreck has the opening lyrics of ______", "Somebody Once Told Me")
            pm = 4
        if question == 5:
            que("This meme is a very popular subset of memes and has its own subsets", "Vines")
            pm = 5
        if question == 6:
            #Meme sugested by JoeBiz
            que("This dead meme features a _____", "Moth")
            pm = 6
        if question == 7:
            que("What was touched in the Three Little Bears animation", "Spaget")
            pm = 7
        if question == 8:
            que("What is the famous video game made by Nintendo for the Wii", "Wii Sports")
            pm = 8
        if question == 9:
            que("Sorry I fell asleep while I was waiting on you to make me a _____", "Sandwich")
            pm = 9
        if question == 10:
            que("This meme ofiginated form Roblox", "Oof")
            pm = 10
        if question == 11:
            que("A kid says a famous basketball player's name over and over", "LeBron James")
        if question == 12:
            que("I have the power of God and _____ ond my side", "Anime")
        if question == 13:
            que("This meme has a kid eating sugar", "Johnny Johnny, Yes Papa")
        

        


    questionl = tk.Label(practicef, text="Loading, press next to start")
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
