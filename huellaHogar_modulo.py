#Creado por Ricardo Mora y Jordan Segura
#Modulo para calcular huella de carbono

#Importamos biblioteca tkinter
import tkinter as tk
from tkinter import messagebox


huella_de_casas=[]

#Funcion para calcular la huella
def calcular_huella():
    Nombre = txt_nombre.get()
    Energia = txt_Energia.get()
    Energia = int(Energia)
    Huella = Energia*0.4
    registro = {"Nombre":Nombre, "Huella":Huella}
    huella_de_casas.append(registro)
    messagebox.showinfo("Registro",
                        f"Huella de {Nombre} registrada correctamente.")
    txt_nombre.delete(0, tk.END)
    txt_Energia.delete(0, tk.END)

#Funcion para ver las huellas registradas
def ver_huellas():
    mensaje = ""
    for i,huella in enumerate(huella_de_casas):
        mensaje += f"""Huella N.{i+1}:
        Nombre: {huella.get("Nombre")}
        Huella: {huella.get("Huella")} CO2\n\n"""
    messagebox.showinfo("Ver huellas",
                        f"{mensaje}")
    txt_nombre.delete(0, tk.END)
    txt_Energia.delete(0, tk.END)

#Funcion para buscar una huella registrada
def buscar_huella():
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huella_de_casas:
        if Nombre == nombre.get("Nombre"):
            bandera=True
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos encotrado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_Energia.delete(0, tk.END)


#Funcion para eliminar una huella registrada
def eliminar_huella():
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huella_de_casas:
        if Nombre == nombre.get("Nombre"):
            bandera=True
            indice=huella_de_casas.index(nombre)
            del huella_de_casas[indice]
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos eliminado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_Energia.delete(0, tk.END)


#Funcion para la nueva ventana
def huella_energia():
    #Definimos variables globales
    global txt_nombre, txt_Energia
    #Creamos una nueva ventana ventana
    pagina_huellacasas = tk.Tk()
    pagina_huellacasas.title("Calcula la huella de tu carro")

    #Creamos el area de trabajo
    area_trabajo = tk.Canvas(pagina_huellacasas, width=500, height=400, bg="White")
    area_trabajo.pack()

    #Declaramos donde se abrira la pagina al ejecutarse
    pagina_huellacasas.geometry("480x350+1230+100")

    #Texto diciendo que hace la pagina
    lb_info1=tk.Label(pagina_huellacasas, text="Aqui puedes calcular la huella de carbono de tu casa.",
                  width=44, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(192,20,window=lb_info1)
    lb_info2=tk.Label(pagina_huellacasas, text="Solo completa la información necesitada.",
                  width=33, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(150,40,window=lb_info2)

    #Labels y Entry para la informacion necesitada
    lb_info3=tk.Label(pagina_huellacasas, text="Nombre:",
                  width=13, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(50,100,window=lb_info3)
    txt_nombre=tk.Entry(pagina_huellacasas, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,100,window=txt_nombre)

    lb_info4=tk.Label(pagina_huellacasas, text="Cuanta Energia(en kilovatios) ",
                  width=23, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(122,140,window=lb_info4)
    lb_info5=tk.Label(pagina_huellacasas, text="consume tu casa por mes:",
                  width=26, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(128,160,window=lb_info5)
    txt_Energia=tk.Entry(pagina_huellacasas, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,150,window=txt_Energia)
    
    #Boton para calcular la huella
    catch_btn=tk.Button(pagina_huellacasas, text="Calcular huella", command=calcular_huella,
                           bg="light grey", width=15, height=1, font=("Arial",12))
    area_trabajo.create_window(170,220,window=catch_btn)

    #Boton para ver los calculos guardados
    view_btn=tk.Button(pagina_huellacasas, text="Ver huellas", command=ver_huellas,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,220,window=view_btn)

    #Boton para buscar un calculo
    search_btn=tk.Button(pagina_huellacasas, text="Buscar huella", command=buscar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,280,window=search_btn)

    #Boton para eliminar un calculo
    release_btn=tk.Button(pagina_huellacasas, text="Eliminar huella", command=eliminar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(170,280,window=release_btn)
