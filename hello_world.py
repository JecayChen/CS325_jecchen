import random

again = bool(True)
correct = bool(True)
print("Coinflip")

while again:
    rand = int(random.randint(0,1))
    if rand == 0:{
        print("Heads")
    }
    else:{
        print("Tails")
    }
    while not correct: 
        again = input("Flip again (True/False)?:")
    correct = True