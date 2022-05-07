from Menu import menu
if __name__ =="__main__":
    unmenu=menu()
    op=str.lower(input("Seleccione la opcion que desea\n \ta-Actualizar el valor del vehículo de cada plan\n\tb-Mostrar datos de vehiculos inferiores a un valor\n\tc-Monto para licitar\n\td-Modificar la cantidad de cuotas para licitar\n\te-Mostrar\n\tf-Salir\n"))
    unmenu.operador(op)
    while (op!='f'):
        op=str.lower(input("Seleccione la opcion que desea\n \ta-Actualizar el valor del vehículo de cada plan\n\tb-Mostrar datos de vehiculos inferiores a un valor\n\tc-Monto para licitar\n\td-Modificar la cantidad de cuotas para licitar\n\te-Mostrar\n\tf-Salir\n"))
        unmenu.operador(op)
    print ("Adios")
