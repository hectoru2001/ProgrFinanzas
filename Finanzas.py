import os, mysql.connector, datetime
from prettytable import PrettyTable  

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
        print("* No existe historial de gastos, ingrese nueva información *")
        total = 0
    else:
        total = float(resultado[0])
    
    print("----- Bienvenido al programa de finanzas -----")
    print("")
    print("- Por favor elige la transacción que desees realizar -")
    print("1. Mostrar mi cantidad actual de dinero")
    print("2. Registrar un nuevo gasto de dinero")
    print("3. Registrar un nuevo ingreso de dinero")
    print("4. Cambiar la cantidad del total por una nueva")
    print("5. Mostrar los últimos gastos realizados")
    print("6. Mostrar los últimos ingresos recibidos")
    print("7. Eliminar historial")




    print()
    opcion = input()
    
    if opcion == "1":
        print("Esta es la cantidad actual con la que cuentas de dinero: " + str(total))
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "2":
        print("Escribe la cantidad que hayas gastado:")
        gasto = float(input("$ "))
        print("Ingresa el motivo del gasto:")
        motGasto = input()
        total = total - gasto
        print("Muy bien, con el gasto registrado ahora tu cantidad de dinero es de: " + str(total))
        feGasto = datetime.date.today()
        ejecucion.execute(f"INSERT INTO ingresos (gasto, motGasto, feGasto, total) VALUES (%s, %s, %s, %s)", (gasto, motGasto, feGasto, total))
        conexion.commit()
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "3":
        print("Escribe la cantidad que hayas ingresado:")
        ingreso = float(input("$ "))
        print("Ingresa el motivo del ingreso:")
        motIngreso = input()
        total = total + ingreso
        print("Muy bien, con el ingreso registrado ahora tu cantidad de dinero es de: " + str(total))
        feIngreso = datetime.date.today()
        ejecucion.execute("INSERT INTO ingresos (ingreso, motIngreso, feIngreso, total) VALUES (%s, %s, %s, %s)", (ingreso, motIngreso, feIngreso, total))
        conexion.commit()
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "4":
        print("Ingresa la nueva cantidad de dinero que tienes:")
        total = float(input("$ "))
        ejecucion.execute(f"INSERT INTO ingresos (total) VALUES ({total})" )
        conexion.commit()
        print("Muy bien, ahora la nueva cantidad que tienes de dinero es de: " + str(total))
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "5":
        print("Estos son los ultimos gastos que se han hecho")
        ejecucion.execute("SELECT gasto, motGasto, feGasto FROM ingresos WHERE gasto > 0 ORDER BY id")
        gasInf = ejecucion.fetchall()
        tablaG = PrettyTable(['Gasto', 'Motivo de gasto', 'Fecha de gasto'])
        for prGas in gasInf:
            tablaG.add_row(prGas)
        print(tablaG)
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "6":
        print("Estos son los ultimos ingresos que se han recibido")
        ejecucion.execute("SELECT ingreso, motIngreso, feIngreso FROM ingresos WHERE ingreso > 0 ORDER BY id")
        gasInf = ejecucion.fetchall()
        tablaI = PrettyTable(['Ingreso', 'Motivo de ingreso', 'Fecha de ingreso'])
        for prIng in gasInf:
            tablaI.add_row(prIng)
        print(tablaI) 
        input("Pulsa cualquier tecla para continuar")
    elif opcion == "7":
         print("¿Estás seguro de que deseas borrar todo el historial? si / no")
         sel = input()
         if sel == "si":
             ejecucion.execute("DELETE FROM ingresos")
             conexion.commit()
             input("Historial eliminado con éxito, pulse cualquier tecla para continuar")
         elif sel == "no":
             pass
    elif opcion == "69":
        ejecucion.execute("SELECT id, gasto, motGasto, feGasto, ingreso, motIngreso, feIngreso, total FROM ingresos")
        bdd = ejecucion.fetchall()
        tabla = PrettyTable(['ID', 'Gastos', 'Motivo de gasto', 'Fecha de gasto', 'Ingreso', 'Motivo de ingreso', 'Fecha de ingreso', 'Total'])
        for muestra in bdd:
            tabla.add_row(muestra)
        print(tabla)
        input("")
    elif opcion == "deudas":
        print("- Bienvenido al modo de deudas -")
        print("Ingresa por favor la descripción de la deuda")
        descDeuda = input("")
        print("Ingresa el monto de la deuda")
        montDeuda = float(input(""))
        dateActual = datetime.date.today()
        ejecucion.execute("INSERT INTO deudas (descripcion, monto, fecha) VALUES (%s, %s, %s)", (descDeuda, montDeuda, dateActual))
        print("¿Deseas ver el listado de deudas?")
        ele = input()
        if ele == "si":
            print("Estas son las deudas por el momento")
            ejecucion.execute("SELECT descripcion, monto, fecha FROM deudas")
            deuInf = ejecucion.fetchall()
            tablaII = PrettyTable(['Descripción de deuda', 'Monto de deuda', 'Fecha de pago'])
            for prDeu in deuInf:
                tablaII.add_row(prDeu)
            print(tablaII) 
            input("Pulsa cualquier tecla para continuar")
        elif ele == "no":
            pass