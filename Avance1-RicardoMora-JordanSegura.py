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
        print("""
-----------------------------
¿Que es la Huella de Carbono?
-----------------------------

La huella de carbono es una medida de la cantidad total de gases de efecto invernadero (GEI)
emitidos directa o indirectamente por un individuo, organización, evento, producto o servicio
a lo largo de su ciclo de vida.

La huella de carbono se expresa generalmente en términos de la cantidad de dióxido de carbono
equivalente (CO2e) emitido.""")
    elif main_opcion=="2":
        nombre=input("\nAntes de comenzar...\nEscribe tu nombre: ")
        usuarios.append(nombre)
        print("no")
    elif main_opcion=="3":
        print("""
-----------------------------------
¿Como mejorar tu Huella de Carbono?
-----------------------------------

Mejorar tu huella de carbono implica reducir las emisiones de gases de efecto invernadero en
tus actividades diarias. Puedes lograrlo mediante la reducción del consumo de energía, adoptando
transporte sostenible, practicando la reducción, reutilización y reciclaje, modificando tu dieta 
hacia opciones más basadas en plantas, apoyando las energías renovables, conservando el agua y 
educándote sobre tus impactos ambientales. Cada pequeña acción contribuye a la mitigación del cambio climático.""")
    elif main_opcion=="4":
        print(f"""
------------------------------------------------------
¿Cual es el impacto ambiental de la Huella de Carbono?
------------------------------------------------------
La huella de carbono representa el impacto ambiental de las actividades humanas en 
términos de emisiones de gases de efecto invernadero. Este impacto incluye el cambio 
climático,acidificación oceánica, degradación de ecosistemas, pérdida de biodiversidad
y costos socioeconómicos. Reducir la huella de carbono es crucial para mitigar estos
impactos y proteger el medio ambiente y las comunidades humanas.""")
    else:
        print("\nLo sentimos... Esa opcion no esta disponible.")