
import re

text = input("შეიყვანეთ ჯავშნის ინფორმაცია: ")

numbers = re.findall(r"\d+(?:\.\d+)?", text)

try:
    tickets = int(numbers[0])
    paid_money = float(numbers[2])

    total_price = tickets * 15

    if tickets <= 0:
        raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1")

    if paid_money < total_price:
        raise ValueError("თანხა არ არის საკმარისი")

except IndexError:
    print("შეცდომა: ტექსტში საჭირო რიცხვები ვერ მოიძებნა.")

except ValueError as error:
    print(f"შეცდომა: {error}")

else:
    change = paid_money - total_price

    print("ჯავშანი წარმატებით შესრულდა!")
    print(f"ბილეთების რაოდენობა: {tickets}")
    print(f"ჯამური ღირებულება: {total_price:.2f} ლარი")
    print(f"გადახდილი თანხა: {paid_money:.2f} ლარი")
    print(f"ხურდა: {change:.2f} ლარი")

finally:
    print("[სისტემა]: ტრანზაქციის მცდელობა დასრულდა.")
