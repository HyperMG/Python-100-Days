import tkinter
from tkinter import font

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "Bold"))
my_label.pack(side="left")


my_label.config(text="New Text")