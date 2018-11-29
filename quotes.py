import csv
with open('top.csv', newline="") as top:
    file = csv.reader(top, delimiter=',', quotechar='|')
    print(len(list(file)))
