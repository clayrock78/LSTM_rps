from team import move as net_move
from opponent import move as opp_move

from opponents import opponents

beaten_by = {
    "r":"p",
    "p":"s",
    "s":"r"
}
tw = 0
tl = 0
tt = 0 

for opponent in opponents:
    t1 = ""
    tp = ""
    t2 = ""

    wins = 0
    losses = 0
    ties = 0

    for i in range(100):
        t1m, pred = net_move(t1, t2)
        t2m = opponent(t2, t1)

        if t1m == t2m:
            ties += 1
            tt += 1
        elif beaten_by[t1m] == t2m:
            losses += 1
            tl += 1
        else:
            wins += 1
            tw += 1

        t1 += t1m
        tp += pred
        t2 += t2m


    print(f"OPPONENT NAME : {opponent.__name__}")
    print("NETWORK :",t1)
    print("PREDICT :",tp)
    print("OPPONENT:",t2)

    # display results
    print("wins:", wins)
    print("losses:", losses)
    print("ties:", ties)

    # display win rate
    print("win rate:", wins/(wins+losses+ties))

print("OVER ALL RESULTS")

# display results
print("wins:", tw)
print("losses:", tl)
print("ties:", tt)

# display win rate
print("win rate:", tw/(tw+tl+tt))