import csv

file_path = "mydata2.csv"

data = [
    {"Name": "Alice", "Age": 30, "Location": "Seoul"},
    {"Name": "Alice.Jr", "Age": 5, "Location": "Seoul"},
    {"Name": "Bob.Jr", "Age": 36, "Location": "Busan"},
    {"Name": "Bob.Jr", "Age": 7, "Location": "Busan"},
]

with open(file_path, "w", encoding="UTF-8", newline="") as file:
    # headers = ["Name", "Age", "Location"]
    headers = data[0].keys()
    csv_w = csv.DictWriter(file, fieldnames=headers)
    csv_w.writeheader()
    csv_w.writerows(data)
    # csv_w.writerow(["이름", "나이"])
    # csv_w.writerow(["Alice", 30])
    # csv_w.writerow(["Alice.Jr", 5])
    # csv_w.writerow(["Bob", 35])
    # csv_w.writerow(["Bob.Jr", 7])
