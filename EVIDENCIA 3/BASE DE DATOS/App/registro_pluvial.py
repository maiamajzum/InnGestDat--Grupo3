def registroPluvialMenu() :
    print("Accediendo al menú de REGISTROS PLUVIALES:")

    año = int(input("Ingrese el AÑO que desee conocer: "))

    comprovación_año = año # A MODIFICAR MAS ADELANTE!

    print(f"Registros del AÑO {año} cargados, seleccione como proseguir:")

    while True:
        print("")
        print("")
        print("")
        print("")

        userOp = input("Seleccione: ")

        match userOp:
            case 1:
                print("1")