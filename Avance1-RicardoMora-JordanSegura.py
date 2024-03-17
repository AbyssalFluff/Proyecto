#Avance 01 de proyecto de Programacion en Python
#Creado por Ricardo Mora y Jordan Segura
print("Bienvenido a ")
main_while=True
while main_while:
    print("""\n0. Exit
1.
2.
3.
4.""")
    main_opcion=input("A donde quieres ir? ")
    if main_opcion==0:
        main_while=False
    if main_opcion==1:
        print("si")
    else:
        print("Lo sentimos... Esa opcion no esta disponible.")