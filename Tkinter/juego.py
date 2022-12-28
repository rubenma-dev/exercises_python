from tkinter import *
import tkinter as tk
import random

# FUNCIONES

def numeroaleatorio():
    global numal
    numal=random.randint(1,100)
    return numal

def ingresar(a,b):
    if a > b:
        return r.set("El numero ingresado es mayor que el digito secreto")
    if a < b:
        return r.set("El numero ingresado es menor que el digito secreto")
    if a == b:
        return r.set("Has encontrado el numero secreto.")

def juego():
    x=int(entry.get())
    rand=numal
    ingresar(x,rand)

# INTERFAZ

ventana = Tk()
ventana.geometry('300x160')
ventana.title ('Adivina mi numero')
ventana.configure(background= 'azure4')

# VARIABLES

r = StringVar()
numal=IntVar()

# LABELS

label = Label(ventana, text = 'Ingrese su numero entre 1 y 100')
label.pack(anchor = NW)
label.place(x = 10, y = 10)
label.config(fg = 'snow', bg = 'azure4', font = ('Bodoni, 15'))

dialogo = Label(ventana, textvariable = r)
dialogo.place(x = 10, y = 130)
dialogo.config(fg = 'red4', bg = 'azure4')

# ENTRY

entry = Entry(ventana)
entry.pack(anchor = NW)
entry.place(x = 10, y = 40)

# BOTONES

comenzar = tk.Button(ventana, text = 'Iniciar Juego', command = numeroaleatorio)
comenzar.place(x = 20, y = 80)

ingresarNum = tk.Button(ventana, text = 'Ingresar', command = juego)
ingresarNum.place(x = 140, y = 80)

# BUCLE

ventana.mainloop()