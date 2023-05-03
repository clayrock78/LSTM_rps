move_that_beats = {
    "r":"p",
    "p":"s",
    "s":"r"
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

def opponent_repeat_rs(my_history, their_history):
    # repeat rock, scissors
    if len(my_history) % 2 == 0:
        return "r"
    return "s"

def opponent_repeat_pr(my_history, their_history):
    # repeat paper, rock
    if len(my_history) % 2 == 0:
        return "p"
    return "r"

def opponent_repeat_sp(my_history, their_history):
    # repeat scissors, paper
    if len(my_history) % 2 == 0:
        return "s"
    return "p"

def opponent_repeat_rps(my_history, their_history):
    # repeat rock, paper, scissors
    if len(my_history) % 3 == 0:
        return "r"
    elif len(my_history) % 3 == 1:
        return "p"
    return "s"

def opponent_repeat_prs(my_history, their_history):
    # repeat paper, rock, scissors
    if len(my_history) % 3 == 0:
        return "p"
    elif len(my_history) % 3 == 1:
        return "r"
    return "s"

def opponent_repeat_srp(my_history, their_history):
    # repeat scissors, rock, paper
    if len(my_history) % 3 == 0:
        return "s"
    elif len(my_history) % 3 == 1:
        return "r"
    return "p"

def opponent_copy_last(my_history, their_history):
    # copy opponents last move
    if len(their_history) > 0:
        return their_history[-1]
    # if no history, play random
    return "rps"[random.randint(0,2)]

move_that_loses = {
    "p" : "r",
    "s" : "p",
    "r" : "s"
}

def opponent_antibeat_last(my_history, their_history):
        # copy opponents last move
    if len(their_history) > 0:
        return move_that_loses[their_history[-1]]
    # if no history, play random
    return "rps"[random.randint(0,2)]


opponents = [opponent_random, opponent_beat_last, opponent_repeat_rs, opponent_repeat_pr, opponent_repeat_sp, opponent_repeat_rps, opponent_repeat_prs, opponent_repeat_srp, opponent_copy_last, opponent_antibeat_last]
