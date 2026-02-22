print("Hello Sidiq")

Name = "Sidiq"
Age = 18
Height = 173
is_gamer = True

print("Name:", Name)
print("Age:", Age)
print("Height:", Height)
print("is gamer:?", is_gamer)

User_name = input("What is your Name?")
print("Welcome, " + User_name + "!")

x = 3
y = 10

print(x + y)
print(y - x)
print(x * y)
print(y / x)
print(y // x)
print(y % x)
print(y ** x)

Age = int(input("Enter your Age: "))
if Age >= 18:
    print("you are adult")
elif Age >= 15:
    print("you are tennager.")
else:
    print("You are a minor.")
    
count = 0
while count < 10:
    print("count is:", count)
    count += 1
    
video_games = ["Game 1", "Game 2", "Game 3", ]
#print video_games([0])

video_games.append("Game 4")
print(video_games)

#for game in video_games:
    #print(game)
    
def say_Hello(person_name):
    print("Hello, " + person_name + " your so cute")
    
say_Hello("Nana")
say_Hello("Sidiq")
say_Hello("Veinaa")
say_Hello("Arbian")

def Multiplay(a, b):
    return a * b
result = Multiplay(3, 15)
print("Result: ", result)

import random

secret_number = random.randint(1, 10)
attempts = 3
print("im thingking of a number between 1 and 10")
while attempts > 0:
    guess = int(input("take a guess: "))
    if guess == secret_number:
        print("congratulasion! you guessed the number")
        break
    elif guess < secret_number:
        print("Too low, try again")
    else:
        print("Too High, try again")
    attempts -= 1    
    if attempts == 0:
        print("Sorry, you,ve run out of attempts. the secret number was:", secret_number)