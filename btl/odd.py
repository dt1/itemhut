fields = [("one"), ("two"), ("three")]
fdict = {}
x = 1
for f in fields:
    fdict[f] = {}
    fdict[f]["cnt"] = x
    x += 1

print(fdict)
