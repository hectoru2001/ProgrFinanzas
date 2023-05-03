import os
import mysql.connector
os.system("cls")

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="user")
eject = conexion1.cursor()

# Obtener el saldo anterior desde el archivo
with open("saldo.txt", "r") as archivo:
    saldo = archivo.read()
    saldo_anterior = int(saldo)

while True:
    print("Menú de opciones:")
    print("1. Ingresar gasto")
    print("2. Mostrar dinero actual")
    print("3. Ingresar nueva cantidad de dinero")
    print("4. Ingresar un nuevo déposito")
    print("5. Salir del programa")
    print("6. Mostrar ultimos gastos hechos")

    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        
        # Escribir valor total en archivo de texto
        gas = int(input("Ingrese un Gasto: "))
        mot = input('Ingrese el motivo del gasto: ')
        with open("saldo.txt", "w") as archivo:
            archivo.write(str(saldo_actual - gas))

        # Secuencia para guardar valor en base de datos
        values = (gas, mot)
        sql = "INSERT INTO ingresos (gasto, motivo) VALUES (%s, %s)"
        eject.execute(sql, values)
        conexion1.commit()
        print("El saldo actual es:", saldo_actual - gas)
        print(eject.rowcount, input("Valor insertado correctamente, pulsa cualquier tecla para continuar "))
        os.system("cls")
        
        
    elif opcion == "2":
        os.system("cls")
        with open("saldo.txt", "r") as archivo:
            archivo.read(saldo)
        print("Esta es la cantidad de dinero con la que cuentas actualmente: ", saldo)
        input("Pulsa cualquier tecla para continuar")
        os.system("cls")
        
        
    elif opcion == "3":
        os.system("cls")
        nCant = int(input("Ingrese la nueva cantidad de dinero "))
        saldo_actual = nCant
        with open("saldo.txt", "w") as archivo:
            archivo.write(str(saldo_actual))
        print("Esta es la cantidad de dinero con la que cuentas actualmente: " + str(saldo_actual))
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
        eject.execute("SELECT gasto, motivo FROM ingresos")
        resultados = eject.fetchall()
        os.system("cls")
        for fila in resultados:
            print(fila)
        input("Pulsa cualquier tecla para continuar")

    elif opcion == "6":
        os.system("cls")
        print("Nos vemos pronto")
        break  
            
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presiona enter para continuar")