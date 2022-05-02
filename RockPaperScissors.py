import random
user_action=input('Please enter rock, paper, or scissors: ')
possible_action=['rock','paper', 'scissors']
computer_action=random.choice(possible_action)
print('You chose:' + user_action + '. Computer chose:' + computer_action)
def apple():
   while True:
       try:
           if user_action not in computer_action:
               raise ValueError
       except ValueError:
           print("You must enter rock, paper, or scissors")
           break #this stops running the try except funtion
if user_action==computer_action:
   print('Both players selected' + user_action + '. It is a tie')
elif user_action=='rock':
   if computer_action=='scissors':
       print('Rock smashes scissors. You win:)')
   else:
       print('Paper covers rock. You lose.')
elif user_action=='scissors':
   if computer_action=='paper':
       print('Scissors cuts paper. You win:)')
   else:
       print('Rock smashes scissors. You lose.')
elif user_action=='paper':
   if computer_action=='rock':
       print('Paper covers rock. You win:)')
   else:
       print('Scissors cuts paper. You lose.')