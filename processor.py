# processes rps games to make random samples of games
import random
import numpy as np

# format for game (p1_history ("mine") ,p2_history ("theirs"))
all_games = []

with open("gen_huger.txt", "r") as f:
    text = f.read()
    games = text.split("\n\n")
    all_games = [tuple(game.split("\n")) for game in games]

def load_data(hist_len):
    # format for history (my_hist, their_hist, their_next_move)
    histories = list()
    nexts = list()

    rps_val = {
        "r" : [1,0,0],
        "p" : [0,1,0],
        "s" : [0,0,1],
        " " : [0,0,0]
    }

    for game in all_games:
        me = game[0]
        them = game[1]
        for _ in range(15):
            r_start = random.randint(2,988)
            r_stop = min(r_start + min(random.randint(2,hist_len+hist_len//2),hist_len), 999)
            hist = np.array([list(zip([rps_val[x] for x in me[r_start:r_stop].ljust(hist_len, " ")],[rps_val[x] for x in them[r_start:r_stop].ljust(hist_len, " ")]))])
            #print(hist.shape)
            histories.append(hist)
            nexts.append(rps_val[them[r_stop]])

    histories = np.array(histories).reshape((len(histories),hist_len,6))
    nexts = np.array(nexts)
    return histories, nexts
