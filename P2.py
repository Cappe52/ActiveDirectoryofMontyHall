import random

options = ['Car','Tiger']

#Function for setting up three curtains. It takes in count that a tiger can be chosen twice and the car only once.
def variablessetup():
    car_count = 0
    tiger_count = 0

    c1 = random.choice(options)

    if c1 == 'Car' and car_count == 0:
        car_count += 1
    elif c1 == 'Tiger' and tiger_count < 2:
        tiger_count += 1
    else:
        return variablessetup()


    c2 = random.choice(options)

    if c2 == 'Car' and car_count == 0:
        car_count += 1
    elif c2 == 'Tiger' and tiger_count < 2:
        tiger_count += 1
    else:
        return variablessetup()


    c3 = random.choice(options)

    if c3 == 'Car' and car_count == 0:
        car_count += 1
    elif c3 == 'Tiger' and tiger_count < 2:
        tiger_count += 1
    else:
        return variablessetup()

    return c1, c2, c3


result = variablessetup()
#print(type(result))''

#Prompt the user to select a curtain.
while True:
    user_input1 = input("Which curtain do you choose (1, 2 or 3): ")

    if user_input1 not in['1', '2', '3']:
        print("Invalid input, please select a correct value (1, 2, or 3).")
    else:
        user_input1 = int(user_input1)
        curtains = [1, 2, 3]
        curtains.remove(user_input1)

        valid_curtain = [curtain for curtain in curtains if result[curtain - 1] == 'Tiger']

        if valid_curtain:
            revealed_curtain = random.choice(valid_curtain)
        else:
            revealed_curtain = random.choice(curtains)

        print(f"Under curtain {revealed_curtain} is a {result[revealed_curtain - 1]}...")
        break


user_input2 = input("Do you want to stay with your initial choice? (yes / no): ").lower()

while True:
    try:
        if user_input2 == "yes":
            print(f"Behind curtain {user_input1} is a {result[user_input1 - 1]}")

            if result[user_input1-1] == 'Tiger':
                print(f"You loose.")
                Game_result = 'Loss'
            elif result[user_input1-1] == 'Car':
                print(f"You win!")
                Game_result = 'Win'
            break

        if user_input2 == "no":
            while True:
                user_input3 = int(input("Please select a different curtain: "))
                if user_input3 in [1, 2, 3] and user_input3 != (user_input1):
                    revealed_curtain = user_input3
                    break
                else:
                    print("You already picked this curtain. Please choose a different number.")

            print(f"Behind curtain {revealed_curtain} is a {result[revealed_curtain-1]}")

            if result[revealed_curtain-1] == 'Tiger':
                print(f"You loose.")
                Game_result = 'Loss'

            elif result[revealed_curtain-1] == 'Car':
                print(f"You win!")
                Game_result = 'Win'
            break

    except ValueError:
        print("Invalid input - please try again.")

with open("game_results.txt", "a") as file:
    file.write(f"{user_input1}, {user_input2}, {user_input2}, {Game_result}\n")
