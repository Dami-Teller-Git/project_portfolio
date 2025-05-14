# Generation Bootcamp Mini Project

# Project Background Overview
My client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders. The program provides options for managing products, viewing orders, creating new orders, and handling courier services. This project is built as a simple, menu-driven program where users can interact with different features such as adding products, updating orders, and managing couriers.

# Client Requirements
The client would like the following:
  To maintain a collection of `products` and `couriers`. 
  When a customer makes a new `order`, I need to create this on the system. 
  I need to be able to update the status of an `order` i.e: `preparing`, `out-for-delivery`, `delivered`. 
  When I exit my app, I need all data to be persisted and not lost. 
  When I start my app, I need to load all persisted data. 
  I need to be sure my app has been tested and proven to work well. 
  I need to receive regular software updates. 

  # Technical specificiations
  The client also has the below specs that needs to be adhered to:
  I will be building a program that runs on the command line (CLI). 

- UI should be logical, clear, and simple to navigate. 
- It should display a menu of options; some may be nested. 
- There should be the option to exit / return to main menu. 
- It should handle invalid input.

  # Data Persistence
  Initially the data will be stored in plain text files but overtime, the data will need to be switched to csv and then finally SQL

  # Testing
  The code wll need to be robust to prevent it from breaking
  
 # How to run the app 
 To run my app, you will need to open the file onto VS code or obtain it from Git. You will then need to open a terminal and press the execute (play) button and let the magic happen.

The program will present a main menu with the following options:
Products Menu: Manage products (view, add, update, delete).
Orders Menu: Manage orders (view, create, update status, delete).
Courier Menu: Manage couriers (view, add, update, delete).
Exit: Exit the program.
Using the numbers 0,1,2,3 will help navigate you to where you need to go 

# Core Functions
- main_menu(): Displays the main menu and navigates to other sections.
- products_menu(): Displays options related to products.
- orders_menu(): Displays options related to orders.
- courier_menu(): Displays options related to couriers.
- view_courier_list(): Displays the list of couriers.
- print_products(): Displays the list of products.
- create_order(): Creates a new order and adds it to the order list.
- update_product(): Updates product details (name, price).
- update_order(): Updates order details (product ID, quantity, status).
- delete_product(): Deletes a product from the list.
- delete_order(): Deletes an order from the list.
- add_courier(): Adds a new courier to the list.
- update_courier(): Updates the details of a courier.
- delete_courier(): Deletes a courier from the list.

# How did your design go about meeting the project's requirements? 
To the best of my ability, i followed the weekly project requirements set out by Brian/Jess/Jas leaning on the powerpoints provided and on my cohort during the breakout rooms.

# How did you guarantee the project's requirements? 
I highlighted in green every part of the project requirement i had implemented in red. Once i ran my code and executed the code successfully, i then highlighted the project requirement in green to indicate to me that i could move onto the next task.

# If you had more time, what is one thing you would improve upon? 
I would try to stay up to date with the weeks so that i could have got further with the mini project. There was some topics being taught that i did not understand straight away so i had to use the project time to go over the notes and do my own independent research. This helped me understand the concepts being taught but inadvertently made me fall behind on my mini task. 

# What did you most enjoy implementing? 
Honestly, i would say everything because i am new to coding to everything i found interesting. If i had to pick one i would say it was implementing functions because functions took me such a long time to wrap my head around.





