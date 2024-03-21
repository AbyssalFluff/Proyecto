#Avance 01 del proyecto de Programación en Python
#Creado por Ricardo Mora y Jordan Segura
usuarios=[]
gasolina=["Carro","Moto","Camión"]
transporte=["Bus","Tren","Taxi"]
electrico=["Carro","Moto"]
objetos=("Vehículos","Electrodomésticos","Edificios","Productos de plástico","Productos de papel")
print("""
                  ==========================
                  =Bienvenido a EcoFriendly=
                  ==========================""")
main_while=True
while main_while:
    users_co2={"usuario":"","co2":""}
    print("""
        -------------------
        |Opciones de Menú:|
        -------------------""") 
    print("""
        *****************************************************************
        * 0. Salir                                                      *
        * 1. ¿Que es la Huella de Carbono?                              *
        * 2. Calcula tu Huella de Carbono                               *
        * 3. ¿Como mejorar tu Huella de Carbono?                        *
        * 4. ¿Cual es el impacto ambiental de la Huella de Carbono?     *
        * 5. Objetos que dejan mayor Huella de Carbono                  *
        * 6. Observar los usuarios registrados                          *
        *****************************************************************
        """)
    main_opcion=input("""
        A donde quieres ir? 
        """)
    if main_opcion=="0":
        print("Gracias por ser uno más en ayudar el bienestar del Mundo.")
        main_while=False
    elif main_opcion=="1":
        print("""
                            -----------------------------
                            Que es la Huella de Carbono?
                            -----------------------------
....................................................................................................
. La huella de carbono es una medida de la cantidad total de gases de efecto invernadero (GEI)     .
. emitidos directa o indirectamente por un individuo, organización, evento, producto o servicio    .
. a lo largo de su ciclo de vida.                                                                  .
.                                                                                                  .
. La huella de carbono se expresa generalmente en términos de la cantidad de dióxido de carbono    .
. equivalente (CO2e) emitido.                                                                      .
....................................................................................................
""")
    elif main_opcion=="2":
        nombre=input("""
    Antes de comenzar...
    Escribe tu nombre: """)
        usuarios.append(nombre)
        users_co2["usuario"]=nombre
        vehiculo=input("""
    ¿Posee algún vehículo?
    Si/No\n""")
        vehiculo_lower=vehiculo.lower()
        if vehiculo_lower=="si":
            print("""
          ===================================
          =¿Qué medio de transporte utiliza?=
          ===================================""")
            vehiculo_tipo=input("""
    -----------------
    * 1. Gasolina   *
    * 2. Eléctrico  *
    * 3. Híbrido    *
    -----------------
    Elija una opción: """)
            print()
            if vehiculo_tipo=="1":
                for tipo in gasolina:
                    print(tipo)
                tipo_gas=input("""
    ¿Escriba el tipo de vehículo que utiliza?""")
                if tipo_gas in gasolina:
                    co2_vehiculo="345 kg de CO2"
                    print(co2_vehiculo)
                    users_co2["co2"]=co2_vehiculo
                else:
                    print("Ese vehículo no está disponible")
                  
            elif vehiculo_tipo=="2":
                print("\t.................")
                for tipo in electrico:
                    print(f"\t{tipo}")
                print("\t..................")
                tipo_electrico=input("\n¿Qué tipo de vehículo utiliza?\n")
                if tipo_electrico in electrico:
                    co2_vehiculo="\n172 kg de CO2"
                    print(co2_vehiculo)
                    users_co2["co2"]=co2_vehiculo
                else:
                    print("Ese vehículo no está disponible")
              
            elif vehiculo_tipo=="3":
                co2_vehiculo="172 kg de CO2"
                print(co2_vehiculo)
                users_co2["co2"]=co2_vehiculo
            else:
                print("Esa no es una opción.")
              
        elif vehiculo_lower=="no":
            print("""
          ===================================
          =¿Qué medio de transporte utiliza?=
          ===================================""")
            transporte_tipo=input("""
    -----------------
    * 1. Gasolina   *
    * 2. Eléctrico  *
    * 3. Híbrido    *
    -----------------
    Elija una opción: """)
            if transporte_tipo=="1":
                for tipo in transporte:
                    print(tipo)
                tipo_gas=input("¿Qué tipo de vehículo utiliza?")
                if tipo_gas in transporte:
                    co2_vehiculo="345 kg de CO2"
                    print(co2_vehiculo)
                    users_co2["co2"]=co2_vehiculo
                else:
                    print("Ese vehículo no está disponible")
                  
            elif transporte_tipo=="2":
                for tipo in transporte:
                    print(tipo)
                tipo_electrico=input("¿Qué tipo de vehículo utiliza?")
                if tipo_electrico in transporte:
                    co2_vehiculo="172 kg de CO2"
                    print(co2_vehiculo)
                    users_co2["co2"]=co2_vehiculo
                else:
                    print("Ese vehículo no está disponible")
              
            elif transporte_tipo=="3":
                co2_vehiculo="172 kg de CO2"
                print(co2_vehiculo)
                users_co2["co2"]=co2_vehiculo
            else:
                print("Esa no es una opción.")
        else:
            print("Esa no es una opción.")
        print(f"""
        Aquí están tus datos {nombre}
        Usuario: {users_co2["usuario"]}
        CO2: {users_co2["co2"]}""")
    elif main_opcion=="3":
        print("""
                        -----------------------------------
                        ¿Como mejorar tu Huella de Carbono?
                        -----------------------------------
....................................................................................................
. Mejorar tu huella de carbono implica reducir las emisiones de gases de efecto invernadero en     .
. tus actividades diarias. Puedes lograrlo mediante la reducción del consumo de energía, adoptando .
. transporte sostenible, practicando la reducción, reutilización y reciclaje, modificando tu dieta .
. hacia opciones más basadas en plantas, apoyando las energías renovables, conservando el agua y   .
. educándote sobre tus impactos ambientales. Cada pequeña acción contribuye a la mitigación del    .
. cambio climático.                                                                                .
....................................................................................................
""")                                                                           
    elif main_opcion=="4":
        print(f"""
            ------------------------------------------------------
            ¿Cual es el impacto ambiental de la Huella de Carbono?
            ------------------------------------------------------
....................................................................................................
. La huella de carbono representa el impacto ambiental de las actividades humanas en               .
. términos de emisiones de gases de efecto invernadero. Este impacto incluye el cambio             .
. climático,acidificación oceánica, degradación de ecosistemas, pérdida de biodiversidad           .
. y costos socioeconómicos. Reducir la huella de carbono es crucial para mitigar estos             .
. impactos y proteger el medio ambiente y las comunidades humanas.                                 .
....................................................................................................
""")
    elif main_opcion=="5":
        print("\t\t..........................................")
        print("\t\tObjetos que dejan mayor Huella de Carbono")
        print("\t\t..........................................")
        print("\n\t......................")
        for chingadera in objetos:
            print(f"\t{chingadera}")
        print("\t......................")
    elif main_opcion == "6":
        print("Observa los usuarios registrados")
        for usuario in usuarios:
            print(usuario)
        editar_usuarios=input(f"""
        .......................................................
        . ¿Deseas "agregar" o "eliminar" algún usuario?       .
        . Puedes escribir las palabras entre "" para confimar .
        . Puedes escribir "exit" para salir                   .
        .......................................................\n""")
        editar_usuarios_lower=editar_usuarios.lower()
        if editar_usuarios_lower=="agregar":
            add_usuario=input("Ingrese el nombre del usuario que desea agregar: ")
            usuarios.append(add_usuario)
            print("\nEsta es la lista con el usuario agregado: ")
            for usuario in usuarios:
                print(usuario, end=", ")
        elif editar_usuarios_lower=="eliminar":
            del_usuario=input("Escribe el usuario que quieres eliminar: ")
            if del_usuario in usuarios:
                usuarios.remove(del_usuario)
                print(f"\nSe ha eliminado {del_usuario} de los usuarios:")
                for usuario in usuarios:
                    print(usuario)
        elif editar_usuarios_lower=="exit":
            continue
        else:
            print("Esa no es una opción.")
    else:
        print("Lo sentimos... Esa opcion no esta disponible.")
