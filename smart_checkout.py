cart_total = float(input("შეიყვანეთ კალათის ღირებულება ლარებში:\n"))

user_status = input("მომხმარებლის სტატუსი(regular, vip, ან admin):\n").strip().title()

has_promo_code = input("აქვს პრომოკოდი? (True/False): ").strip().lower() == "true"

loyalty_points = int(input("მომხმარებლის დაგროვილი ქულები\n"))

delivery_city = input("ქალაქი, სადაც იგზავნება შეკვეთა(მაგ: თბილისი, ბათუმი, რეგიონი):\n").strip().title()

is_account_active = input("არის ანგარიში აქტიური? (True/False): ").strip().lower() == "true"



if not is_account_active:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება.")

elif cart_total <= 0:
    print("შეცდომა: კალათის ღირებულება უნდა იყოს 0-ზე მეტი.")
else: 
    discount = 0
    if user_status == "vip":
        if loyalty_points >= 500:
            discount = 25
        else: discount = 20       
    elif user_status == "regular":
        if has_promo_code or cart_total >= 150:
            discount = 10     
        else: discount = 0  
    elif user_status == "admin":
            discount = 50    
    if discount >= 0:
        discount_amount = cart_total * discount / 100
        discounted_total = cart_total - discount_amount
        
        main_cities = ["თბილისი", "ქუთაისი", "ბათუმი"]

    if delivery_city in main_cities:
        if discounted_total >= 100:
            delivery_fee = 0
        else: 
            delivery_fee = 5
    else:
        delivery_fee = 15            

        final_total = discounted_total + delivery_fee
        print("\n შეკვეთის ინვოისი")
        print(f"კალათის საწყისი ფასი: {cart_total:.2f} ლარი")
        print(f"ფასდაკლება: {discount}%")
        print(f"ფასდაკლების თანხა: {discount_amount:.2f} ლარი")
        print(f"ფასდაკლებული ფასი: {discounted_total:.2f} ლარი")
        print(f"მიტანის საფასური: {delivery_fee:.2f} ლარი")
        print(f"საბოლოო გადასახდელი: {final_total:.2f} ლარი")

        