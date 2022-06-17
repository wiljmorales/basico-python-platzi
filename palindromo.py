def palindromo(word):
  word = word.replace(" ", "").lower()
  return word == word[::-1]

def run():
  word = input("Escribe una palabra: ")
  if palindromo(word):
    print(word + " es palindromo.")
  else:
    print(word + " no es palindromo.")

if __name__ == "__main__":
  run()