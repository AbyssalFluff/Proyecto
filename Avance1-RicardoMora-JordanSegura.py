#Avance 01 de proyecto de Programacion en Python
#Creado por Ricardo Mora y Jordan Segura
usuarios=[]
print("Bienvenido a EcoFriendly!")
main_while=True
while main_while:
    nombre=input("Antes de comenzar...\nEscribe tu nombre: ")
    usuarios.append(nombre)
    print("""
        0. Salir
        1. Que es la Huella de Carbono
        2. Calcula tu Huella de Carbono
        3. Como mejorar tu Huella de Carbono
        4.""")
    main_opcion=input("A donde quieres ir? ")
    if main_opcion=="0":
        main_while=False
    elif main_opcion=="1":
        print("si")
    elif main_opcion=="2":
        print("no")
    elif main_opcion=="3":
        print("yes")
    elif main_opcion=="4":
        print("no")
    else:
        print("\nLo sentimos... Esa opcion no esta disponible.")