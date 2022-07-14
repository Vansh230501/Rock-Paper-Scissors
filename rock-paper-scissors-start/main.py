rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
actions = [rock,paper,scissors]
n = random.randint(0,2)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(actions[user_input])
print("Computer chose:")
print(actions[n])

if (n == user_input):
  print("The match is drawn..")
elif (user_input == 0 and n == 1):
  print("You lose")
elif (user_input == 0 and n == 2):
  print("You win")
elif(user_input == 1 and n == 2):
  print("You lose")
elif(user_input == 1 and n == 0):
  print("You win")
elif(user_input == 2 and n == 0):
  print("You lose")
else:
  print("You win")  
  