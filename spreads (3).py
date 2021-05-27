from tkinter import *
import tkinter as tk
window =tk.Tk()

def getvalue():
    print(mystring.get())
    global motivo
    motivo = mystring.get()

mystring =tk.StringVar(window)
e1 = Entry(window,textvariable = mystring,width=100,fg="blue",bd=3,selectbackground='violet').pack()
button1 = tk.Button(window,width = 10, text = "Enviar", command=getvalue).pack()

window.mainloop()