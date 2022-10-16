Win = "Correct +1"
Lose = "Wrong is was"
score = 0

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
if Q5 == "season 9" or Q5 == "s9" or Q5 == "5":
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

