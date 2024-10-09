import random
from hangman_art import stages
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
longitud = len(chosen_word)
lives = 6


blancos=""
game_over = False

for letras in range(longitud):
    print(blancos, end="")
    #blancos+= "_"
print(blancos)

letra_correcta = []

contador = 1


while contador < lives:
      
      adivinacion = input("Adivina la letra: ").lower()
      display = ""

      
      for letter in chosen_word:
          if letter == adivinacion:
              display += letter
              letra_correcta.append(adivinacion)
          elif letter in letra_correcta:
               display += letter
          else:
            display += "_"
     
      
      if adivinacion not in chosen_word:
           print(stages[contador])
           contador += 1


      print(display)

      if "_" not in display:
           game_over = True
           print("Ganaste")
      else: print(f"Te quedan {contador} vidas")

