import os
import re

with open(os.path.join(os.path.dirname(__file__),"input.txt")) as f:
    data = f.read().splitlines()

res = []

def part1(data):
    seeds = data[0][7:].split()
    for seed in seeds:
        new_seed = int(seed)
        converted = 0
        for l in data[1:]:
            value = re.findall(r"(\d+) (\d+) (\d+)", l)
            if value: 
                    if new_seed >= int(value[0][1]) and new_seed < int(value[0][1]) + int(value[0][2]):
                        if not converted:
                            new_seed = int(value[0][0]) + (new_seed - int(value[0][1]))
                            converted = 1
                    else:
                        new_seed = new_seed
            else:
                converted = 0
        res.append(new_seed)
    print(min(res))


def part2(data):
    seeds = data[0][7:].split()
    # seeds = 
    # for seed in seeds:
    #     new_seed = int(seed)
    #     converted = 0
    #     for l in data[1:]:
    #         value = re.findall(r"(\d+) (\d+) (\d+)", l)
    #         if value: 
    #                 if new_seed >= int(value[0][1]) and new_seed < int(value[0][1]) + int(value[0][2]):
    #                     if not converted:
    #                         new_seed = int(value[0][0]) + (new_seed - int(value[0][1]))
    #                         converted = 1
    #                 else:
    #                     new_seed = new_seed
    #         else:
    #             converted = 0
    #     res.append(new_seed)
    # print(min(res))
    # print(res)


# part1(data)
part2(data)