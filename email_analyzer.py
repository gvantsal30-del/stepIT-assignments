import re
text = "ჩვენი გუნდის წევრები არიან: saba.ananidze@itstep.com, მეგობარი დიმა dima123@gmail.com და კიდევ ერთი ტესტური მისამართი test_user@yahoo.com"
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
last = "+".join(emails)
print(last)

