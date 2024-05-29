#Creado por Ricardo Mora y Jordan Segura
#Modulo para calcular huella de carbono

#Importamos biblioteca tkinter
import tkinter as tk
from tkinter import messagebox

#Importamos otras bibliotecas
import os
import pickle

#Definimos una clase para un objeto
class huellaCarros:
    huella_de_carros=[]

    #Método - Constructor
    def __init__(self,nombre,huella):
        self.__nombre=nombre
        self.__huella=huella

    #Método - STR
    def __str__(self):
        return f"""Nombre: {self.__nombre}
        Huella: {self.__huella} CO2"""

    #Métodos - Get's y Set's
    def get_nombre(self):
        return f"{self.__nombre}"
    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    def get_edad(self):
        return f"{self.__huella}"
    def set_edad(self,huella):
        self.__huella=huella

#Clase nueva para manipular archivos
class huellaCarros_Archivo:
    nombre_archivos="huellaCarros.txt"

    @classmethod
    def agregar_huellas(cls,huella_de_carros):
        with open(cls.nombre_archivos,"wb")as archivo:
            pickle.dump(huellaCarros.huella_de_carros,archivo)
            
    @classmethod
    def listar_huellas(cls):
        with open(cls.nombre_archivos,"rb")as archivo:
            huellaCarros.huella_de_carros=pickle.load(archivo)
            mensaje=""
            for huella in huellaCarros.huella_de_carros:
                mensaje+= f"""{huella}\n"""
            messagebox.showinfo("Ver huellas",
                                f"{mensaje}")
    @classmethod
    def cargar_huellas(cls):
        with open(cls.nombre_archivos,"rb")as archivo:
            huellaCarros.huella_de_carros=pickle.load(archivo)

    @classmethod
    def eliminar_huellas(cls):
        os.remove(cls.nombre_archivos)

#Funcion para calcular la huella
def calcular_huella():
    Combustible = txt_combustible.get()
    Combustible = int(Combustible)
    Huella = Combustible/2.40
    
    #Creamos un objeto
    huella=huellaCarros(txt_nombre.get(),Huella)

    #Agregamos el objeto a la lista
    huellaCarros.huella_de_carros.append(huella)

    #Método nuevo para escribir la lista en el archivo
    huellaCarros_Archivo.agregar_huellas(huellaCarros.huella_de_carros)

    messagebox.showinfo("Registro",
                        f"Huella de {txt_nombre.get()} registrada correctamente.")
    txt_nombre.delete(0, tk.END)
    txt_combustible.delete(0, tk.END)

#Funcion para ver las huellas registradas
def ver_huellas():
    huellaCarros_Archivo.listar_huellas()

#Funcion para buscar una huella registrada
def buscar_huella():
    #Guardar el archivo a la lista
    huellaCarros_Archivo.cargar_huellas()
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huellaCarros.huella_de_carros:
        if Nombre == nombre.get_nombre():
            bandera=True
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos encotrado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_combustible.delete(0, tk.END)


#Funcion para eliminar una huella registrada
def eliminar_huella():
    #Guardar el archivo a la lista
    huellaCarros_Archivo.cargar_huellas()
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huellaCarros.huella_de_carros:
        if Nombre == nombre.get_nombre():
            bandera=True
            indice=huellaCarros.huella_de_carros.index(nombre)
            del huellaCarros.huella_de_carros[indice]
            #Guardar la lista a el archivo
            huellaCarros_Archivo.agregar_huellas(huellaCarros.huella_de_carros)
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos eliminado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_combustible.delete(0, tk.END)


#Funcion para la nueva ventana
def huella_carros():
    #Definimos variables globales
    global txt_nombre, txt_combustible
    #Creamos una nueva ventana ventana
    pagina_huellaCarros = tk.Tk()
    pagina_huellaCarros.title("Calcula la huella de tu carro")

    #Creamos el area de trabajo
    area_trabajo = tk.Canvas(pagina_huellaCarros, width=500, height=400, bg="White")
    area_trabajo.pack()

    #Declaramos donde se abrira la pagina al ejecutarse
    pagina_huellaCarros.geometry("480x350+1230+100")

    #Texto diciendo que hace la pagina
    lb_info1=tk.Label(pagina_huellaCarros, text="Aqui puedes calcular la huella de carbono de tu carro.",
                  width=44, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(192,20,window=lb_info1)
    lb_info2=tk.Label(pagina_huellaCarros, text="Solo completa la información necesitada.",
                  width=33, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(150,40,window=lb_info2)

    #Labels y Entry para la informacion necesitada
    lb_info3=tk.Label(pagina_huellaCarros, text="Nombre:",
                  width=13, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(50,100,window=lb_info3)
    txt_nombre=tk.Entry(pagina_huellaCarros, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,100,window=txt_nombre)

    lb_info4=tk.Label(pagina_huellaCarros, text="Cuanto combustible(en litros) ",
                  width=23, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(122,140,window=lb_info4)
    lb_info5=tk.Label(pagina_huellaCarros, text="consume tu carro por kilómetro:",
                  width=26, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(128,160,window=lb_info5)
    txt_combustible=tk.Entry(pagina_huellaCarros, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,150,window=txt_combustible)
    
    #Boton para calcular la huella
    btn_calcular=tk.Button(pagina_huellaCarros, text="Calcular huella", command=calcular_huella,
                           bg="light grey", width=15, height=1, font=("Arial",12))
    area_trabajo.create_window(170,220,window=btn_calcular)

    #Boton para ver los calculos guardados
    btn_ver=tk.Button(pagina_huellaCarros, text="Ver huellas", command=ver_huellas,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,220,window=btn_ver)

    #Boton para buscar un calculo
    btn_buscar=tk.Button(pagina_huellaCarros, text="Buscar huella", command=buscar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,280,window=btn_buscar)

    #Boton para eliminar un calculo
    btn_elimnar=tk.Button(pagina_huellaCarros, text="Eliminar huella", command=eliminar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(170,280,window=btn_elimnar)