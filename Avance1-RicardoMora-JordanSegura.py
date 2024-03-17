#Avance 01 del proyecto de Programación en Python
#Creado por Ricardo Mora y Jordan Segura
usuarios=[]
print("Bienvenido a EcoFriendly!")
main_while=True
while main_while:
    nombre=input("\nAntes de comenzar...\nEscribe tu nombre: ")
    usuarios.append(nombre)
    print("Opciones de Menú:")
    print("""
        0. Salir
        1. ¿Que es la huella de carbono?
        2. Calcula tu huella de carbono.
        3. ¿Como mejorar tu huella de carbono?
        4. ¿Cual es el impacto ambiental de la huella de carbono?""")
    main_opcion=input("\nA donde quieres ir? ")
    if main_opcion=="0":
        print("Gracias por ser uno más en ayudar el bienestar del Mundo.")
        main_while=False
    elif main_opcion=="1":
        print("¿Que es la Huella de Carbono?")
        print(f"{nombre}, la huella de carbono es una medida de la cantidad total de gases de efecto invernadero (GEI) emitidos directa o indirectamente por un individuo, organización, evento, producto o servicio a lo largo de su ciclo de vida.")

    elif main_opcion=="2":
        print("no")
    elif main_opcion=="3":
        print("yes")
    elif main_opcion=="4":
        print("no")
    else:
        print("\nLo sentimos... Esa opcion no esta disponible.")