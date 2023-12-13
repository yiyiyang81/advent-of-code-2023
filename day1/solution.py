import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = f.read().splitlines()

res = 0
for l in data:
    num = ""
    for c in l:
        if c.isdigit():
            num += c
    res += int(num[0]+num[-1])
print(res)


with open(os.path.join(os.path.dirname(__file__),"input.txt")) as f:
    data = f.read().splitlines()

res2=0
dict = {"one":1,"two":2,"three":3,
        "four":4,"five":5,"six":6,
        "seven":7,"eight":8,"nine":9}
for s in data:
    num = ""
    k=0
    for i in range(len(s)):
        for word in dict.keys():
            if word in s[k:i+1]:
                num+=str(dict[word])
                k=i-1
        if s[i].isnumeric():
            num+=s[i]

    res2 += int(num[0]+num[-1])
print(res2)
