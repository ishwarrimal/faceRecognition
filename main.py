from tkinter import *

import os

import sys

from PIL import Image, ImageTk

window=Tk()

window.title("Enter Details")

window.configure(bg="#D7CCC8")

window.focus_set()

def enter_the_value():

    name=e1.get()

    print(name)

    os.system("python captureFace.py "+name)

    window.destroy()

if __name__=="__main__":

    Label(window,text="ENTER THE DETAILS", fg='white', bg='#424242' ,font=("helvetica",40),width=23).grid(rowspan=2,columnspan=3,sticky=E+W+N+S,padx=5,pady=5)

    Label(window, text="Enter Student Name: ",font=("helvetica ",30),fg='#212121',bg="#D7CCC8").grid(row=2,sticky=E,column=0)

    e1=Entry(window)

    e1.grid(row=2,column=1,columnspan=2,sticky=W)

    # enter=PhotoImage(file="enter.gif")

    # clear=PhotoImage(file="clear.gif")

    Button(window,text="CLEAR",font=("times new roman",30), fg="red",bg="#3E2723",command=window.quit).grid(row=4,column=0, pady=10,padx=10,sticky=E+W+N+S)

    Button(window,text="ENTER",font=("times new roman",30), fg="black",bg="#3E2723",command=enter_the_value).grid(row=4,column=1,pady=10,padx=10,sticky=E+W+N+S)

window.mainloop()