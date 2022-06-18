def prime(num):
  for i in range(1,num):
    if i == 1 or i == num:
      continue
    if num % i == 0:
      return False
    if i >= num / 2:
      return True

def run():
  number = int(input("Ingresa un numero: "))

  if prime(number):
    print(f"{str(number)} es primo 🥳️")
  else:
    print(f"{str(number)} no es primo 😮‍💨️")
  
  keep_running()

  
def keep_running():
  stop_program = input("Quieres cerrar el programa?[S/N] ").lower()
  
  if stop_program == "s":
    print("cerrando el programa")
    print("adios")
  elif stop_program == "n":
    run()
  else:
    print("ingrese \"S\" para cerrar o \"N\" para continuar")
    keep_running()

if __name__ == "__main__":
  run()