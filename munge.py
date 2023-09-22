# Place code below to do the munging part of this assignment.

with open('/Users/zhangjianing/Desktop/Databases/2-data-munging-Catherineya/data/raw_data_file.txt', 'r') as f_txt, open('/Users/zhangjianing/Desktop/Databases/2-data-munging-Catherineya/data/clean_data.csv', 'w') as f_csv:
    for line in f_txt:
        if line.startswith("Year"):
            values = line.strip().split()
            values = values[:-1]
            csv_row = ",".join(values)
            f_csv.write(csv_row + "\n")
            break
    for line in f_txt:
        if line.startswith(("Year", " ")) or len(line.strip()) == 0:
            continue
        if line.startswith("Divide"):
            break
        values = line.strip().split()
        date = values[0]
        new_values = values[1:-1]
        for i in range(len(new_values)):
            if('*' not in new_values[i]):
                new_values[i] = format(float(new_values[i]) / 100 * 1.8, '.1f')
        new_values.insert(0, date)
        csv_row = ",".join(new_values)
        f_csv.write(csv_row + "\n")


