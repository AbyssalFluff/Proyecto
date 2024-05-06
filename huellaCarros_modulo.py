#Creado por Ricardo Mora y Jordan Segura
#Modulo para calcular huella de carbono

#Importamos biblioteca tkinter
import tkinter as tk
from tkinter import messagebox

def huella_carros():
    #Definimos variables globales

    #Creamos una nueva ventana ventana
    pagina_huellaCarros = tk.Tk()
    pagina_huellaCarros.title("Calcula la huella de tu carro")

    #Creamos el area de trabajo
    area_trabajo = tk.Canvas(pagina_huellaCarros, width=640, height=400, bg="White")
    area_trabajo.pack()

    #Declaramos donde se abrira la pagina al ejecutarse
    pagina_huellaCarros.geometry("640x400+1230+100")

    #Texto diciendo que hace la pagina
    lb_info1=tk.Label(pagina_huellaCarros, text="Aqui puedes calcular la huella de carbono de tu carro.",
                  width=44, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(195,20,window=lb_info1)
    lb_info2=tk.Label(pagina_huellaCarros, text="Solo completa la información necesitada.",
                  width=33, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(150,40,window=lb_info2)

    #Labels and Entry for the needed information
    lb_info3=tk.Label(pagina_huellaCarros, text="Nombre:",
                  width=13, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(71,100,window=lb_info3)
    txt_nombre=tk.Entry(pagina_huellaCarros, font=("Arial", 12), width=18)
    area_trabajo.create_window(250,100,window=txt_nombre)

    lb_info4=tk.Label(pagina_huellaCarros, text="Cuanto combustible(en litros) ",
                  width=23, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(130,140,window=lb_info4)
    lb_info5=tk.Label(pagina_huellaCarros, text="consume tu carro por kilómetro:",
                  width=26, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(130,160,window=lb_info5)
    txt_combustible=tk.Entry(pagina_huellaCarros, font=("Arial", 12), width=18)
    area_trabajo.create_window(330,150,window=txt_combustible)
    
    
