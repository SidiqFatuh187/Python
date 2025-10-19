Name = "Sidiq"
Age = 19
Height = 173
Hobby = "Palying Game"

print("Name:", Name)
print("Age:", Age)
print("Height:", Height)
print("Hobby:", Hobby)

user_name = input("What is your name:")
print("Hello Welcome ," + user_name + "<3" )

#Kabar
user_info = input("How are you?")
if user_info.lower() in "i'm not fine" or user_info.lower() in "im not fine":
    print("Get Well soon <3")
elif user_info.lower() in "i'm fine" or user_info.lower() in "im fine":
    print("Have a nice day!")
else:
    print("Thanks For Sharing!")

def say_Hello(person_name):
    print("Hello, " + person_name + " You are so cute")
    
say_Hello("Arbian")
say_Hello("Veinaa")
say_Hello("Sidiq")
say_Hello("Fanny")

Age =int(input("enter your Age:"))
if Age <= 18 :
    print("you are Minor")
elif Age >= 20 :
    print("you are Tennagers")
    
def Multiplay(A, B):
    return A * B
result = Multiplay(10, 20)
print("Result", result)