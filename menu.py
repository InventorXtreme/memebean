import tkinter
import memebeanupdate
from tkinter import *
import tkinter as tk
import webbrowser
from tkinter import messagebox

ver = memebeanupdate.version
url = "https://memebean--inventorx.repl.co/"


# open update page
def updatelink():
    webbrowser.open(url)
    messagebox.showinfo("Update", "You have version " + ver + "")
def start():
    memebeanupdate.mempkg()

main = tk.Tk()
main.title("Memebean dashboard")

welcome = tk.Label(main, text="Welcome to Membean")
welcome.pack(side=TOP)
launch = Button(main, text="launch memebean", command=start)
launch.pack()
updater = Button(main, text="Check for and install updates", command=updatelink)
updater.pack()


main.mainloop()
