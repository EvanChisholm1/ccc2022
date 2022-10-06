players = int(input())

global starPlayers
starPlayers = 0

for i in range(0, players):
    starsGained = int(input()) * 5
    starsLost = int(input()) * 3
    rating = starsGained - starsLost
    if rating > 40:
        starPlayers += 1

if players == starPlayers:
    print("{}+".format(starPlayers))
else:
    print(starPlayers)