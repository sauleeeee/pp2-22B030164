import random
name = input("Hello! What is your name?\n")

rand = random.randrange(1, 20)
cnt= 0

print( f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")

while True:
    guess = int(input())
    cnt+=1
    if guess == rand:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    else:
        print("Your guess is too low. \
                    \nTake a guess.")