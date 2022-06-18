import random
def run():
  magic_number = random.randint(1, 100)
  print("Adivina el numero magico")
  user_number = int(input("Elige un numero del 1 al 100: "))
  count = 1
  while user_number != magic_number:
    if user_number > magic_number:
      user_number = int(input("Elige un numero mas pequeño: "))
    else:
      user_number = int(input("Elige un numero mas grande: "))
    count += 1
  print("Ganaste! 🥳️, en numero magico es " + str(user_number))
  print("Lo lograste en " + str(count) + " intentos")
if __name__ == "__main__":
  run() 