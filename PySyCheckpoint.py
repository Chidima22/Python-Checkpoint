my_dict = {
    "small": 15,
    "medium": 20,
    "large": 25,
    "pepperoni_small": 2,
    "pepperoni_medium": 3,
    "pepperoni_large": 3,
    "extra_cheese": 1
}

print(f"Here is our price list:\n {my_dict}")

pizza_size = input("What size of pizza do you want? (small, medium, large): ").lower()

if pizza_size not in ["small", "medium", "large"]:
    print("Please we only offer small, medium, or large pizzas.")
else:
    add_pepperoni = input("Do you want pepperoni in your pizza? (Yes or No): ").lower()
    
    if add_pepperoni not in ["yes", "no"]:
        print("Please we only accept Yes or No.")
    else:
        extra_cheese = input("Do you want cheese in your pizza? (Yes or No): ").lower()
        
        if extra_cheese not in ["yes", "no"]:
            print("Please we only accept Yes or No.")
        else:
            #Calculate Total Bill
            total_bill = my_dict[pizza_size]
            
            if add_pepperoni == "yes":
                total_bill += my_dict[f"pepperoni_{pizza_size}"]

            if extra_cheese == "yes":
                total_bill += my_dict["extra_cheese"]

            #Final price
            print(f"Your total bill is: ${total_bill}.")
