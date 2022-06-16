# def print_mesage():
#   print("Mensaje especial")
#   print("¡Estoy aprendiendo a usar funciones!")

# print_mesage()
# print_mesage()
# print_mesage()

option = int(input("Elige una opción"))

def conversation(option):
  print("hola")
  print("¿Cómo estas?")
  print(f"Elegiste la opción {option}")
  print("Adios")

if option == 1:
  conversation(1)
elif option == 2:
  conversation(2)
elif option == 3:
  conversation(3)
else: 
  print("Opcion invalida")