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
    area_trabajo = tk.Canvas(pagina_huellaCarros, width=540, height=400, bg="White")
    area_trabajo.pack()

    #Declaramos donde se abrira la pagina al ejecutarse
    pagina_huellaCarros.geometry("540x400+1230+100")