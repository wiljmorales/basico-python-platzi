menu = """
Bienvenido a mi exchange 💰️

1 - Pesos colombians
2 - Pesos argentinos
3 - Bolivares

Elige una opción: 
"""

option = int(input(menu))

def exchange(currency, exchange_rate):
  pesos = input(f"¿Cuantos {currency} tienes?: ")
  pesos = float(pesos)
  dolares = pesos / exchange_rate
  dolares = round(dolares, 2)
  print(f"Tienes ${dolares} dolares.")


if option == 1:
  exchange("pesos colombianos", 3891)
elif option == 2:
  exchange("pesos argentinos", 122.91)
elif option == 3:
  exchange("bolivares", 5.74)
else:
  print("Por favor elige una opcion corecta")