scores = []
while True:
    score = input("please enter your scores or 'stop' to end operation: ")
    if score == "stop":
        break

    try:
        numbers = int(score)
        if 0 <= numbers <= 10:
            scores.append(numbers)
        else:
            print("score should be from 0 to 10")
    except ValueError:
        print("please enter correct number or'stop': ")
print(scores)