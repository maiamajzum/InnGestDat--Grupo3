import calendar
import os
import pandas as pan
import numpy as np
import matplotlib.pyplot as plt

# MENU PRINCIPAL -> Acá Comienza la MAGIA!

def registroPluvialMenu() :

    
    print("\nAccediendo al menú de REGISTROS PLUVIALES:")

    año = int(input("Ingrese el AÑO que desee conocer: "))

    comprovación_año = crearOcargar(año)

    print(f"\nRegistro N° {año} cargado, seleccione como proseguir:")

    while True:
        print("\nOpciones:")
        print("---------")
        print("1 -> Buscar mes")
        print("2 -> Buscar año")
        print("3 -> Generar gráfico")
        print("4 -> Exportar datos")
        print("0 ->Salir")
        print("---------")

        userOp = input("Seleccione: ")

        match userOp:
            case "1":
                mes = int(input("Ingrese un NÚMERO de mes (1-12): "))
                if 1 <= mes <= 12:
                    mostrarMes(comprovación_año, mes, año)
                else:
                    print("Mes inválido. Por favor ingrese un número entre 1 y 12.")

            case "2":
                infoAnual(comprovación_año, año)
                print("\n")

            case "3":
                print("Seleccione el TIPO de GRAFICO:")
                print("1 -> Gráfico DIARIO")
                print("2 -> Gráfico MENSUAL")
                print("3 -> Gráfico ANUAL")

                match userOp:
                    case "1":
                        infoDiariaGrafica(comprovación_año, año)
                    case "2":
                        infoMensualGrafica(comprovación_año, año)
                    case "3":
                        infoAnualGrafica(comprovación_año, año)
                    case _:
                        print("Ingrese una OPCIÓN VÁLIDA")

            case "4":
                filename = f"registroPluvial{año}_exportado.csv"
                comprovación_año.to_csv(filename)
                print(f"Datos exportados a {filename}")
                print("\n")
                userOp = input("Tipo de gráfico: ")

            # Opción secreta, la usamos para debugear un poco... ya la saco
            case "99":
                año = 2023  # o el año que desees
                comprovación_año = crearOcargar(año)
                print("Columnas disponibles:", comprovación_año.columns)
                infoDiariaGrafica(comprovación_año, año)

            case "0":
                print("Saliendo del menú...")
                break
            case _:
                print("Ingrese una OPCIÓN VÁLIDA")

# -- Comprueba si existe o no el ".CSV"(de no existir, lo crea) --> el corazón del menú
def crearOcargar(año):

    archivo = f"registro_pluvial_año_{año}.csv"

    if os.path.exists(archivo):
        # Si existe:
        cOc = pan.read_csv(archivo, index_col='Day')
        
        # Cambiar nombres de columnas a español!!!!!!
        cOc.columns = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

        """
        #COMPROBACIÓN -> Ya no es necesaria, pero me costó encontrar lo que rompia el código... así que la dejo de recuerdo XD

        print(cOc.head())  # Muestra las primeras filas del DataFrame
        print(cOc.columns)  # Imprime los nombres de las columnas
        """
    else:
        # Si NO existe:
        cOc = crearInfoPluvial(año)
        cOc.to_csv(archivo)
        #print(f"Datos guardados en {archivo}")
    return cOc

# -- Acá CREAMOS el ".CSV" --> Si la anterior es el corazón, esta es el ALMA!
def crearInfoPluvial(año):
    meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
    data = {mesee: np.random.uniform(0, 50, 31).round(1) for mesee in meses}  # Generar 31 días para cada mes
    
    # Rellenar con NaN donde no haya días
    for i, mesee in enumerate(meses):
        dias = dias_en_mes(año, i + 1)
        data[mesee][dias:] = np.nan  # Rellenar con NaN si hay menos de 31 días

    coc = pan.DataFrame(data)
    coc.index = range(1, 32)  # Establecer índice de 1 a 31
    coc.index.name = 'Day'
    
    return coc



# -- Funciones "TEMPROALES" --> Determinan mes y año (Necesarias para todo)

def dias_en_mes(año, mes):
    
    if 1 <= mes <= 12: # Verificar que el mes esté en el rango válido (1 a 12)
        _, dias = calendar.monthrange(año, mes) # calendar.monthrange devuelve un tupla con el primer día del mes y el número de días en el mes
        return dias
    else:
        return "Mes inválido. Debe ser un valor entre 1 y 12."
    


# -- 1) MOSTRAR MES --> Solo mostraos 1 mes del AÑO SELECCIONADO:
def mostrarMes(cOc, mes, año):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    print(f"Datos del MES: {meses[mes - 1]}, AÑO: {año}\n")
    totalDeDias = dias_en_mes(año, mes)

    # GRACIAS POR LA CORRECCION MUCHACHOS!!
    mes_nombre = cOc.columns[mes - 1]
    mes_data = cOc[mes_nombre].head(totalDeDias)


    #FORMATO DE COLUMNAS! (Encabezado, línea separadora, columna)
    print(f"{'Día':<5} {'Lluvia (mm)':<15}")
    print("-" * 20)

    for dia, lluvia in zip(mes_data.index, mes_data):
        print(f"{dia:<5} {lluvia:<15.1f}")

    print(f"TOTAL en {meses[mes-1]}: {mes_data.sum():.1f} mm")
    print(f"PROMEDIO en {meses[mes-1]}: {mes_data.mean():.1f} mm")



