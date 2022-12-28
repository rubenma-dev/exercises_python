from tkinter import * 

vtn = Tk()
vtn.title("Calculadora")
vtn.geometry('235x150')
vtn.configure(background='black')

def suma():
    suma = int(txt1.get())+int(txt2.get())
    return resultado.set(suma)
def resta():
    resta = int(txt1.get())-int(txt2.get())
    return resultado.set(resta)
def multi():
    multi = int(txt1.get())*int(txt2.get())
    return resultado.set(multi)
def division():
    division = int(txt1.get())/int(txt2.get())
    return resultado.set(division)
def cerrar():
    vtn.destroy()
resultado=StringVar()

lbl1 = Label(vtn, text="Calculadora", bg='black', fg='white')
lbl1.grid(row=1, column=1)

lbl2 = Label(vtn,text="Primer Numero", bg='black', fg='white')
lbl2.grid(row=2,column=1)
txt1 = Entry(vtn)
txt1.grid(row=2,column=2)

lbl3 = Label(vtn,text="Segundo Numero", bg='black', fg='white')
lbl3.grid(row=3,column=1)
txt2 = Entry(vtn)
txt2.grid(row=3,column=2)

btnSuma = Button(vtn, text="Suma", bg='white', fg='black', width=11, command=suma)
btnSuma.grid(row=4,column=1)

btnResta = Button(vtn, text="Resta", bg='white', fg='black', width=11, command=resta)
btnResta.grid(row=4,column=2)

btnMulti = Button(vtn, text="Multiplicacion", bg='white', fg='black', width=11, command=multi)
btnMulti.grid(row=5,column=1)

btnDivision = Button(vtn, text="Division", bg='white', fg='black', width=11, command=division)
btnDivision.grid(row=5,column=2)

btnCerrar = Button(vtn, text="Cerrar", bg='red', fg='white', width=30, command=cerrar)
btnCerrar.grid(row=6,column=1, columnspan=2)

lblRes = Label(vtn, bg='white', width=10, textvariable=resultado)
lblRes.grid(row=7, column=1, columnspan=2)
vtn.mainloop()