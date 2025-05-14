# Product and order lists (Food items in products and ID, quantity, and status in orders)
products = [{"id": 1, "name": "Croissant", "price": 1.50},
            {"id": 2, "name": "Pretzel", "price": 0.75},
            {"id": 3, "name": "Salad", "price": 2.00},
            {"id": 4, "name": "Baguette", "price": 1.80}]
orders = [{"id": 1, "product_id": 1, "quantity": 3, "status": "Pending"},
          {"id": 2, "product_id": 2, "quantity": 5, "status": "Shipped"}]

# Main Menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("0 - Exit")
        print("1 - Products Menu")
        print("2 - Orders Menu")
        
        choice = input("Select an option: ")

        if choice == "0":
            print("Exiting the app.")
            break
        elif choice == "1":
            products_menu()
        elif choice == "2":
            orders_menu()
        else:
            print("Invalid choice. Please try again.")

# Products Menu
def products_menu():
    while True:
        print("\nProducts Menu:")
        print("0 - Return to Main Menu")
        print("1 - View Products List")
        print("2 - Add New Product")
        print("3 - Update Product")
        print("4 - Delete Product")

        choice = input("Select an option: ")

        if choice == "0":
            break
        elif choice == "1":
            print_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        else:
            print("Invalid choice. Please try again.")

# Orders Menu
def orders_menu():
    while True:
        print("\nOrders Menu:")
        print("0 - Return to Main Menu")
        print("1 - View Orders List")
        print("2 - Create New Order")
        print("3 - Update Order Status")
        print("4 - Update Existing Order")
        print("5 - Delete Order")

        choice = input("Select an option: ")

        if choice == "0":
            break
        elif choice == "1":
            print_orders()
        elif choice == "2":
            create_order()
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            update_order()
        elif choice == "5":
            delete_order()
        else:
            print("Invalid choice. Please try again.")

# Print Products List
def print_products():
    if not products:
        print("No products available.")
    else:
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")

# Add New Product
def add_product():
    id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append({"id": id, "name": name, "price": price})
    print("Product added successfully!")

# Update Product
def update_product():
    id = int(input("Enter product ID to update: "))
    product = next((prod for prod in products if prod["id"] == id), None)
    
    if product:
        name = input(f"Enter new name (current: {product['name']}): ")
        price = float(input(f"Enter new price (current: {product['price']:.2f}): "))
        product["name"] = name if name else product["name"]
        product["price"] = price if price else product["price"]
        print("Product updated successfully!")
    else:
        print("Product not found.")

# Delete Product
def delete_product():
    id = int(input("Enter product ID to delete: "))
    global products
    products = [prod for prod in products if prod["id"] != id]
    print("Product deleted successfully.")

# Print Orders List
def print_orders():
    if not orders:
        print("No orders available.")
    else:
        for order in orders:
            print(f"Order ID: {order['id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}, Status: {order['status']}")

# Create New Order
def create_order():
    id = int(input("Enter order ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    status = input("Enter order status: ")
    orders.append({"id": id, "product_id": product_id, "quantity": quantity, "status": status})
    print("Order created successfully!")

# Update Order Status
def update_order_status():
    print_orders()
    order_index = int(input("Enter the index of the order to update (0-based): "))
    if 0 <= order_index < len(orders):
        new_status = input("Enter new order status: ")
        orders[order_index]["status"] = new_status
        print("Order status updated successfully!")
    else:
        print("Invalid order index.")

# Update Existing Order
def update_order():
    print_orders()
    order_index = int(input("Enter the index of the order to update (0-based): "))
    if 0 <= order_index < len(orders):
        product_id = int(input(f"Enter new product ID (current: {orders[order_index]['product_id']}): "))
        quantity = int(input(f"Enter new quantity (current: {orders[order_index]['quantity']}): "))
        status = input(f"Enter new status (current: {orders[order_index]['status']}): ")
        
        orders[order_index]["product_id"] = product_id
        orders[order_index]["quantity"] = quantity
        orders[order_index]["status"] = status
        print("Order updated successfully!")
    else:
        print("Invalid order index.")

# Delete Order
def delete_order():
    print_orders()
    order_index = int(input("Enter the index of the order to delete (0-based): "))
    if 0 <= order_index < len(orders):
        del orders[order_index]
        print("Order deleted successfully!")
    else:
        print("Invalid order index.")

# Start the program
if __name__ == "__main__":
    main_menu()        