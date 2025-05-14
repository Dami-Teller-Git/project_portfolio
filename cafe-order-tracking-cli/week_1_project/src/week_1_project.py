main_menu = ["croissant", "pretzel", "salad", "baguette"]

product_list= ["Exit App", " Print Main Menu", "Add New Item", "Update Exisiting Item", "Delete a Product"] 

def manage_main_menu():
    # Initial list of food

   

    while True: # Loop to allow multiple inputs
            
        print(f"\n Current food List: {main_menu}")
        user_input = int(input("Enter a number (0 to exit app, 1 to print main menu, 2 to add a new item, 3 to update exisiting item and 4 to delete a product):"))
        for index, product in enumerate (main_menu):
                print(f" Index {index}: {product}")
        if user_input == 0: 
            
            # Simply exiting the app

            print("Exiting app")
    
            continue
        elif user_input == 1:
            print(main_menu [0])
            print(main_menu [1])
            print(main_menu [2])
            print(main_menu [3])
        elif user_input == 2:
            # Ask the user for a new food item to add

            new_product = input ("Which food item would you like to add: ")
            main_menu.append(new_product)
            print(f"{new_product} has been added.")
        elif user_input == 3:
            print("Here is the list of products:")
        for index, product in enumerate (main_menu):
            print (f" Index {index}: {product}")
# Step 2: Get user input for the index   
manage_main_menu()
try:    
    update_index = int(input("Enter the index you wish to update:"))
    # Step 3: Validate the index
    if 0 <= update_index < len(main_menu):
        # Step 4: Ask for the product name
        new_product_name = input ("Enter the new product name: ")
        # Step 5: Update the product in the list 
        main_menu [update_index] = new_product_name
        print(f" Product updated sucessfully! Here is the updated list:")
        for index, product in enumerate (main_menu):
            print(f"{index}: {product}")
    else:
        print("Invalid Index, Please enter a number between 0 and", len(main_menu) -1)
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Stretch goal - delete product
        