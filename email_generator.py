firs_name = input("please enter your first name:\n").strip().title()
last_name = input("please enter your last name:\n").strip().title()
platform = input("please enter your preferable platfrom(gmail.com, itstep.ge, yahoo.com):\n")
first_two_letters = last_name[:2]
email = f"{firs_name[:2].lower()}{last_name.lower()}@{platform}"
print(email)
print()
print()
print("your email was created successfully")