import csv
import os
import math

pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

csvpath = os.path.join(pwd,"Resources", "budget_data.csv")

total = 0
total_profit = 0
p_max = 0
value_max = -math.inf
value_min = math.inf
p_min = 0
indice = 0
list_total = []
list_date = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for i in csvreader:
        # Total Months
        if indice == 0:
            indice += 1
        else:
            indice += 1
            # Greatest Increase
            if int(i[1]) > value_max:
                p_max, value_max = i[0],int(i[1])
            # Greatest Decrease
            if int(i[1]) < value_min:
                p_min, value_min = i[0], int(i[1])
            #Total
        if indice > 0:
            total_profit += int(i[1])

    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {indice}')
    print(f'Total: {total_profit}')
    print(f'Average: {total_profit/indice}')
    print(f'Greatest Increase in Profits: {p_max} {value_max}')
    print(f'Greatest Decrease in Profits: {p_min} {value_min}')


