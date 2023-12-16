import os
import re

with open(os.path.join(os.path.dirname(__file__),'input.txt')) as f:
    data = f.read().splitlines()

res = 0
for l in data:
    if l in ["\n",""]:
        continue
    print(l)
    x,plays = l.split(": ")
    dict={"red":12,"blue":14,"green":13}

    game_id = int(x.replace("Game ",""))
    plays = plays.split("; ")
    flag = 0
    for p in plays:
        draws = p.split(", ")
        for d in draws:
            num, color = d.split(" ")
            if dict[color]<int(num):
                flag=1
    if not flag:
        res+=game_id
    else:
        print("game_id",game_id)

print(res)
