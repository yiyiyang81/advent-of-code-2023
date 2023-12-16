import os
import functools

with open(os.path.join(os.path.dirname(__file__),"input.txt")) as f:
    data = f.read().splitlines()

def part1(data):
    res = 0
    for l in data:
        if not l:
            continue
        x, cards = l.split(": ")
        elf, you = cards.split("|")
        set1  = set(elf.split())
        set2  = set(you.split())
        tmp = set1 & set2
        if tmp:
            res+=2**(len(tmp)-1)
    print(res)

def part2(data):
    dict = {}
    for i in range(1, len(data)):
        dict[i] = 1
    for l in data:
        if not l:
            continue
        x, cards = l.split(": ")
        x = int(x.replace("Card ",""))
        elf, you = cards.split("|")
        set1  = set(elf.split())
        set2  = set(you.split())
        win = len(set1 & set2)
        print("card",x, "wins:", win)

        if win:
            copies = dict[x]
            print("already have card:",x, copies)
            for i in range(x+1,x+win+1):
                dict[i] +=copies
    print(sum(dict.values()))

        
    

part1(data)

part2(data)