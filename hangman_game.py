import random
import hangman_stages
import word_file_hangman
lives= 6
chosen_word = random.choice(word_file_hangman.words)
display = []
for i in chosen_word :
   i ="_"
   display.append(i)
print(display)
game_over = False
while not game_over:
   guessed_letter = input("Guess a letter: ").lower()
   for j in range(len(chosen_word)):
      letter = chosen_word[j]
      if letter == guessed_letter:
         display[j] = guessed_letter
   print(display)
   if guessed_letter not in chosen_word:
      lives -= 1
      if lives == 0:
         game_over = True
         print("You Lose!!")
   if "_" not in display:
      game_over = True
      print("You win !!")
   print(hangman_stages.stages[lives])



