import csv
import json
import os
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from contextlib import contextmanager

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "employees.csv"
OUT = BASE / "output"

def task_1_1():
    OUT.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        print("ფაილი data/employees.csv ვერ მოიძებნა!")
        return False

    print("ბილიკი:", DATA_FILE.resolve())
    return True

def backup_file(src, dst):
    count = 0

    with open(src, "r", encoding="utf-8", newline="") as fin, \
         open(dst, "w", encoding="utf-8", newline="") as fout:

        for line in fin:
            fout.write(line)
            count += 1

    return count

def task_1_2():
    count = backup_file(DATA_FILE, OUT / "employees_backup.csv")
    print("დაკოპირებული ხაზები:", count)

def log(message):
    with open(OUT / "log.txt", "a", encoding="utf-8") as f:
        f.write(datetime.now().isoformat() + " " + message + "\n")

def task_1_4():
    try:
        with open(OUT / "lock.txt", "x", encoding="utf-8") as f:
            f.write(datetime.now().isoformat())

        print("lock.txt შეიქმნა")

    except FileExistsError:
        print("ანგარიში უკვე შექმნილია")

def task_2_1():
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")

        header = next(reader)
        rows = list(reader)

    print("სათაური:", header)
    print("პირველი 3 ჩანაწერი:", rows[:3])
    print("ჩანაწერების რაოდენობა:", len(rows))

def task_2_2():
    employees = []

    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            row["salary"] = int(row["salary"])

            row["is_active"] = row["is_active"].strip().lower() == "true"

            employees.append(row)

    counts = {}
    totals = {}

    for e in employees:
        department = e["department"]

        counts[department] = counts.get(department, 0) + 1
        totals[department] = totals.get(department, 0) + e["salary"]

    stats = []

    for department in counts:
        avg = round(totals[department] / counts[department], 2)

        stats.append({
            "department": department,
            "employee_count": counts[department],
            "avg_salary": avg
        })

    stats.sort(key=lambda s: s["avg_salary"], reverse=True)

    print("\nდეპარტამენტების სტატისტიკა:")

    for s in stats:
        print(s)

    active = []

    for e in employees:
        if e["is_active"]:
            active.append(e)

    active.sort(key=lambda e: e["salary"], reverse=True)

    print("\nტოპ 3 აქტიური თანამშრომელი:")

    for e in active[:3]:
        print(e["first_name"], e["last_name"], e["salary"])

    print("აქტიური თანამშრომლები:", len(active))
    print("არააქტიური თანამშრომლები:", len(employees) - len(active))

    return employees, stats

def task_2_3(stats):
    with open(OUT / "department_stats.csv", "w", encoding="utf-8", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=["department", "employee_count", "avg_salary"])

        writer.writeheader()
        writer.writerows(stats)

def task_2_4(employees):
    rows = []

    for e in employees:
        if e["is_active"] and e["salary"] >= 5000:

            full_name = e["first_name"] + " " + e["last_name"]

            rows.append([e["id"], full_name, e["department"], e["salary"]])

    with open(OUT / "high_earners.csv", "w", encoding="utf-8", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["id", "full_name", "department", "salary"])
        writer.writerows(rows)

    print("მაღალი ხელფასის მქონე თანამშრომლები:", len(rows))

def safe_read(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        log("ფაილი ვერ მოიძებნა: " + str(path))
        return ""

    except UnicodeDecodeError:
        log("კოდირების შეცდომა: " + str(path))

        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()

def task_3_1():
    with open(OUT / "broken.txt", "wb") as f:
        f.write(bytes([99, 97, 102, 233, 32, 255]))

    print("არარსებული ფაილი:", safe_read(OUT / "missing.txt"))
    print("დაზიანებული ფაილი:", safe_read(OUT / "broken.txt"))

def task_3_2(employees):
    cities = Counter()

    for e in employees:
        cities[e["city"]] += 1

    top3 = cities.most_common(3)

    print("\nტოპ 3 ქალაქი:")

    for city, count in top3:
        print(city, count)

    with open(OUT / "city_report.txt", "w", encoding="utf-8") as f:
        print("ტოპ 3 ქალაქი:", file=f)

        for city, count in top3:
            print(city, count, file=f)

def save_json_safe(data, path):
    tmp = str(path) + ".tmp"

    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.replace(tmp, path)

def task_3_3(stats):
    save_json_safe(stats, OUT / "summary.json")

@contextmanager
def Timer(name):
    print(f"START {name}")

    start = time.perf_counter()

    try:
        yield

    except Exception as error:
        print(f"FAILED {name}: {type(error).__name__}")
        raise

    finally:
        end = time.perf_counter()

        print(f"FINISH {name}: {end - start:.4f} წამი")

def main():

    if not task_1_1():
        sys.exit(1)

    log("პროგრამა დაიწყო")

    task_1_2()
    task_1_4()

    log("ნაწილი 1 დასრულდა")

    with Timer("CSV ანალიზი"):
        task_2_1()

        employees, stats = task_2_2()

        task_2_3(stats)
        task_2_4(employees)

    log("ნაწილი 2 დასრულდა")

    task_3_1()
    task_3_2(employees)
    task_3_3(stats)

    log("ნაწილი 3 დასრულდა")

    try:
        with Timer("test"):
            1 / 0

    except ZeroDivisionError:
        print("ZeroDivisionError დაჭერილია")

    log("ნაწილი 4 დასრულდა")

    log("პროგრამა დასრულდა")


if __name__ == "__main__":
    main()
