Win = "Correct +1"
Lose = "Wrong it was"
score = 0
birthday = 0

print("Welcome to my Fortnite quiz!")
print()

name = input("What is your name? ")

yes_no = input("Have you have your birthday this year? ").lower()
if yes_no == "yes" or yes_no == "y":
    birthday =+ 2022
else:
    birthday =+ 2021

def num_check(question, low, high):
   error = "Please enter an  number between 1900 and 2022\n"

   valid = False
   while not valid:
       try:
           response = int(input(question))
           if low < response <= high:
               return response


           else:
               print(error)

       except ValueError:
           print(error)


year = num_check("when were you born? ", 1900, 2022)

age = birthday - year
print("Your age is {}".format(age))

start = input("Press enter to start...")
if start == "":
    print("")
else:
    print("")

Q1 = input("What colour the rare rarity? ").lower()
if Q1 == "blue":
    print(Win)
    score += 1

else:
    print("{} blue".format(Lose))

print()
Q2 = input("What colour is the Epic rarity? ").lower()
if Q2 == "purple":
    print(Win)
    score += 1

else:
    print("{} purple".format(Lose))

print()
Q3 = input("What Colour is the Legendary rarity? ").lower()
if Q3 == "gold" or Q3 == "yellow":
    print(Win)
    score += 1

else:
    print("{} gold".format(Lose))

print()
Q4 = input("How much people are in a fortnite match? ").lower()
if Q4 == "100 players" or Q4 == "100":
    print(Win)
    score += 1

else:
    print("{} 100 players".format(Lose))

print()
print("That was easy im gonna increase the difficulty to medium level")
print("your score is {} ".format(score))

print()
Q5 = input("What season (not chapter) was the combat shotgun added? ").lower()
if Q5 == "season 9" or Q5 == "s9" or Q5 == "9":
    print(Win)
    score += 1

else:
    print("{} season 9".format(Lose))

print()
Q6 = input("What season (not chapter) was primal season? ").lower()
if Q6 == "season 15" or Q6 == "s15" or Q6 == "15":
    print(Win)
    score += 1

else:
    print("{} season 15".format(Lose))

print()
Q7 = input("What season (not chapter) was flick lock added?").lower()
if Q7 == "season 8" or Q7 == "s8" or Q7 == "8":
    print(Win)
    score += 1

else:
    print("{} season 8".format(Lose))

print()
print("That was easy im gonna increase the difficulty to hard level")
print("your score is {} ".format(score))

print()
Q8 = input("What season (not chapter) was spider-man added? ").lower()
if Q8 == "s19" or Q8 == "season 19" or Q8 == "19":
    print(Win)
    score += 1

else:
    print("{} season 19".format(Lose))

print()
Q9 = input("What is fortnite: battle royale release date? ").lower()
if Q9 == "2017":
    print(Win)
    score += 1

else:
    print("{} 2017".format(Lose))

print()
Q10 = input("What is the most used pickaxe? ").lower()
if Q10 == "the reaper" or Q10 == "reaper":
    print(Win)
    score += 1

else:
    print("{} the reaper pickaxe".format(Lose))

print()

if score == 0:
    print("WOW! you got 0 you really dont know much about fortnite")
else:

    print("Good job you got {} out of 10 questions".format(score))

