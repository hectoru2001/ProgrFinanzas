import os, mysql.connector, datetime

# Conexión con la base de datos
conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="user")
ejecucion = conexion.cursor()


while True:
    # Limpiar consola
    os.system("cls")

    # Extraer el total de la base de datos
    ejecucion.execute("SELECT total FROM ingresos ORDER BY id DESC LIMIT 1")
    resultado = ejecucion.fetchone()
    if resultado == None:
        print("Error al encontrar información en la base de datos")
        total = 0
    else:
        total = int(resultado[0])
    
    print("----- Bienvenido al programa de finanzas -----")
    print("")
    print("- Por favor elige la transacción que desees realizar -")
    print("1. Mostrar mi cantidad actual de dinero")
    print("2. Registrar un nuevo gasto de dinero")
    print("3. Registrar un nuevo ingreso de dinero")
    print("4. Cambiar la cantidad del total por una nueva")
    print("5. Mostrar los últimos gastos realizados")
    print("6. Mostrar los últimos ingresos realizados")
    print("7. Eliminar historial")




    print()
    opcion = input()
    
    if opcion == "1":
        print("Esta es la cantidad actual con la que cuentas de dinero: " + str(total))
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "2":
        print("Escribe la cantidad que hayas gastado")
        gasto = int(input())
        print("Ingresa el motivo del gasto")
        motGasto = input()
        total = total - gasto
        print("Muy bien, con el gasto registrado ahora tu cantidad de dinero es de: " + str(total))
        feGasto = datetime.date.today()
        ejecucion.execute(f"INSERT INTO ingresos (gasto, motGasto, feGasto, total) VALUES (%s, %s, %s, %s)", (gasto, motGasto, feGasto, total))
        conexion.commit()
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "3":
        print("Escribe la cantidad que hayas ingresado")
        ingreso = int(input())
        print("Ingresa el motivo del ingreso")
        motIngreso = input()
        total = total + ingreso
        print("Muy bien, con el ingreso registrado ahora tu cantidad de dinero es de: " + str(total))
        feIngreso = datetime.date.today()
        ejecucion.execute("INSERT INTO ingresos (ingreso, motIngreso, feIngreso, total) VALUES (%s, %s, %s, %s)", (ingreso, motIngreso, feIngreso, total))
        conexion.commit()
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "4":
        print("Ingresa la nueva cantidad de dinero que tienes")
        total = int(input())
        ejecucion.execute(f"INSERT INTO ingresos (total) VALUES ({total})" )
        conexion.commit()
        print("Muy bien, ahora la nueva cantidad que tienes de dinero es de: " + str(total))
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "5":
        print("Estos son los ultimos gastos que se han hecho")
        ejecucion.execute("SELECT gasto, motGasto, feGasto FROM ingresos ORDER BY id")
        gasInf = ejecucion.fetchall()
        for x in gasInf:
            print(f"Gasto: $ {x[0]} | Motivo: {x[1]} | Fecha: {x[2]}")
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "6":
        print("Estos son los ultimos ingresos que se han hecho")
        ejecucion.execute("SELECT ingreso, motIngreso, feIngreso FROM ingresos ORDER BY id")
        gasInf = ejecucion.fetchall()
        for x in gasInf:
            print(f"Ingreso: $ {x[0]} | Motivo: {x[1]} | Fecha: {x[2]}")
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "7":
         print("¿Estás seguro de que deseas borrar todo el historial? si / no")
         sel = input()
         if sel == "si":
             pass
         elif sel == "no":
             pass
