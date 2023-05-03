move_that_beats = {
    "r" : "p",
    "p" : "s",
    "s" : "r"
}

move_that_loses = {
    "p" : "r",
    "s" : "p",
    "r" : "s"
}

import random

def opponent_random(my_history, their_history):
    # if no history, play random
    return "rps"[random.randint(0,2)]

def opponent_beat_last(my_history, their_history):
    # beat opponents last move
    if len(their_history) > 0:
        return move_that_beats[their_history[-1]]
    # if no history, play random
    return "rps"[random.randint(0,2)]

def opponent_copy_last(my_history, their_history):
    # copy opponents last move
    if len(their_history) > 0:
        return their_history[-1]
    # if no history, play random
    return "rps"[random.randint(0,2)]

def opponent_antibeat_last(my_history, their_history):
        # copy opponents last move
    if len(their_history) > 0:
        return move_that_loses[their_history[-1]]
    # if no history, play random
    return "rps"[random.randint(0,2)]


#opponents = [opponent_beat_last, opponent_copy_last, opponent_antibeat_last]

from opponents import opponents

buff = ""
games = 1000
game_len = 1000

for opponent in opponents:
    for _ in range(games):
        t1 = ""
        t2 = ""

        for __ in range(game_len):
            t1m = opponent(t1, t2)
            t2m = opponent_random(t2, t1)
            t1 += t1m
            t2 += t2m

        buff += t1 + "\n" + t2 + "\n\n"

with open("gen_huger.txt", "w") as f:
    f.write(buff)