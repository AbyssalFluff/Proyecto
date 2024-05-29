#Creado por Ricardo Mora y Jordan Segura
#Modulo para calcular huella de carbono

#Importamos biblioteca tkinter
import tkinter as tk
from tkinter import messagebox

#Importamos otras bibliotecas
import os
import pickle

#Definimos una clase para un objeto
class huellaAgua:
    huella_de_agua=[]

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
class huellaAgua_Archivo:
    nombre_archivos="huellaAgua.txt"

    @classmethod
    def agregar_huellas(cls,huella_de_agua):
        with open(cls.nombre_archivos,"wb")as archivo:
            pickle.dump(huellaAgua.huella_de_agua,archivo)
            
    @classmethod
    def listar_huellas(cls):
        with open(cls.nombre_archivos,"rb")as archivo:
            huellaAgua.huella_de_agua=pickle.load(archivo)
            mensaje=""
            for huella in huellaAgua.huella_de_agua:
                mensaje+= f"""{huella}\n"""
            messagebox.showinfo("Ver huellas",
                                f"{mensaje}")
    @classmethod
    def cargar_huellas(cls):
        with open(cls.nombre_archivos,"rb")as archivo:
            huellaAgua.huella_de_agua=pickle.load(archivo)

    @classmethod
    def eliminar_huellas(cls):
        os.remove(cls.nombre_archivos)

#Funcion para calcular la huella
def calcular_huella():
    Agua = txt_agua.get()
    Agua = int(Agua)
    Huella = Agua*0.40

    #Creamos un objeto
    huella=huellaAgua(txt_nombre.get(),Huella)

    #Agregamos el objeto a la lista
    huellaAgua.huella_de_agua.append(huella)

    #Método nuevo para escribir la lista en el archivo
    huellaAgua_Archivo.agregar_huellas(huellaAgua.huella_de_agua)

    messagebox.showinfo("Registro",
                        f"Huella de {txt_nombre.get()} registrada correctamente.")
    txt_nombre.delete(0, tk.END)
    txt_agua.delete(0, tk.END)

#Funcion para ver las huellas registradas
def ver_huellas():
    huellaAgua_Archivo.listar_huellas()

#Funcion para buscar una huella registrada
def buscar_huella():
    #Guardar el archivo a la lista
    huellaAgua_Archivo.cargar_huellas()
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huellaAgua.huella_de_agua:
        if Nombre == nombre.get_nombre():
            bandera=True
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos encotrado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_agua.delete(0, tk.END)


#Funcion para eliminar una huella registrada
def eliminar_huella():
    #Guardar el archivo a la lista
    huellaAgua_Archivo.cargar_huellas()
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huellaAgua.huella_de_agua:
        if Nombre == nombre.get_nombre():
            bandera=True
            indice=huellaAgua.huella_de_agua.index(nombre)
            del huellaAgua.huella_de_agua[indice]
            #Guardar la lista a el archivo
            huellaAgua_Archivo.agregar_huellas(huellaAgua.huella_de_agua)
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos eliminado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_agua.delete(0, tk.END)


#Funcion para la nueva ventana
def huella_agua():
    #Definimos variables globales
    global txt_nombre, txt_agua
    #Creamos una nueva ventana ventana
    pagina_huellaAgua = tk.Tk()
    pagina_huellaAgua.title("Calcula la huella del agua")

    #Creamos el area de trabajo
    area_trabajo = tk.Canvas(pagina_huellaAgua, width=500, height=400, bg="White")
    area_trabajo.pack()

    #Declaramos donde se abrira la pagina al ejecutarse
    pagina_huellaAgua.geometry("480x350+1230+100")

    #Texto diciendo que hace la pagina
    lb_info1=tk.Label(pagina_huellaAgua, text="Aqui puedes calcular la huella de carbono del uso de agua.",
                  width=46, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(208,20,window=lb_info1)
    lb_info2=tk.Label(pagina_huellaAgua, text="Solo completa la información necesitada.",
                  width=33, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(147,40,window=lb_info2)

    #Labels y Entry para la informacion necesitada
    lb_info3=tk.Label(pagina_huellaAgua, text="Nombre:",
                  width=13, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(50,100,window=lb_info3)
    txt_nombre=tk.Entry(pagina_huellaAgua, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,100,window=txt_nombre)

    lb_info4=tk.Label(pagina_huellaAgua, text="Cantidad de agua consumida",
                  width=23, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(122,140,window=lb_info4)
    lb_info5=tk.Label(pagina_huellaAgua, text="en un mes(en litros):",
                  width=26, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(105,160,window=lb_info5)
    txt_agua=tk.Entry(pagina_huellaAgua, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,150,window=txt_agua)
    
    #Boton para calcular la huella
    btn_calcular=tk.Button(pagina_huellaAgua, text="Calcular huella", command=calcular_huella,
                           bg="light grey", width=15, height=1, font=("Arial",12))
    area_trabajo.create_window(170,220,window=btn_calcular)

    #Boton para ver los calculos guardados
    btn_ver=tk.Button(pagina_huellaAgua, text="Ver huellas", command=ver_huellas,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,220,window=btn_ver)

    #Boton para buscar un calculo
    btn_buscar=tk.Button(pagina_huellaAgua, text="Buscar huella", command=buscar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,280,window=btn_buscar)

    #Boton para eliminar un calculo
    btn_elimnar=tk.Button(pagina_huellaAgua, text="Eliminar huella", command=eliminar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(170,280,window=btn_elimnar)
