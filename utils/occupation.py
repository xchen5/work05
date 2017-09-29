import csv
import random

def pick():
    #read file
    file = csv.reader(open('data/occupations.csv','rU'))
    occupations = []
    next(file)
    for row in file:
        if row[0] == "Total":
            break
        percentage = int(float(row[1]) * 10)
        for i in range(0,percentage):
            occupations.append(row[0])
    #pick occupation
    num = random.randint(0,len(occupations) - 1)
    return occupations[num]

print(pick())
