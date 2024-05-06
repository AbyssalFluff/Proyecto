#Avance 02 de proyecto de Programacion en Python
#Creado por Ricardo Mora y Jordan Segura

#Importamos biblioteca tkinter al igual que modulos
import tkinter as tk
from tkinter import messagebox
from huellaCarros_modulo import *
from huellahogar_modulo import *

def nada():
    print("Hola")

#Creamos la pagina principal
pagina_principal = tk.Tk()
pagina_principal.title("EcoFriendly Clean Air")

#Creamos el area de trabajo
area_trabajo = tk.Canvas(pagina_principal, width=1200, height=720, bg="white")
area_trabajo.pack()

#Declaramos donde se abrira la pagina al ejecutarse
pagina_principal.geometry("1200x720+10+10")

#Creamos un titulo dentro de la pagina por el diseño
lb_titulo = tk.Label(pagina_principal, text="Bienvenidos a EcoFriendly Clean Air!",
                     width=30, height=1, font=("Arial", 32, "bold"), bg="white")
area_trabajo.create_window(390,30,window=lb_titulo)

#Creamos texto señalando que pueden realizar los usuarios con los botones
lb_info1 = tk.Label(pagina_principal, text="Utiliza estos botones para calcular tu huella de carbono.",
                    width=43, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(200,80,window=lb_info1)

#Creamos botones que redirigen a otras paginas con diferentes funciones
#
btn_1=tk.Button(pagina_principal, text="Carro", command=huella_carros,
                          bg="light grey", width=12, height=1, font=("Arial", 10))
area_trabajo.create_window(150,120,window=btn_1)
#
btn_2=tk.Button(pagina_principal, text="Energia", command=huella_energia,
                          bg="light grey", width=12, height=1, font=("Arial", 10))
area_trabajo.create_window(270,120,window=btn_2)
#
btn_3=tk.Button(pagina_principal, text="Lyrum", command=nada,
                          bg="light grey", width=12, height=1, font=("Arial", 10))
area_trabajo.create_window(150,160,window=btn_3)
#
btn_4=tk.Button(pagina_principal, text="Lyrum", command=nada,
                          bg="light grey", width=12, height=1, font=("Arial", 10))
area_trabajo.create_window(270,160,window=btn_4)

#Text explicando que es la huella de carbono
lb_info2 = tk.Label(pagina_principal, text="¿Qué es la huella de carbono?",
                    width=30, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(112,230,window=lb_info2)

lb_info3 = tk.Label(pagina_principal, text="La huella de carbono es una medida de la cantidad total de gases de efecto invernadero (GEI)",
                    width=75, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(334,260,window=lb_info3)
lb_info4 = tk.Label(pagina_principal, text="emitidos directa o indirectamente por un individuo, organización, evento, producto o servicio",
                    width=75, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(326,280,window=lb_info4)
lb_info5 = tk.Label(pagina_principal, text="a lo largo de su ciclo de vida.",
                    width=30, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(109,300,window=lb_info5)
lb_info6 = tk.Label(pagina_principal, text="La huella de carbono se expresa generalmente en términos de la cantidad de dióxido de carbono",
                    width=75, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(344,320,window=lb_info6)
lb_info7 = tk.Label(pagina_principal, text="equivalente (CO2e) emitido.",
                    width=30, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(106,340,window=lb_info7)

#Ejecutamos la pagina principal
pagina_principal.mainloop()