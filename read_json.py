import json

with open('roadcrash_factors.json', 'r') as rcf_file:
    rcf_data = json.load(rcf_file)

line_count = 0

for record in rcf_data['records']:
    year = record[1]
    severity = record[3]
    dui = record[4]
    speed = record[5]
    fatigue = record[6]
    defect = record[7]
    print(f"In {year} an accident of severity {severity} was caused by dui: {dui}, speed: {speed}, fatigue: {fatigue}, vehicle defects: {defect}")
    line_count += 1

print(f"Processed {line_count-1} records")