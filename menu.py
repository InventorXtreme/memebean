import tkinter
import memebeanupdate
import shoutabout
from tkinter import *
import tkinter as tk
import webbrowser
from tkinter import messagebox

ver = memebeanupdate.version
url = "https://github.com/InventorXtreme/memebean"
def load(memepak):
    #try:
    mpkg = __import__(memepak)
    TY = mpkg.TYPE


    if(TY == "NGUI"):
        nw = tk.Tk()
        nwwidget = mpkg.gui(nw)
        nw.mainloop()
    elif(TY == "AGUI"):
        AGUIW = mpkg.gui(main2)
    else:
        secure = messagebox.askquestion("Error", "This Pak does not have a PakType, Allow it to run?")
        if secure == "yes":
            print("g")
        mpkg.run()
#except:
        #print(memepak)
        #messagebox.showerror("Error", "Memepack not found")
# open update page
def updatelink():
    webbrowser.open(url)
    messagebox.showinfo("Update", "You have version " + ver + "")
def start():
    memebeanupdate.mempkg()
def shouta():
    shoutabout.thing()
def loadb():
    global exide
    impkg = exide.get()
    load(impkg)

#def le()
def loaderwin():
    global exide
    global main2
    main2 = tk.Tk()
    exide = Entry(main2)
    exide.pack()
    loada = Button(main2, text="Load MemePak", command=loadb)
    loada.pack()

main = tk.Tk()
main.title("Memebean dashboard")

welcome = tk.Label(main, text="Welcome to Memebean")
welcome.pack(side=TOP)
launch = Button(main, text="Launch Memebean", command=start)
launch.pack()
shout = Button(main, text="Shoutouts", command=shouta)
shout.pack()
updater = Button(main, text="Check for and Install Updates", command=updatelink)
updater.pack()
#load MemePak Gui
mpkgui = Button(main, text="MemePak Manager", command=loaderwin)
mpkgui.pack()


main.mainloop()
