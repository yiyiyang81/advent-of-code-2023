import os
import functools

with open(os.path.join(os.path.dirname(__file__),'input.txt')) as f:
    data = f.read().splitlines()

def part1(data):
    res = 0
    for l in data:
        if l in ["\n",""]:
            continue
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

    print(res)


def part2(data):
    res = 0
    for l in data:
        if l in ["\n",""]:
            continue
        x,plays = l.split(": ")
        dict={"red":0,"blue":0,"green":0}

        plays = plays.split("; ")
        for p in plays:
            draws = p.split(", ")
            for d in draws:
                num, color = d.split(" ")
                if dict[color]<int(num):
                    dict[color] = int(num)
        res+=functools.reduce(lambda x,y:x*y,dict.values())
    print(res)

part1(data)
part2(data)