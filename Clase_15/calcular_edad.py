from datetime import datetime

def calcular_anios(anio, mes, dia) :
    hoy = datetime.now()

    dif_anios = hoy.year - anio

    if hoy.month < mes and hoy.day < dia :
        dif_anios -= 1

    return dif_anios

edad = calcular_anios(1949, 1, 28)

print(f'Tienes {edad} años')