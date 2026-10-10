first_name = input("what is your first name?\n")
last_name = input("What is your last name?\n")
birth_year = int(input("what is your birth year?\n"))
favorite_language = input("what is your favourite programming language?\n")
#მონაცემების დამუშავება
first_name = first_name.upper()
last_name = last_name.upper()
favorite_language = favorite_language.upper()
now = 2026
age = now - birth_year
is_adult = age >= 18
#ინფორმაციის დაბეჭდვა
print(first_name, last_name, age, favorite_language, is_adult, sep=" | ")

score = int(input("enter student's score (max 20): "))
grade = score // 2
print("students grade is", grade)
