science = str(input("Are you interested in computer science? (Y/N): "))
games = str(input("Do you like playing computer games? (Y/N): "))
ig_account = str(input("Do you have an Instagram account (Y/N): "))
y_n = 0
def yes_no(x):
    if x == "Y":
        return True
    else:
        return False
if yes_no(science) == True:
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")
if yes_no(games) == True:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")
if yes_no(ig_account) == True:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")