import random


def random_generator():
    x = list(range(10))
    r = ""
    random.shuffle(x)
    for i in x:
        r += str(i)

    return r[:3]


def generate_clues(ai_guess, user_guess):
    clue = []

    for i in range(3):
        if ai_guess[i] == user_guess[i]:
            clue.append("Match")
        elif user_guess[i] in ai_guess:
            clue.append("Close")

    if clue == []:
        clue.append("Nope")
    return clue



ai_guess = random_generator()
print("Computer Value is generated\n")


user_guess = input("Guess a number of 3 digit : ")

i = ""
while i != "Code Cracked!!":
    if ai_guess == user_guess:
        i = "Code Cracked!!"
        for j in i:
            print(j)
        break

    print("Clues : ")
    clues = generate_clues(ai_guess, user_guess)
    for i in clues:
        print(i)
    user_guess = input("Guess a number of 3 digit : ")
