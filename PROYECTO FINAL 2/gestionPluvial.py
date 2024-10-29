import calendar
import os
import pandas as pan
import numpy as np
import matplotlib.pyplot as plt
from colores import *

"""
 
▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▄  ▗▄▖  ▗▄▄▖
▐▛▚▞▜▌▐▌     █ ▐▌ ▐▌▐▌  █▐▌ ▐▌▐▌   
▐▌  ▐▌▐▛▀▀▘  █ ▐▌ ▐▌▐▌  █▐▌ ▐▌ ▝▀▚▖
▐▌  ▐▌▐▙▄▄▖  █ ▝▚▄▞▘▐▙▄▄▀▝▚▄▞▘▗▄▄▞▘

"""

# -- Comprueba si existe o no el ".CSV"(de no existir, lo crea) --> el corazón del menú
def crearOcargar(año):
    # Definir la ruta al archivo dentro de 'datosAnalizados'
    archivo = os.path.join('datosAnalizados', f"registro_pluvial_año_{año}.csv")

    if os.path.exists(archivo):
        # Si existe, cargar el archivo .csv
        cOc = pan.read_csv(archivo, index_col='Day')
        
        # Cambiar nombres de columnas a español
        cOc.columns = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
        
        # Comprobación opcional
        # print(cOc.head())  # Muestra las primeras filas del DataFrame
        # print(cOc.columns)  # Imprime los nombres de las columnas
    else:
        # Si no existe, crear el DataFrame con la información pluvial y guardarlo
        cOc = crearInfoPluvial(año)
        cOc.to_csv(archivo)
        # print(f"Datos guardados en {archivo}")

    return cOc

# -- Acá CREAMOS el ".CSV" --> Si la anterior es el corazón, esta es el ALMA!
def crearInfoPluvial(año):
    meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
    data = {mes: np.random.uniform(0, 50, 31).round(1) for mes in meses}  # Generar 31 días para cada mes
    
    # Rellenar con NaN donde no haya días
    for i, mes in enumerate(meses):
        dias = dias_en_mes(año, i + 1)
        data[mes][dias:] = np.nan  # Rellenar con NaN si hay menos de 31 días

    coc = pan.DataFrame(data)
    coc.index = range(1, 32)  # Establecer índice de 1 a 31
    coc.index.name = 'Day'
    
    # Guardar el archivo en la carpeta 'datosAnalizados'
    carpeta = 'datosAnalizados'
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)  # Crear la carpeta si no existe
    
    archivo = os.path.join(carpeta, f"registro_pluvial_año_{año}.csv")
    coc.to_csv(archivo)  # Guardar el archivo en la ruta especificada
    
    return coc



# -- Funciones "TEMPROALES" --> Determinan mes y año (Necesarias para todo)

def dias_en_mes(año, mes):
    
    if 1 <= mes <= 12: # Verificar que el mes esté en el rango válido (1 a 12)
        _, dias = calendar.monthrange(año, mes) # calendar.monthrange devuelve un tupla con el primer día del mes y el número de días en el mes
        return dias
    else:
        return "Mes inválido. Debe ser un valor entre 1 y 12."
    


# -- 1) MOSTRAR MES --> Solo mostraos 1 mes del AÑO SELECCIONADO:
def mostrarMes(cOc, mes, año, opcion: int):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    totalDeDias = dias_en_mes(año, mes)
    mes_nombre = cOc.columns[mes - 1]
    mes_data = cOc[mes_nombre].head(totalDeDias)

    if opcion == 1:
        print(f"{BLUE}Datos del MES: {meses[mes - 1]}, AÑO: {año}\n")
        
        #FORMATO DE COLUMNAS! (Encabezado, línea separadora, columna)
        print(f"{'Día':<5} {'Lluvia (mm)':<15}")
        print("-" * 20)

        for dia, lluvia in zip(mes_data.index, mes_data):
            print(f"{dia:<5} {lluvia:<15.1f}")

        # Calcular mínimo y máximo
        minimo = mes_data.min()
        maximo = mes_data.max()
        print(f"\nMínimo en {meses[mes-1]}: {minimo:.1f} mm")
        print(f"Máximo en {meses[mes-1]}: {maximo:.1f} mm{RESET}")

    else:
        if mes_data is not None:  # Verificar que mes_data fue asignado
            print("\n")
            print(f"{BLUE}TOTAL en {meses[mes-1]}: {mes_data.sum():.1f} mm")
            print(f"PROMEDIO en {meses[mes-1]}: {mes_data.mean():.1f} mm{RESET}")
        else:
            print("No se han obtenido datos para el mes solicitado.")


