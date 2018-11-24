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
    #MEMEPAK API/LOADER
    try:
        #import Pak
        mpkg = __import__(memepak)
        TY = mpkg.TYPE


        if(TY == "NGUI"):

            #Create new GUI and load PakWidget
            nw = tk.Tk()
            nw.title(memepak)
            nwwidget = mpkg.gui(nw)
            nw.mainloop()
        elif(TY == "AGUI"):
            #add widget to current GUI
            AGUIW = mpkg.gui(main2)
        elif(TY == "SCRIPT"):
            #run the script
            mpkg.run()
        else:
            #SECURITY CHECK
            secure = messagebox.askquestion("Error", "This Pak does not have a PakType, Allow it to run?")
            if secure == "yes":
                #run script
                mpkg.run()
    except ModuleNotFoundError:
        messagebox.showerror("Error", "Memepack not found")
    except ValueError:
        messagebox.showerror("Error", "You cant load a MemePak with no name")
# open update page
def updatelink():
    webbrowser.open(url)
    messagebox.showinfo("Update", "You have version " + ver + "")
def start():
    memebeanupdate.mempkg()
def shouta():
    shoutabout.thing()
def loadb(a):
    global exide
    impkg = exide.get()
    load(impkg)
    a2 = a


#def le()
def loaderwin():
    global exide
    global main2
    main2 = tk.Tk()
    exide = Entry(main2)
    exide.pack()
    loada = Button(main2, text="Load MemePak", command=loadb)
    loada.pack()
    main2.bind("<Return>", loadb)

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
