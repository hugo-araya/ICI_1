from tkinter import * 

def mifuncion():
    print('Hola Mundo')
    label1.configure(text = varstr.get())

ventana = Tk()
ventana.title('Primera ventana')
ventana.geometry("400x200")
ventana.configure(background = "#5EFF33")
label1 = Label(ventana,text="Label 1")
label1.pack()
varstr = StringVar()
entrada = Entry(ventana,textvariable = varstr)
entrada.pack()
boton1 = Button(ventana,text="Boton 1", command = mifuncion)
boton1.pack()
ventana.mainloop()