# -- 2) MOSTRAR AÑO --> Mostramos el AÑO SELECCIONADO:
def infoAnual(comprovación_año, año):
    print(f"{BLUE}\nResumen anual de lluvia para el año {año}:")
    
    totalAnual = comprovación_año.sum().sum()
    print(f"{'Total anual de lluvia:':<30} {totalAnual:.1f} mm")
    
    #FORMATO DE COLUMNAS! (Encabezado, línea separadora, columna)
    totalMensual = comprovación_año.sum()
    #print("\nTotales mensuales:")
    #print(f"{'Mes':<15} {'Total (mm)':<15}") 
    #print("-" * 30)
    
    # for month, total in totalMensual.items():
    #     print(f"{month:<15} {total:<15.1f}")

    print(f"{'Mes más lluvioso:':<5} {totalMensual.idxmax()} con {totalMensual.max():.1f} mm")
    print(f"{'Mes menos lluvioso:':<5} {totalMensual.idxmin()} con {totalMensual.min():.1f} mm{RESET}")


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
            print(f"{RED}Warning: Mes '{month_abbr}' no existe en el DataFrame!!!.{RESET}")

    if data_available:
        plt.colorbar(label='Lluvia (mm)')
        plt.title(f'Distribución de Lluvia Diaria en Córdoba, Argentina - {año}', fontsize=16)
        plt.xlabel('Mes', fontsize=14)
        plt.ylabel('Día', fontsize=14)
        plt.yticks(range(1, 32, 5))
        plt.xticks(range(1, 13), meses)
        #plt.grid(color='white', linestyle='--')  # Añadir una cuadrícula
        os.makedirs('datosAnalizados', exist_ok=True)
        plt.savefig(f'datosAnalizados/grafico_dispersion_{año}.png')
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

    os.makedirs('datosAnalizados', exist_ok=True) #Si no exite la carpeta
    plt.title(f'Distribución Mensual de Lluvia en Córdoba, Argentina - {año}', fontsize=16, weight='bold')
    plt.axis('equal')  # Para asegurar que el gráfico es un círculo
    plt.savefig(f'datosAnalizados/torta{año}.png')
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
    
    carpeta_destino = 'datosAnalizados'

    os.makedirs(carpeta_destino, exist_ok=True)
    plt.savefig(os.path.join(carpeta_destino, f'lluvia_anual_{año}.png'))
    plt.show()
    plt.close()
    #print(f"Gráfico de barras guardado como 'lluvia_anual_{año}.png'")

def graficoTortaDiario(comprovación_año, año, mes):
    # Nombres de los meses para etiqueta y colores personalizados
    meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
    
    # Verificar que el mes solicitado sea válido y exista en el DataFrame
    if mes < 1 or mes > 12:
        print("Error: Mes inválido. Debe estar entre 1 y 12.")
        return

    month_abbr = meses[mes - 1]
    if month_abbr not in comprovación_año.columns:
        print(f"Advertencia: No hay datos para el mes '{month_abbr}' en el DataFrame.")
        return

    # Extraer datos de lluvia para el mes especificado y eliminar valores NaN
    lluvia_mensual = comprovación_año[month_abbr].dropna()
    days = [f'Día {i+1}' for i in lluvia_mensual.index]

    # Configuración de colores y gráfico de torta
    plt.figure(figsize=(16, 12))  # Aumentar el tamaño de la figura
    colores = plt.cm.Blues(range(len(lluvia_mensual)))

    wedges, texts, autotexts = plt.pie(
        lluvia_mensual,
        labels=days,
        autopct='%1.1f%%',
        startangle=90,
        colors=colores,
        wedgeprops={'edgecolor': 'gray', 'linewidth': 1}  # Borde gris y más grueso
    )
    
    # Formateo de etiquetas y porcentajes
    for text in texts:
        text.set_fontsize(12)  # Aumentar tamaño de las etiquetas
        text.set_fontweight('bold')
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(10)  # Aumentar tamaño de los porcentajes
        autotext.set_fontweight('bold')

    # Título y ajustes finales
    plt.title(f'Distribución de Lluvia en {month_abbr.capitalize()} {año}', fontsize=22, fontweight='bold', color='#4b6f94')
    plt.axis('equal')  # Asegura que el gráfico sea circular
    
    # Guardar el gráfico en la carpeta datosAnalizados
    carpeta_destino = 'datosAnalizados'
    os.makedirs(carpeta_destino, exist_ok=True)
    plt.savefig(os.path.join(carpeta_destino, f'distribucion_lluvia_{month_abbr}_{año}.png'))
    plt.show()
    plt.close()


