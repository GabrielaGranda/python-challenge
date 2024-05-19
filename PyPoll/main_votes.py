import csv
import os
import math

pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

csv_path = os.path.join(pwd, "Resources", "election_data.csv")
print(csv_path)

indice = 0
indice1 = 0
name = {}
votes = []
cont = {}
list_per = []
total_list = {}

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for i in csvreader:
        if indice == 0:
            indice += 1
        else:
            indice += 1
            if i[2] in cont:
                cont[i[2]] += 1
            else:
                cont[i[2]] = 1
    votes = max(cont.keys(), key=lambda k: cont[k])
    name = {k: (v/indice)*100 for (k,v) in cont.items()}

    from itertools import chain
    from collections import defaultdict

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {indice}')
    print("-------------------------")

    total_list = defaultdict(list)
    for k, v in chain(name.items(), cont.items()):
        total_list[k].append(v)
    for k, v in total_list.items():
        print(k,v)

    print("-------------------------")
    print(f'Winner: {votes}')
    print("-------------------------")