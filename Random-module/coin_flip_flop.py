"flip- flop game using python"
import random

user = str(input("enter 'head' or 'tail': "))
computer = random.choice(["head", "tail"])

if user == computer:
    print("you win")
else:
    print("you loss")