# Place code below to do the analysis part of the assignment.

import csv

with open('/Users/zhangjianing/Desktop/Databases/2-data-munging-Catherineya/data/clean_data.csv', 'r') as f, open('/Users/zhangjianing/Desktop/Databases/2-data-munging-Catherineya/data/analyze.txt', 'w') as f2:
    reader = csv.reader(f, delimiter=',')
    rows = list(reader)
    for i in range(1, len(rows), 10):
        date1 = rows[i][0]
        avg = 0
        if rows[i][0] == '2020':
            date2 = rows[i+2][0]
            numYears = 3
            for k in range(i, i+3):
                avg += float(rows[k][13])
            avg = format(avg / numYears, '.1f')
        else:
            date2 = rows[i+9][0]
            numYears = 10
            for k in range(i, i+10):
                avg += float(rows[k][13])
            avg = format(avg / numYears, '.1f')
        f2.write(date1 + '-' + date2 + ': ' + avg + '\n')