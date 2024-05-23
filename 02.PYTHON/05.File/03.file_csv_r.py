import csv

file_path = "mydata.csv"

with open(file_path, "r", encoding="UTF-8") as file:
    csv_r = csv.reader(file)
    for data in csv_r:
        print(data)
