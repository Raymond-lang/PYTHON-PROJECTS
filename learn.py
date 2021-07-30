
#EMAIL GENERATOR
import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

print (random_char(9)+"@gmail.com")
print (random_char(7)+"@gmail.com")
print (random_char(10)+"@yahoo.com")
print (random_char(7)+"@yahoo.com")
print (random_char(9)+"@gmail.com")
print (random_char(8)+"@yahoo.com")

#MADLIB

# adj = input("Adejective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous Person: ")

# madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \
#   I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

# print(madlib)

#Guessing game


#GUESSING GAME
# def guess(x):
#   random_number = random.randint(1, x)
#   guess = 0
#   while guess != random_number:
#     guess = int(input(f"Guess a number between 1 and {x}: "))
#     if guess < random_number:
#       print("Sorry, guess again. Too low.")
#     elif guess > random_number:
#       print("Sorry, guess again. Too high.")

#   print(f"Yay, congrats. You have guessed the number {random_number} correctly! ")

# guess(10)

#GUESSING GAME (USER)
# import random

# def computer_guess(x):
#   low = 1
#   high = x
#   feedback = ''
#   while feedback != 'c':
#     if low != high:
#       guess = random.randint(low, high)
#     else:
#       guess = low  # could also be high b/c low = high
#     feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
#     if feedback == 'h':
#       high = guess - 1
#     elif feedback == 'l':
#       low = guess + 1

# print(f'Yay! The computer guessed your number, {computer_guess} correctly')
# computer_guess(100)

#ROCK PAPER SCISSORS
# import random
#
# def play():
#   user = input("'r' for rock, 'p' for paper, 's' for scissors")
#   computer = random.choice(['r', 'p', 's'])
#



# print("I love you");
# num1, num2, num3, name = 5, 6, 2.4, "Raymond";
# print(num1);
# print(num2);
# print(num3);
# print(name);
# a = b = c = "equal";
# print(b)

# PI = 9
# print(PI);
# PI = 2;

# num1 = 0b0101 #binary
# num2 = 50 #decimal
# num3 = 0o310 #octal
# num4 = 0x12c #Hexa

# num5 = 11.7 #float literal
# num6 = 1.5e2

# num7 = 3.2j #complex

# print(num1);
# print(num2);
# print(num3);
# print(num4);
# print(num5);
# print(num6);
# print(num7);

# msg = "Python is fun";
# char = "F"
# multiLine = """This is
#             multiple line"""
# unicode = u"\u00dcnic\u00f6de"
# raw_string = r"raw \n sting!"

# print(msg);
# print(char);
# print(multiLine);
# print(unicode);
# print(raw_string);

# a = (1 == True);
# b = (1 == False);
# c = True + 5;
# d = False + 6;

# print(a);
# print(b);
# print(c);
# print(d);

# drink = "Availabe";
# food = None

# def new_menu(a):
#   if a == drink:
#     print(drink)
#   else:
#     print(food);
# new_menu(drink)
# new_menu(food)

# fruits = ["fig", "banana", "apple"] #List
# numbers = (1, 2, 3, 4) #tuple
# words = {"first word": "Banana", "second word": "Hi"}  #dict
# chars = {'A','B','C'} #set
# print(fruits);
# print(numbers);
# print(words);
# print(chars);

# x = 5
# y = 6.5
# z = 3 + 6j

# print(x, "is a type of", type(x))
# print(y, "is a type of", type(y))
# print(z, "is a type of", type(z))

# mix = [2, 3.5, 'Hello']
# print(mix);
# print("This is a type of", type(mix))
# print(mix[0:])

# mix[1] = 5;
# print(mix);

# mix = [4, 100, 43.4, "I don't care"];
# print(mix);

# mixT = (10, "app", 25, 4 + 5j)
# print(mixT);
# print(mixT[0:2])

# str = "I don't care about you fake niggas";
# newStr = '''I don't care about you
# fucking niggas, fuck off and
# go to bed.
# your ASS!!!'''

# print(newStr)
# print(newStr[0:5])

# newSet = {2, 6, 1, 7, 20}
# print(newSet)
# print(type(newSet));

# newD = {1: "I don't care", 2: "Let me know", "Third number": 5}
# print(newD);
# print(newD[2])

# print( '     /|')
# print( '    / |')
# print( '   /  |')
# print( '  /   |')
# print( '/     |')
# print( '------')

# import.math

# input = ("Tell me about you")
# print(input)

# name = input("What is your name?: ")
# print(name)

