import os
os.system("cls")

dCant = 0
dGast = 0

while True:
    print("Menú de opciones:")
    print("1. Ingresar gasto")
    print("2. Mostrar dinero actual")
    print("3. Ingresar nueva cantidad de dinero")
    print("4. Ingresar un nuevo déposito")
    print("5. Salir del programa")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        bddGast = open("dGast.txt", "w")
        dGast = input("Ingresa la cantidad que se haya gastado $")
        bddGast.write(dGast)
        bddGast.close()
        input("")
    elif opcion == "2":
        bddCant = open("dCant.txt", "r")
        bddGast = open("dGast.txt", "r")
        dGast = bddGast.read()
        dCant = bddCant.read()
        num1 = int(dGast)
        num2 = int(dCant)
        print("Esta es la cantidad de dinero con la que cuentas actualmente $" + str(num2 - num1))
        bddCant.close()
        bddGast.close()
    elif opcion == "3":
        bddCant = open("dCant.txt", "w")
        dCant = input("Ingresa la cantidad que deseas cambiar $")
        bddCant.write(dCant)
        bddCant.close()
        input("")
    elif opcion == "4":
        bddIngr = open("dIngr.txt", "w")
        dIngr = input("Ingresa la cantidad cantidad que se haya ingresado $")
        bddIngr.write(dIngr)
        print("Esta es la cantidad de dinero con la que cuentas actualmente $")
        bddIngr.close()
        input("")
    elif opcion == "5":
        print("Hasta la próxima")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presiona enter para continuar")