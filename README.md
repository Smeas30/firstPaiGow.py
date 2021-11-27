# firstPaiGow.py
Paigow project game where you can play against an AI

Game mechanics:
AI play
AI will choose the best possible 5 cards for the bottom > 5 middle > top 3

top 3
check for highest single
range(1-13)

single
lowest 3 value = 2, 3, 4 = 7
highest 3 value = Q, K, A = 33

pair
lowest pair = 2,2,3 = 3
highest pair = A,A,K = 35

Triple
lowest triple = 2,2,2 = 0
highest triple = A,A,A = 36

5 middle
single
lowest = 2,3,4,5,7 = 21
highest = A,K,Q,J,9 = 49

pair

triple

straight

flush

full house

4 of a kind

straigh flush

royal flush

5 bottom
has to be larger then middle

AI game play

let AI play the best hands on bot then second best then last 3 cards remaining on top
