# Purpose
The goal of this project is to make a winning strategy for PLTW CSE Rock Paper Scissors. 

The network uses LSTM to do pattern detection and attempts to guess the opponent's next move.

## Inputs 
Last 10 moves (opponent's and network's) (3 booleans, one for rock, one for paper, one for scissors)
Represented with a numpy array of shape (10,6)  ((20,3) in the old versions, which doesn't work so well)

## Training data
This network was trained on data from actual rounds of PLTW rps (from students) and on generated data `makedata.py` (from basics strats). 

In the future, I might like to train the network with data from games that it has played, but I haven't done this yet.

## Outputs
Three outputs, one represents rock, one paper, and one scissors. This represents the networks prediction for the opponent's next move.

## Results
It works pretty well! `tester.py` uses the local implementation of the network in `team.py` and tests against other (basic) algorithms in `opponents.py`. 

```
OVER ALL RESULTS
wins: 824
losses: 104
ties: 72
win rate: 0.824
```

More specific details
```
OPPONENT NAME : opponent_random
NETWORK : rspprsrsrssssprpsprpsrrrspprsssrprsrpsspprsrrrrsrrssrrrrrppsprsrrppsprsrprprspsrprpssprssrpssssssrrr
PREDICT : sprrspspspppprsrprsrpsssprrspppsrspsrpprrspsssspssppsssssrrprspssrrprspsrsrsprpsrsrpprsppsrppppppsss
OPPONENT: rpssrpsrrpsspssspsrrppssprrpspsrpprssrsssrssppsspsrprrpprrsppssrrsprrspsssrppspprrsrsrrrrrsppsprrrss
wins: 38
losses: 34
ties: 28
win rate: 0.38

OPPONENT NAME : opponent_beat_last
NETWORK : rsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprspr
PREDICT : sprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprs
OPPONENT: rprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprs
wins: 99
losses: 0
ties: 1
win rate: 0.99

OPPONENT NAME : opponent_repeat_rs
NETWORK : rsppprsrprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprpr
PREDICT : sprrrspsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrs
OPPONENT: rsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrs
wins: 96
losses: 2
ties: 2
win rate: 0.96

OPPONENT NAME : opponent_repeat_pr
NETWORK : rsrrsrprssspppssssssspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspsp
PREDICT : spsspsrsppprrrppppppprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprpr
OPPONENT: prprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprprpr
wins: 88
losses: 7
ties: 5
win rate: 0.88

OPPONENT NAME : opponent_repeat_sp
NETWORK : rrspprrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrs
PREDICT : ssprrsspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspsp
OPPONENT: spspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspspsp
wins: 95
losses: 3
ties: 2
win rate: 0.95

OPPONENT NAME : opponent_repeat_rps
NETWORK : rsppppssrssrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrp
PREDICT : sprrrrppsppsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsr
OPPONENT: rpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsr
wins: 94
losses: 4
ties: 2
win rate: 0.94

OPPONENT NAME : opponent_repeat_prs
NETWORK : rsrpsrspprsppprrprsprrsppprrprsprrsppprrprsprrsppprrprsprrsppprrprsprrsppprrprsprrsppprrprsprrsppprr
PREDICT : spsrpsprrsprrrssrsprssprrrssrsprssprrrssrsprssprrrssrsprssprrrssrsprssprrrssrsprssprrrssrsprssprrrss
OPPONENT: prsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsprsp
wins: 55
losses: 36
ties: 9
win rate: 0.55

OPPONENT NAME : opponent_repeat_srp
NETWORK : rrprssrpsrpprpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsr
PREDICT : ssrsppsrpsrrsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrps
OPPONENT: srpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrps
wins: 96
losses: 1
ties: 3
win rate: 0.96

OPPONENT NAME : opponent_copy_last
NETWORK : rrprprpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrp
PREDICT : ssrsrsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsr
OPPONENT: srrprprpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsrpsr
wins: 97
losses: 2
ties: 1
win rate: 0.97

OPPONENT NAME : opponent_antibeat_last
NETWORK : rrrrpsrprprrrsssppsrrpprrsspprrrrrssspssrprspprrrrsssppprrrrrssrrrrrrprrrrrrrrrrppppppssssssssssssss
PREDICT : ssssrpsrsrsssppprrpssrrsspprrsssssppprppsrsprrssssppprrrsssssppssssssrssssssssssrrrrrrpppppppppppppp
OPPONENT: sssssrpsrsrsssppprrpssrrsspprrsssssppprppsrsprrssssppprrrsssssppssssssrssssssssssrrrrrrppppppppppppp
wins: 66
losses: 15
ties: 19
win rate: 0.66
```
