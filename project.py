import random
randNumber=random.randint(1,100)

guesses=0
userGuess=None

while(userGuess!=randNumber):
  userGuess=int(input("Enter your guess: "))
  guesses+=1
  if(userGuess==randNumber):
    print("You guessed it right!")
  else:
      if(userGuess>randNumber):
          print("You guessed it wrong! Enter a smaller number")
      else:
          print("You guessed it wrong! Enter a greater number")

    
print(f"You guessed the number {guesses} guesses")   
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print("You habe just broken the high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