# -- 2) MOSTRAR AÑO --> Mostramos el AÑO SELECCIONADO:
def infoAnual(comprovación_año, año):
    print(f"\nResumen anual de lluvia para {año}:\n")
    
    totalAnual = comprovación_año.sum().sum()
    print(f"{'Total anual de lluvia:':<30} {totalAnual:.1f} mm")
    
    #FORMATO DE COLUMNAS! (Encabezado, línea separadora, columna)
    totalMensual = comprovación_año.sum()
    print("\nTotales mensuales:")
    print(f"{'Mes':<15} {'Total (mm)':<15}") 
    print("-" * 30)
    
    for month, total in totalMensual.items():
        print(f"{month:<15} {total:<15.1f}")

    print("\n")
    print(f"{'Mes más lluvioso:':<5} {totalMensual.idxmax()} con {totalMensual.max():.1f} mm")
    print(f"{'Mes menos lluvioso:':<5} {totalMensual.idxmin()} con {totalMensual.min():.1f} mm")


# -- 3) FUNCIONES GRÁFICAS --

# -- GRAFICO díario --> DISPERSIÓN
def infoDiariaGrafica(comprovación_año, año):
    plt.figure(figsize=(12, 8))
    meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
    data_available = False

    
    plt.gca().set_facecolor('#f0f0f0') # Color de fondo

    for month in range(1, 13):
        month_abbr = meses[month - 1]
        if month_abbr in comprovación_año.columns:
            month_data = comprovación_año[month_abbr]
            days = dias_en_mes(año, month)
            plt.scatter([month] * days, range(1, days + 1), 
                        c=month_data[:days], cmap='Blues', s=50, edgecolor='black')  # Color de borde
            data_available = True
        else:
            print(f"Warning: Month '{month_abbr}' does not exist in the DataFrame.")

    if data_available:
        plt.colorbar(label='Lluvia (mm)')
        plt.title(f'Distribución de Lluvia Diaria en Córdoba, Argentina - {año}', fontsize=16)
        plt.xlabel('Mes', fontsize=14)
        plt.ylabel('Día', fontsize=14)
        plt.yticks(range(1, 32, 5))
        plt.xticks(range(1, 13), meses)
        #plt.grid(color='white', linestyle='--')  # Añadir una cuadrícula
        plt.savefig(f'distribucion_lluvia_{año}.png')
        plt.show()
        plt.close()
        #print(f"Gráfico de dispersión guardado como 'distribucion_lluvia_{año}.png'")
    else:
        print("No se pudieron generar datos para crear el gráfico.")


# -- GRAFICO MENSUAL --> TORTA
def infoMensualGrafica(comprovación_año, año):
    monthly_totals = comprovación_año.sum()
    plt.figure(figsize=(10, 10))

    # Definir colores personalizados para el gráfico
    colores = ['#2a3835','#bed2d3','#92a9aa','#778d8e','#889ba4',
               '#27374D','#526D82','#9DB2BF','#DDE6ED','#243642',
               '#387478','#629584']

    # Crear el gráfico circular
    wedges, texts, autotexts = plt.pie(monthly_totals.values, 
                                       labels=monthly_totals.index, 
                                       autopct='%1.1f%%', 
                                       startangle=90, 
                                       colors=colores)


    # -- FORMATO:
    plt.setp(texts, size=12, weight="bold")  # Etiquetas
    plt.setp(autotexts, size=12, weight="bold", color='white')  # Porcentajes

    plt.title(f'Distribución Mensual de Lluvia en Córdoba, Argentina - {año}', fontsize=16, weight='bold')
    plt.axis('equal')  # Para asegurar que el gráfico es un círculo
    plt.savefig(f'distribucion_mensual_{año}.png')
    plt.show()
    plt.close()
    #print(f"Gráfico circular guardado como 'distribucion_mensual_{año}.png'")


# -- GRAFICO ANUAL --> Barras
def infoAnualGrafica(comprovación_año, año):
    monthly_totals = comprovación_año.sum()
    plt.figure(figsize=(12, 6))

    # Cambiar el color de fondo
    plt.gca().set_facecolor('#f0f0f0')  # Color de fondo gris claro

    # Cambiar colores de las barras
    bars = plt.bar(monthly_totals.index, monthly_totals.values, color='#889ba4', edgecolor='black')  # Color de borde negro

    plt.title(f'Distribución Anual de Lluvia en Córdoba, Argentina - {año}', fontsize=16)
    plt.xlabel('Mes', fontsize=14)
    plt.ylabel('Lluvia Total (mm)', fontsize=14)
    
    # Añadir etiquetas a las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.1f}', va='bottom', ha='center')

    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Añadir una cuadrícula en el eje y
    plt.savefig(f'lluvia_anual_{año}.png')
    plt.show()
    plt.close()
    #print(f"Gráfico de barras guardado como 'lluvia_anual_{año}.png'")



