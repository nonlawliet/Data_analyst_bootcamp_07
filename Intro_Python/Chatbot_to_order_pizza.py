def order_pizza():
    user_name = input("The Non's pizza. Can you give me your name? ")
    print(f"Hi! {user_name}. This is chatbot for ordering pizza which you can create your own pizza")
    print("Please enter the number which you want in each step")
    print("Choose size you want? ")
    sizes = ("Small (7 inch)", "Medium (9 inch)", "Large (12 inch)")
    size_index = 1
    for size in sizes:
        print(f"[{size_index}]: {size}")
        size_index += 1
    user_size = []
    user_size = int( input("Your pizza size: ") )
    print("Choose crust you want")
    crusts = ("Classic", "Thin", "Cheese")
    crust_index = 1
    for crust in crusts:
        print(f"[{crust_index}]: {crust}")
        crust_index += 1
    user_crust = []
    user_crust = int( input("Your pizza crust: ") )
    print(f"Your pizza order has size {sizes[user_size - 1]} and crust {crusts[user_crust - 1]}.")
    print("Next step is the topping you can adding anything you want in the list below:")
    toppings = ("Crab Meat", "BBQ Chinken", "Shrimp", "Ham", "Squid", "Red Chill", "Corn", "Pineapple")
    topping_index = 1
    for topping in toppings:
        print(f"[{topping_index}]: {topping}")
        topping_index += 1
    user_toppings = []
    print("Enter '9' when you finish your topping")
    while True:
        user_topping = int( input("Your pizza topping: ") )
        if user_topping == 9:
            print(f"Your order is the pizza {sizes[user_size - 1]} size, {crusts[user_crust - 1]} crust.")
            print(f"And the toppings: {user_toppings}")
            return
        user_toppings.append(toppings[(user_topping) - 1])
order_pizza()
