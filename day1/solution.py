import os

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