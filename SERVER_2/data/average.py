import json

data= list(json.loads(open("stats.json","r").read()).values())

total = 0
for d in data:
    total += d
av = total/len(data)
print(av)