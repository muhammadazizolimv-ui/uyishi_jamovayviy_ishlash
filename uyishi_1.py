import csv

def show_tasks():
    with open("tasks.csv", "r", encoding="utf-8") as fayl:
        oqish = csv.DictReader(fayl)

        for vazifa in oqish:
            print(vazifa["id"], vazifa["name"], vazifa["status"])

show_tasks()
