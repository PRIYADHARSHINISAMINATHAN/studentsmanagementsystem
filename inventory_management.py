products = []

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Low Stock Products")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))

        product = {
            "id": product_id,
            "name": product_name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)
        print("Product added successfully!")

    elif choice == "2":
        if len(products) == 0:
            print("No products available.")
        else:
            print("\n----- Product List -----")
            for product in products:
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
                print("------------------------")

    elif choice == "3":
        search_id = input("Enter Product ID to search: ")
        found = False

        for product in products:
            if product["id"] == search_id:
                print("\nProduct Found")
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
                found = True
                break

        if not found:
            print("Product not found.")

    elif choice == "4":
        update_id = input("Enter Product ID to update quantity: ")
        found = False

        for product in products:
            if product["id"] == update_id:
                new_quantity = int(input("Enter New Quantity: "))
                product["quantity"] = new_quantity
                print("Quantity updated successfully!")
                found = True
                break

        if not found:
            print("Product not found.")

    elif choice == "5":
        delete_id = input("Enter Product ID to delete: ")
        found = False

        for product in products:
            if product["id"] == delete_id:
                products.remove(product)
                print("Product deleted successfully!")
                found = True
                break

        if not found:
            print("Product not found.")

    elif choice == "6":
        print("\n----- Low Stock Products -----")
        found = False

        for product in products:
            if product["quantity"] < 5:
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Quantity:", product["quantity"])
                print("------------------------")
                found = True

        if not found:
            print("No low stock products.")

    elif choice == "7":
        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
