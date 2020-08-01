# pass in the dictionary containing all of the camels probabilities, prints the current probability of winning the leg
def print_leg_probabilities(camels):
    if sum(camels.values()) != 100:
        print("Error! Probabilities don't add up to 100%!")
        quit()
    else:
        for element in camels:
            print(f"{element}: {camels[element]}%")

def initialize_gameboard():
    game_board = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
        16: []
    }
    return game_board

def initialize_camels():
    camels = {
        "orange": 20,
        "blue": 20,
        "yellow": 20,
        "green": 20,
        "white": 20,
    }
    return camels

def prompt_turn():
    while True:
        response = input("Are you rolling, betting, or placing a tile? (roll, bet, tile) ")
        if response not in ('roll', 'bet', 'tile'):
            print("Sorry, please enter roll, bet, or tile")
        else:
            return response
