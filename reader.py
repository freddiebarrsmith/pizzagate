#!/usr/bin/python3

with open("small.in") as f:
    mylist = f.read().splitlines()

print(mylist[0])


rows = mylist[0][0]
columns = mylist[0][2]
minsepingredient = mylist[0][4]
maxslicesize = mylist[0][6]
print(rows)
print(columns)
print(minsepingredient)
