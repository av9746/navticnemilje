import random
import os

# draw grid
#pick random location for player
#pick random location for monster
#pick random location for door
#draw player in grid
#take input for ovement
#move player
#check win loss
#clear screen redraw grid


CELLS = [
    (0,0), (0,1), (0,2), (0,3), (0,4),
    (1,0), (1,1), (1,2), (1,3), (1,4),
    (2,0), (2,1), (2,2), (2,3), (2,4),
    (3,0), (3,1), (3,2), (3,3), (3,4),
    (4,0), (4,1), (4,2), (4,3), (4,4)
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_locations():
    return random.sample(CELLS,3)

def move_player(player, move):
    x,y = player

    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")

    return moves

def draw_map(player):
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "/n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, line_end)


def game_loop(player, monster, door):
    while True:
        valid_moves = get_moves(player)
        print("You are courently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")

        move = input("> ").upper()

        if move == "QUIT":
            print("Thanks for playing")
            break
        if move in valid_moves:
            player = move_player(player, move)
        else:
            input("Ouch walls are hard")



monster, door, player = get_locations()



print("Welcome to the dungeon!")
input("Press return to start")
game_loop()

