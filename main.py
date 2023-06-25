import products
import store

def start(store_obj):
    while True:
        print("Welcome to the Store!")
        print("Please select an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice < 1 or choice > 4:
                raise ValueError()
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
            print()
            continue

        if choice == 1:
            all_products = store_obj.get_all_products()
            if not all_products:
                print("No products available in the store.")
            else:
                for product in all_products:
                    print(product.show())
            print()
        elif choice == 2:
            total_quantity = store_obj.get_total_quantity()
            print(f"Total quantity in the store: {total_quantity}")
            print()
        elif choice == 3:
            shopping_list = []
            while True:
                product_name = input("Enter the name of the product (or 'exit' to finish): ")
                if product_name == "exit":
                    break
                quantity = int(input("Enter the quantity: "))
                product = None
                for p in store_obj.get_all_products():
                    if p.name == product_name:
                        product = p
                        break
                if product is not None:
                    if quantity <= 0:
                        print("Invalid quantity. Please enter a positive number.")
                    elif quantity > product.get_quantity():
                        print("Please enter a smaller quantity.")
                    elif product_name == "Shipping" and quantity > 1:
                        print("Maximum order for that product is 1. Please enter the correct quantity.")
                    else:
                        shopping_list.append((product, quantity))
                else:
                    print("Invalid product name. Try again.")
            if shopping_list:
                total_price = store_obj.order(shopping_list)
                print(f"Order placed! Total price: {total_price}")
            else:
                print("No products selected for order.")
            print()
        elif choice == 4:
            print("Goodbye!")
            break

def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, max_quantity=1)
    ]

    best_buy = store.Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()
