import csv

file_path = "mydata.csv"

data = [
    ["Name", "Age", "Location"],
    ["Alice", 30, "seoul"],
    ["Alice.Jr", 30, "seoul"],
    ["Bob", 35, "seoul"],
    ["Bob.Jr", 35, "seoul"],
]

data2 = []
with open(file_path, "w", encoding="UTF-8", newline="") as file:
    csv_w = csv.writer(file)
    # csv_w.writerow(["이름", "나이"])
    # csv_w.writerow(["Alice", 30])
    # csv_w.writerow(["Alice.Jr", 5])
    # csv_w.writerow(["Bob", 35])
    # csv_w.writerow(["Bob.Jr", 7])
    csv_w.writerows(data)
