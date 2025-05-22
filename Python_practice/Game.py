import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)  
"""

Paper="""  
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
li=[Rock,Paper,Scissor]
user=int(input("Enter the choice as number rock-0 , paper-1, sciccor-2: "))
computer =random.randint(0,2)

if user>=3 or user<0:
    print("Enter the Valid Choice Number ")
else:
    print("User Choice::::\n",li[user])
    print("Computer Choice::::\n",li[computer])
    if user==0 and computer==2:
        print("You Won! Rock smashed the scissor")
    elif computer==0 and user==2:
        print("Your are the looser! u are smashed")
    elif user>computer:
        print("You Won!")
    elif computer>user:
        print("You are the looser")
    elif user==computer:
        print("All Tie")
