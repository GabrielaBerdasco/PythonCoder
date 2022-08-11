from datetime import date

def calcula_edad(nacimiento):

  hoy = date.today()

  try:

    cumple = nacimiento.replace(year=hoy.year)

  except ValueError:

    cumple = nacimiento.replace(year=hoy.year, month=nacimiento.month + 1, day=1)

  if cumple > hoy:

    return hoy.year - nacimiento.year - 1

  else:

    return hoy.year - nacimiento.year

mi_nacimiento = date(1987, 12, 16)

mi_edad = calcula_edad(mi_nacimiento)

print(f"Tengo {mi_edad} años.")