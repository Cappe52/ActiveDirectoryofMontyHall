
import random
import pandas as pd
import matplotlib.pyplot as plt

options = ['Car', 'Tiger']
results = []

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


def simulate_games():
    stay_wins = 0
    stay_losses = 0
    change_wins = 0
    change_losses = 0

    for i in range(2000):
        result = variablessetup()
        user_input1 = random.randint(1,3) # Randomly choose a curtain

        # Randomly choose whether the user stays or changes
        stay = random.choice([True, False])

        # Determine the revealed curtain
        curtains = [1, 2, 3]

        #if user_input1 in curtains:
        curtains.remove(user_input1)  # Remove user's choice only if it's in the list
        valid_curtain = [curtain for curtain in curtains if result[curtain - 1] == 'Tiger']
        revealed_curtain = random.choice(valid_curtain) if valid_curtain else random.choice(curtains)

        if stay:
            final_choice = user_input1
        else:
            curtains.remove(revealed_curtain)
            final_choice = curtains[0]

        if result[final_choice - 1] == 'Car':
            if stay:
                stay_wins += 1
            else:
                change_wins += 1

        if result[final_choice - 1] == 'Tiger':
            if stay:
                stay_losses += 1
            else:
                change_losses += 1

        data = {"wins_stay": stay_wins, "loss_stay": stay_losses, "win_change": change_wins, #Why this?
                "loss_change": change_losses}

        results.append(data) #why this?

simulate_games()

df = pd.DataFrame(results)

df = pd.read_json("monty_hall_results.json")

wins_stay = df["wins_stay"]
loss_stay = df["loss_stay"]
win_change = df["win_change"]
loss_change = df["loss_change"]

x = range(len(df))
plt.plot(x, wins_stay, label="Wins if stayed at original curtain")
plt.plot(x, win_change, label="Wins if changed to new curtain")
plt.xlabel("Games")
plt.ylabel("Count")
plt.title("Monty Hall Game Results")
plt.legend()
plt.show()
