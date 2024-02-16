import random

#Get the input from the user
user_input1 = input("Please select a curtain (1,2 or 3): ")

if user_input1 in ['1','2','3']:
    #Definition of choices and probabilities
    choices = ['Car', 'Tiger']
    probability = [0.33, 0.66]

    #Select random value based on probabilities, store it in output1
    output1 = random.choices(choices, probability)[0]

    #prompt the user to confirm or his choise by yes or no
    user_input2 = input(f"Are you sure about your choice {user_input1} (yes or no) ")

    if user_input2.lower() == 'yes':
        print(f"Behind curtain {user_input1} is a {output1}")

    elif user_input2.lower() == 'no':
        # Prompt the user to choose a different option
        while True:
            new_user_input = input("Please select a different curtain: ")
            if new_user_input in ['1', '2', '3'] and new_user_input != user_input1:
                user_input1 = new_user_input
                break
            else:
                print("You already picked this curtain. Please choose a different number.")

        # Recalculate and display the outcome based on the new user choice
        output2 = random.choices(choices, probability)[0]
        print(f"You have changed your choice to curtain {new_user_input}. You get '{output2}'.")
        print(f"In curtain {user_input1} was a '{output1}'.")

    else:
        print("Invalid input. Please answer 'yes' or 'no'.")

else:
    print("Invalid input. Please choose 1, 2, or 3.")