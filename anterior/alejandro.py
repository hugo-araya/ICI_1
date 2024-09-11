#Importamos la libreria Tkinter como se menciona en "Desarrollo de interfaces gráficas con Tkinter.docx"
from tkinter import *

def comprobar(l1, l2, l3):
        lado1 = float(l1.get())
        lado2 = float(l2.get())
        lado3 = float(l3.get())
        
        #Comprobamos que se trate de un triangulo construible de la manera en la que se menciona en el documento
        if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
            #Si se cumple la condicion identificaremos de que triangulo se trata con una funcion y este sera el resultado que se mostrara en el label de resultado
            resultado_identificar = identificar(lado1, lado2, lado3)
            resultado.config(text = (f"El triango es: {resultado_identificar}"))
        else:
            #si no entonces no es un triangulo construible
            resultado.config(text = "No es un triangulo")

#Funcion para la interfaz grafica Tkinter 
def interfaztkinter():
    # Creamos la ventana principal y definimos sus parametros
    ventana = Tk()
    ventana.title("Clasificacion de triangulos")
    ventana.geometry("500x400")

    #Creamos un label y un entry para cada lado del triangulo y lo mandamos a la ventana con el metodo pack()
    #Nota del autor: Al ser mi primera vez usando tkinter deje un espacio entre cada uno de ellos para mejor organizacion 
    lado1text = Label(ventana, text = ("Ingrese la medida del lado 1"))
    l1 = Entry(ventana, textvariable = StringVar)
    lado1text.pack()
    l1.pack()

    lado2text = Label(ventana, text = ("Ingrese la medida del lado 2"))
    l2 = Entry(ventana, textvariable = StringVar)
    lado2text.pack()
    l2.pack()

    lado3text = Label(ventana, text = ("Ingrese la medida del lado 3"))
    l3 = Entry(ventana, textvariable = StringVar)
    lado3text.pack()
    l3.pack()
    boton = Button(ventana,text = ("Identificar") ,command = comprobar(l1, l2, l3))
    boton.pack()
            
    #Creamos un label para que nos muestre el resultado 
    resultado = Label(ventana, text = "")
    resultado.pack()
    ventana.mainloop()

    #obtenemos los lados del triangulo los transformamos a float para poder trabajar con decimilaes en caso de que sea necesario

    
    #Usamos una funcion para identificar el tipo de triangulo

def identificar(lado1, lado2, lado3):
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 != lado2 != lado3:
            return "Escaleno"
        else:
            return "Isósceles"
        

if __name__=="__main__":
    interfaztkinter()