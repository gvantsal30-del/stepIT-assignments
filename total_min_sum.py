total = 0
shesakrebi = 0
min_num = None
max_num = None

while True:
    txt = input("შეიყვანეთ რიცხვი ან 'stop': ")
    
    if txt == "stop":
        break

    try:
        num = float(txt)

        total += num
        shesakrebi += 1

        if min_num is None or num < min_num:
            min_num = num

        if max_num is None or num > max_num:
            max_num = num

    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")

print("ჯამი:", total)
print("მინიმალური:", min_num)
print("მაქსიმალური:", max_num)