""" 
    
        ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖ ▗▄▄▖
        ▐▛▚▞▜▌▐▌   ▐▛▚▖▐▌▐▌ ▐▌▐▌   
        ▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌▐▌ ▐▌ ▝▀▚▖
        ▐▌  ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘▗▄▄▞▘

"""

def menu_lluvia() :

    # -- MENÚ PLUVIAL --
    # Desde este menú, vamos a llamar a Metodos del Modulo Pluvial (Estadísticas y Gŕaficos)

    print(f"{BLUE}\n")
    print("  __  __  ______  _   _    __    _____   _      _    _ __      __ _____            _      ")
    print(" |  \/  ||  ____|| \ | | _/_/_  |  __ \ | |    | |  | |\ \    / /|_   _|    /\    | |     ")
    print(" | \  / || |__   |  \| || | | | | |__) || |    | |  | | \ \  / /   | |     /  \   | |     ")
    print(" | |\/| ||  __|  | . ` || | | | |  ___/ | |    | |  | |  \ \/ /    | |    / /\ \  | |     ")
    print(" | |  | || |____ | |\  || |_| | | |     | |____| |__| |   \  /    _| |_  / ____ \ | |____ ")
    print(f" |_|  |_||______||_| \_| \___/  |_|     |______|\____/     \/    |_____|/_/    \_\|______|{RESET}")

    año = int(input("\nIngrese el AÑO que desee conocer: "))

    comprovación_año = crearOcargar(año)

    print(f"{BLUE}\nRegistro N° {año} cargado, seleccione como proseguir:{RESET}")

    while True:
        
        print("\n1 -> Minimo, Maximo y Promedios del Año")
        print("2 -> Crear Graficos")
        print("3 -> Analisis Mensual")
        print(f"{RED}\n4 -> Regresar{RESET}")
        print("...........")

        userOp = int(input("Opción: "))
        print("\n")
        
        match userOp:
            case 1:
                infoAnual(comprovación_año, año)
            case 2:
                menuGraficos(comprovación_año, año)
            case 3:
                menuMensual(comprovación_año, año)
            case _:
                print("Regresando...")
                break


def menuGraficos(comprovación_año, año):

    print("\n1 -> Grafico Anual: Barras")
    print("2 -> Grafico de Dispersión")
    print("3 -> Grafico Mensual: Torta")
    print(f"{RED}\n4 -> Regresar{RESET}")
    print("...........")

    userOp = int(input("Opción: "))

    while True:
        match userOp:
            case 1:
                infoAnualGrafica(comprovación_año, año)
                break
            case 2:
                infoDiariaGrafica(comprovación_año, año)
                break
            case 3:
                infoMensualGrafica(comprovación_año, año,)
                break
            case _:
                break

def menuMensual(comprovación_año, año):

    mes = int(input("Ingrese el número del mes: "))

    while True:

        print("\n1 -> Registros diários")
        print("2 -> Minimo, Maximo y Promedio por Mes")
        print("3 -> Grafico Diario")
        print(f"{RED}\n4 -> Regresar{RESET}")
        print("...........")

        userOp = int(input("Opción: "))

        match userOp:
            case 1:
                if 1 <= mes <= 12:
                    mostrarMes(comprovación_año, mes, año,1)
                else:
                    print("Mes inválido. Por favor ingrese un número entre 1 y 12.")
            case 2:
                mostrarMes(comprovación_año, mes, año, 2)
            case 3:
                graficoTortaDiario(comprovación_año, año, mes)
            case _:
                print("Regresando...")
                break

