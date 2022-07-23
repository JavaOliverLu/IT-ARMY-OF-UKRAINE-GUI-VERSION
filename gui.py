import os
from tkinter import *
import webbrowser
import sys
import subprocess
from tkinter.scrolledtext import ScrolledText
def load():
    os.system("python -m pip install -r requirements.txt")
    with open("./movies.txt") as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def callback(url):
    webbrowser.open_new(url)
def save():
    with open(r"./movies.txt", 'w') as file:
        file.write(contents.get('1.0', END))
    os.system("python runner.py -c movies.txt")
top = Tk()
top. title("IT ARMY OF UKRAINE GUI")
contents = ScrolledText()
contents.pack(side=TOP, expand=True, fill=BOTH)
filename = Entry()
load()
link1 = Label(top, text="Go to the headquarter to get the link", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://t.me/s/itarmyofukraine2022"))

Button(text='ATTACK', fg="red", command=save).pack(side=BOTTOM, expand=True, fill=BOTH)
mainloop()