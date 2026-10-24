inventory =  {"laptop": {"price": 2500, "stock": 5}, "keyboard": {"price": 500, "stock": 6}, "TV": {"price": 3500, "stock": 7}}
product = input("enter product name: ")
if product in inventory:
    inventory[product]["stock"] = int(input("Enter new quantity: "))
else:
    price = int(input("Enter product price: "))
    stock = int(input("Enter product quantity: "))
    inventory[product] = {"price": price, "stock": stock}

active_users = {"nika", "ana", "gio", "mari"}
vip_users = {"ana", "mari", "saba"}
each_unic_member = active_users | vip_users
print(f"all unique members of the base: {each_unic_member}")
print(f"vip users of the base: {vip_users}")
print(f"non vip users of the base:{active_users}")

for product in inventory:
    if inventory[product]["stock"] > 0:
        print(product)

most_expensive = ""
max_price = 0

for product in inventory:
    if inventory[product]["price"] > max_price:
        max_price = inventory[product]["price"]
        most_expensive = product

print("Most expensive product:", most_expensive)
print("Price:", max_price)