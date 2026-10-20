
while True:
    try:
        height = int(input("Enter height (1-8): "))

        if 1 <= height <= 8:
            break
        else:
            print("Height must be between 1 and 8.")

    except ValueError:
        print("Please enter a whole number.")

for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")

    for k in range(i):
        print("#", end="")

    print()
