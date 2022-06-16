menu = """
Bienvenido a mi exchange 💰️

1 - Pesos colombians
2 - Pesos argentinos
3 - Bolivares

Elige una opción: 
"""

option = int(input(menu))

if option == 1:
  pesos = input("¿Cuantos pesos colombianos tienes?: ")
  pesos = float(pesos)
  valor_dolar = 3875
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  print(f"Tienes ${dolares} dolares.")
elif option == 2:
  pesos = input("¿Cuantos pesos argentinos tienes?: ")
  pesos = float(pesos)
  valor_dolar = 65
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  print(f"Tienes ${dolares} dolares.")
elif option == 3:
  pesos = input("¿Cuantos bolivares tienes?: ")
  pesos = float(pesos)
  valor_dolar = 5.3
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  print(f"Tienes ${dolares} dolares.")
else:
  print("Por favor elige una opcion corecta")
