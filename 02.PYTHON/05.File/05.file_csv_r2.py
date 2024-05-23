import csv

file_path = "mydata2.csv"

with open(file_path, "r", encoding="UTF-8") as file:
    csv_r = csv.DictReader(file)
    for data in csv_r:
        # print(data)
        print(data["Name"], data["Age"], data["Location"])
