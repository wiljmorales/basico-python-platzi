import random
def run():
  magic_number = random.randint(1, 100)
  print("Adivina el numero magico")
  user_number = int(input("Elige un numero del 1 al 100: "))
  while user_number != magic_number:
    if user_number > magic_number:
      user_number = int(input("Elige un numero mas pequeño: "))
    elif user_number < magic_number:
      user_number = int(input("Elige un numero mas grande: "))
  print("Ganaste! 🥳️, en numero magico es " + str(user_number))

if __name__ == "__main__":
  run()