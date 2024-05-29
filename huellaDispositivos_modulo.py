#Creado por Ricardo Mora y Jordan Segura
#Modulo para calcular huella de carbono

#Importamos biblioteca tkinter
import tkinter as tk
from tkinter import messagebox


huella_de_dispositivos=[]

#Funcion para calcular la huella
def calcular_huella():
    Nombre = txt_nombre.get()
    dispositivo = txt_dispositivo.get()
    dispositivo = int(dispositivo)
    Huella = dispositivo*0.06
    registro = {"Nombre":Nombre, "Huella":Huella}
    huella_de_dispositivos.append(registro)
    messagebox.showinfo("Registro",
                        f"Huella de {Nombre} registrada correctamente.")
    txt_nombre.delete(0, tk.END)
    txt_dispositivo.delete(0, tk.END)

#Funcion para ver las huellas registradas
def ver_huellas():
    mensaje = ""
    for i,huella in enumerate(huella_de_dispositivos):
        mensaje += f"""Huella N.{i+1}:
        Nombre: {huella.get("Nombre")}
        Huella: {huella.get("Huella")}Kg CO2\n\n"""
    messagebox.showinfo("Ver huellas",
                        f"{mensaje}")
    txt_nombre.delete(0, tk.END)
    txt_dispositivo.delete(0, tk.END)

#Funcion para buscar una huella registrada
def buscar_huella():
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huella_de_dispositivos:
        if Nombre == nombre.get("Nombre"):
            bandera=True
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos encotrado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_dispositivo.delete(0, tk.END)


#Funcion para eliminar una huella registrada
def eliminar_huella():
    bandera=False
    Nombre=txt_nombre.get()
    for nombre in huella_de_dispositivos:
        if Nombre == nombre.get("Nombre"):
            bandera=True
            indice=huella_de_dispositivos.index(nombre)
            del huella_de_dispositivos[indice]
    if bandera:
        messagebox.showinfo("Buscar huella",
                    f"Hemos eliminado tu huella {Nombre}.")
    else:
        messagebox.showinfo("Buscar huella",
                    f"No hemos encontrado tu huella {Nombre}.")
    txt_nombre.delete(0, tk.END)
    txt_dispositivo.delete(0, tk.END)


#Funcion para la nueva ventana
def huella_dispositivos():
    #Definimos variables globales
    global txt_nombre, txt_dispositivo
    #Creamos una nueva ventana ventana
    pagina_huelladispositivos = tk.Tk()
    pagina_huelladispositivos.title("Calcula la huella de tus dispositivos")

    #Creamos el area de trabajo
    area_trabajo = tk.Canvas(pagina_huelladispositivos, width=500, height=400, bg="White")
    area_trabajo.pack()

    #Declaramos donde se abrira la pagina al ejecutarse
    pagina_huelladispositivos.geometry("480x350+1230+100")

    #Texto diciendo que hace la pagina
    lb_info1=tk.Label(pagina_huelladispositivos, text="Aqui puedes calcular la huella de carbono de tus dispositivos.",
                  width=50, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(220,20,window=lb_info1)
    lb_info2=tk.Label(pagina_huelladispositivos, text="Solo completa la información necesitada.",
                  width=33, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(150,40,window=lb_info2)

    #Labels y Entry para la informacion necesitada
    lb_info3=tk.Label(pagina_huelladispositivos, text="Nombre:",
                  width=13, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(50,100,window=lb_info3)
    txt_nombre=tk.Entry(pagina_huelladispositivos, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,100,window=txt_nombre)

    lb_info4=tk.Label(pagina_huelladispositivos, text="Cuantos dispositivos tiene: ",
                  width=23, height=1, font=("Arial", 12), bg="white")
    area_trabajo.create_window(114,140,window=lb_info4)

    txt_dispositivo=tk.Entry(pagina_huelladispositivos, font=("Arial", 12), width=18)
    area_trabajo.create_window(360,150,window=txt_dispositivo)
    
    #Boton para calcular la huella
    btn_calcular=tk.Button(pagina_huelladispositivos, text="Calcular huella", command=calcular_huella,
                           bg="light grey", width=15, height=1, font=("Arial",12))
    area_trabajo.create_window(170,220,window=btn_calcular)

    #Boton para ver los calculos guardados
    btn_ver=tk.Button(pagina_huelladispositivos, text="Ver huellas", command=ver_huellas,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,220,window=btn_ver)

    #Boton para buscar un calculo
    btn_buscar=tk.Button(pagina_huelladispositivos, text="Buscar huella", command=buscar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(330,280,window=btn_buscar)

    #Boton para eliminar un calculo
    btn_elimnar=tk.Button(pagina_huelladispositivos, text="Eliminar huella", command=eliminar_huella,
                           bg="light grey", width=15, height=1, font=("Arial", 12))
    area_trabajo.create_window(170,280,window=btn_elimnar)
