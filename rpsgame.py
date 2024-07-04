import random
options = ["Rock", "Paper", "Scissors"]
uscore=0
cscore=0
while True:
  user_choice = input("Choose Rock, Paper, Scissors or Exit: ").title()
  computer_choice = random.choice(options)
  print("Computer chose: ", computer_choice)
  if user_choice=="Exit":
    break
  elif user_choice=="Rock":
    
    if computer_choice == "Rock":
      print("It's a tie!")
    elif computer_choice == "Scissors":
      print("You win!")
      uscore+=1 
    elif computer_choice == "Paper":
      print("Computer win!")
      cscore+=1
  elif user_choice=="Paper":
    
    if computer_choice == "Paper":
      print("It's a tie!")
    elif computer_choice == "Rock":
      print("You win!")
      uscore+=1 
    elif computer_choice == "Scissors":
      print("Computer win!")
      cscore+=1
  elif user_choice=="Scissors":
    
    if computer_choice == "Scissors":
      print("It's a tie!")
    elif computer_choice == "Paper":
      print("You win!")
      uscore+=1 
    elif computer_choice == "Rock":
      print("Computer win!")
      cscore+=1

print("Final Score :" )
print('Computer Score : ',cscore,'\nYour score: ',uscore)
if uscore==cscore:
  print("It's tie")
elif uscore>cscore:
  print('You win')
else:
  print('Computer win')



