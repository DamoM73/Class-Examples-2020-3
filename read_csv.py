import csv

with open('roadcrash_factors.csv', 'r') as rcf_file:
    csv_reader = csv.reader(rcf_file, delimiter=",")

    line_count = 0

    for row in rcf_file:
        row = list(row.split(','))
        
        if line_count == 0:
            line_count += 1
        else:
            year = row[1]
            severity = row[3]
            dui = row[4]
            speed = row[5]
            fatigue = row[6]
            defect = row[7]
            print(f"In {year} an accident of severity {severity} was caused by dui: {dui}, speed: {speed}, fatigue: {fatigue}, vehicle defects: {defect}")
            line_count += 1

print(f"Processed {line_count-1} records")