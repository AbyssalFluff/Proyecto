#Avance 01 del proyecto de Programación en Python
#Creado por Ricardo Mora y Jordan Segura
usuarios=[]
print("Bienvenido a EcoFriendly!")
main_while=True
while main_while:
    print("Opciones de Menú:")
    print("""
        0. Salir
        1. ¿Que es la Huella de Carbono?
        2. Calcula tu Huella de Carbono
        3. ¿Como mejorar tu Huella de Carbono?
        4. ¿Cual es el impacto ambiental de la Huella de Carbono?""")
    main_opcion=input("\nA donde quieres ir? ")
    if main_opcion=="0":
        print("Gracias por ser uno más en ayudar el bienestar del Mundo.")
        main_while=False
    elif main_opcion=="1":
        print("¿Que es la Huella de Carbono?")
        print("La huella de carbono es una medida de la cantidad total de gases de efecto invernadero (GEI) emitidos directa o indirectamente por un individuo, organización, evento, producto o servicio a lo largo de su ciclo de vida.")

    elif main_opcion=="2":
        nombre=input("\nAntes de comenzar...\nEscribe tu nombre: ")
        usuarios.append(nombre)
        print("no")
    elif main_opcion=="3":
        print("yes")
    elif main_opcion=="4":
        print(f"""
¿Cual es el impacto ambiental de la Huella de Carbono?

La huella de carbono es una medida del impacto ambiental directo e indirecto de las
actividades humanas en términos de las emisiones de gases de efecto invernadero, 
expresadas como equivalentes de dióxido de carbono (CO2e). Su impacto ambiental es
significativo y multifacético:""")
    else:
        print("\nLo sentimos... Esa opcion no esta disponible.")