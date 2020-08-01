# pass in the dictionary containing all of the camels probabilities, prints the current probability of winning the leg
def print_leg_probabilities(camels):
    if sum(camels.values()) != 100:
        print("Error! Probabilities don't add up to 100%!")
    else:
        for element in camels:
            print(f"{element}: {camels[element]}%")