# school = "Federal University"
# print(len(school))
# print(school[3:])
# print(school.isupper())
# print(school.upper().isupper())
# print(school)
# print(school.upper())
# print(school.replace("Federal", "State"))
# print(school)
# print(school.index("Uni"))
# print(school.lower())
# print(school + " is a great school")
# print("I'm a good\nboy.\nI be good bad boy no choice\nbeen in the game not long\nsebi nah me sing akong\nmapariwo!\nExtra ordinary things I'm doing\nsing along! ALOUD!")

# myNum = 5
# print(float(myNum))
# num1 = int(input("Input your first number: "))
# num2 = int(input("Input your second number: "))
# result = [(num1 * num2), (num1 + num2), (num1 - num2), (num1 / num2)]
# print(result)

# MADLIBS GAME



# name = input("Enter a name: ")
# color = input("Enter a color: ")
# place = input.("Enter a place: ")
# thing = input("Enter a thing: ")
# attitude = input("Enter a attitude: ")
# conclusion = input("Enter a conclusion: ")

# print("My name is " + name)
# print("my favorite color is " + color)
# print("I'm the King of " + place)
# print("I really love to play with " + thing)
# print("I think your " + attitude + " is a result of how you are brought up")
# print("Let's be friends and enjoy ourselves " + conclusion)


#SIMPLE CALCULATOR
#This is a simple calculator.
#Instructions:
# (+) is for addition
# (-) is for subtraction
# (*) is for multipication
# (/) is for division
# (^) is for square
# (%) is for modulus
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator: ")
# num2 = float(input("Enter first number: "))

# if operator == "+":
#   print(num1 + num2)

# elif operator == "-":
#   print(num1 - num2)

# elif operator == "*":
#   print(num1 * num2)

# elif operator == "/":
#   print(num1 / num2)

# elif operator == "%":
#   print(num1 % num2)

# elif operator == "^":
#   print(num1 ** num2)

# else:
#   print("Error")

# #GUESSING GAME
# print("There is a number greater than 10, but less than 100\nit is divisible by 3,\ncan you guess the number?")
# guess1 = int(input("Put your first guess: "))

# if guess1 == 33:
#   print("WOW!!! You guessed right!")
# elif guess1 != 33:
#   print("Ohh you're wrong!")
#   print("Please try again you still have two more chances")

# guess2 = int(input("Put your second guess: "))

# if guess2 == 33:
#   print("WOW!! you guessed right!")

# elif guess2 != 33:
#   print("Ohh sorry again")
#   print("You have a last try")

# guess3 = int(input("Put your last guess: "))

# if guess3 == 33:
#   print("WOW!! you guessed right!")
# elif guess3 != 33:
#   print("GAME OVER")
#   print("The number is 33. Yooooo!")

#Working with lists
# names = ["Raymond", "Matthew", "Derrick", "Stephen", "David", "Gbenga", "Chris", "Timileyin", "Toluwani"]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8]
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))
# compile(names, numbers)

# hi = ['Hi'] * 4
# print(hi)

# numbers = [1, 3, 4, 6,] + [2, 5, 7]
# print(numbers)

# print(len([1, 2, 3]))

# print.isdecimal("Raymond")

# print(names[0:5])
# names.remove("Raymond")
# print(names)
# print(names)
# names.append("Raymond")
# print(names)
# names.pop()
# print(names)

# x = float(input("Put x value: __"))
# po = float(input("Enter your exponent: __"))

# if po == 3:
#   result = x * x * x
#   print(result)

# elif po == 2:
#   result = x * x
#   print(result)

# elif po == 4:
#   result = x * x * x * x
#   print(result)

# elif po == 5:
#   result = x * x * x * x * x
#   print(result)

# elif po == 6:
#   result = x * x * x * x * x * x
#   print(result)

# else:
#   print("Exponent can't exceed 6")


# def sayhi():
#   print("Hello World")
# sayhi()

# def sayhi(name):
# sayhi("Raymond")
# sayhi("Stephen")
#   (print("What's up " + name))

# print("Im")

# sayhi("Demola")



#MULTIPLE CHOICE QUESTIONS
# from question import Question
# question_prompts = [
#   "What color are apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#   "\nWhat color are strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
#   "\nWhat color are orange?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#   "\nWhat color are bananas?\n(a) Red/Green\n(b) Yellow\n(c) Orange\n\n"

# ]

# questions = [
#   Question(question_prompts[0], "a"),
#   Question(question_prompts[1], "a"),
#   Question(question_prompts[2], "c"),
#   Question(question_prompts[3], "b"),
# ]

# def run_test(questions):
#   score = 0
#   for question in questions:
#     answer = input(question.prompt)
#     if answer == question.answer:
#       score += 1
#   print("You got " + str(score) + "/" + str(len(questions)) + "correct")
# run_test(questions)

#CLASSES AND OBJECTS
