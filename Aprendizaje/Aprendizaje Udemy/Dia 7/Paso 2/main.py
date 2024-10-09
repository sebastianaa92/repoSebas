import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
longitud = len(chosen_word)

adivinacion = input("Adivina la letra: ").lower()

# for letras in range(longitud):
#     print("_", end="")
#     if letras == adivinacion:
#             print(adivinacion, end="")
#     else: print("_", end="")

#MI SOLUCIÓN:

# for letter in chosen_word:
#       if letter == adivinacion:
#             print(adivinacion, end ="")
#       else: print("_", end="")

#SOLUCIÓN UDEMY:

display = ""

for letter in chosen_word:
      if letter == adivinacion:
            display += letter
      else: display += "_"

print(display)

# for letras in range(chosen_word,longitud):
#      if adivinacion == letras:
#          print("_")