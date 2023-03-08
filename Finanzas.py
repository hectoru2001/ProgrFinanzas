import os
import mysql.connector
os.system("cls")

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="user")
eject = conexion1.cursor()
subtotal = 0
total = 0
while True:
    print("Menú de opciones:")
    print("1. Ingresar gasto")
    print("2. Mostrar dinero actual")
    print("3. Ingresar nueva cantidad de dinero")
    print("4. Ingresar un nuevo déposito")
    print("5. Salir del programa")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        gas = int(input("Ingrese un Gasto: "))
        mot = input('Ingrese el motivo del gasto: ')
        sql = "INSERT INTO ingresos (gasto, motivo) VALUES (%s, %s)"
        values = (gas, mot)
        total = (subtotal - gas)
        eject.execute(sql, values)
        conexion1.commit()
        print(eject.rowcount, input("Valor insertado correctamente, pulsa cualquier tecla para continuar " + str(total)))
        os.system("cls")
    elif opcion == "2":
        os.system("cls")
        print("Esta es la cantidad de dinero con la que cuentas actualmente: " + str(total))
        input("Pulsa cualquier tecla para continuar")
        os.system("cls")
    elif opcion == "3":
        os.system("cls")
        ncant = input("Ingrese la nueva cantidad de dinero ")
        total = ncant        
        print("Esta es la cantidad de dinero con la que cuentas actualmente: " + str(total))
        input("Pulsa cualquier tecla para continuar")
        os.system("cls")
    elif opcion == "4":
        ing = int(input("Ingrese un cantidad de dinero: "))
        mot = input('Ingrese el motivo del gasto: ')
        sql = "INSERT INTO ingresos (ingreso, motivo) VALUES (%s, %s)"
        values = (ing, mot)
        eject.execute(sql, values)
        conexion1.commit()
        print(eject.rowcount, "record inserted.")
    elif opcion == "5":
        os.system("cls")
        print("Nos vemos pronto")
        break
    elif opcion == "6":
        eject.execute("SELECT * FROM ingresos")
        resultados = eject.fetchall()
        for fila in resultados:
            print(fila)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presiona enter para continuar")