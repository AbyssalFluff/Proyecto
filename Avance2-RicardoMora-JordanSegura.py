#Avance 02 de proyecto de Programacion en Python
#Creado por Ricardo Mora y Jordan Segura

#Importamos biblioteca tkinter al igual que modulos
import tkinter as tk
from tkinter import messagebox

def nada():
    print("Hola")

#Creamos la pagina principal
pagina_principal = tk.Tk()
pagina_principal.title("Por ahora")

#Creamos el area de trabajo
area_trabajo = tk.Canvas(pagina_principal, width=1200, height=720, bg="white")
area_trabajo.pack()

#Declaramos donde se abrira la pagina principal al ejecutarse
pagina_principal.geometry("1200x720+10+10")

#Creamos un titulo dentro de la pagina por el diseño
lb_titulo = tk.Label(pagina_principal, text="Bienvenidos a EcoFriendly Clean Air!",
                    width=30, height=1, font=("Arial", 32, "bold"), bg="white")
area_trabajo.create_window(390,30,window=lb_titulo)

#Creamos texto señalando que pueden realizar los usuarios con los botones
lb_info = tk.Label(pagina_principal, text="Utiliza estos botones para calcular tu huella de carbono.",
                    width=43, height=1, font=("Arial", 12), bg="white")
area_trabajo.create_window(200,80,window=lb_info)

#Creamos botones que redirigen a otras paginas con diferentes funciones
#
btn_1=tk.Button(pagina_principal, text="Lyrum", command=nada,
                          bg="light grey", width=12, height=1, font=("Arial", 10))
area_trabajo.create_window(150,120,window=btn_1)
#
btn_2=tk.Button(pagina_principal, text="Lyrum", command=nada,
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

#Ejecutamos la pagina principal
pagina_principal.mainloop()