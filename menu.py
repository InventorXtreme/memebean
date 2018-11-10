import tkinter
import memebeanupdate
import shoutabout
from tkinter import *
import tkinter as tk
import webbrowser
from tkinter import messagebox

ver = memebeanupdate.version
url = "https://github.com/InventorXtreme/memebean"


# open update page
def updatelink():
    webbrowser.open(url)
    messagebox.showinfo("Update", "You have version " + ver + "")
def start():
    memebeanupdate.mempkg()
def shouta():
    shoutabout.thing()

main = tk.Tk()
main.title("Memebean dashboard")

welcome = tk.Label(main, text="Welcome to Membean")
welcome.pack(side=TOP)
launch = Button(main, text="Launch Memebean", command=start)
launch.pack()
shout = Button(main, text="Shoutouts", command=shouta)
shout.pack()
updater = Button(main, text="Check for and Install Updates", command=updatelink)
updater.pack()


main.mainloop()
