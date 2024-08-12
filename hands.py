import random

print("welcome to your favorite stone paper siccors")

user = input("r for rock, p for paper, s for siccors :")
    
computer = random.choice(['r','p','s'])
print("computer chose ", computer)
if (user == computer):
    print('its a tie')
elif ( user == "p" and  computer == "r") or ( user == "r" and  computer == "s") or ( user == "s" and  computer == "p"):
    print("you won")
else:
    print("you lost")