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


ai_guess = "123"

user_guess = "456"

clues = generate_clues(ai_guess, user_guess)

for i in clues:
    print(i)
