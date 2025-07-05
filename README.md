#         __ORDER MANAGEMENT SYSTEM IN A RESTAURANT__
## __Video Demo__: https://youtu.be/585p3XPpC90
## __Description of the program:__
          This project is based on Ordering System is a command-line-based Python application designed to simulate a restaurant's menu ordering and payment process. It allows users to browse through different categories of food, place orders, and make payments, all within a user-friendly, interactive interface.
## __Modules:__
__Module Imports__

*tabulate* - Used tabulate library to show different items of the menu in the format of tables.

*sys* - Used this library to exit from the process while ordering food.

## __Functions Used__

### *Main() Function:*
Serves as the main entry point of the program, handling initial user input and driving the application flow.The program starts by printing a welcome message and presenting two options: Menu or Help.
The user is prompted to enter their preference. If the user selects Menu, the menu() function is called to display the menu. If the user selects Help, they are shown a message encouraging them to check the menu to place an order.The main() function is called recursively if the user selects Help, providing an easy way to guide them back to the menu.

### *csv_list() Function:*
This function reads data from a CSV file (python.csv) containing information about the restaurant's menu items. It processes the data to create a list of items, their IDs, and prices.It opens the python.csv file and reads each line.Each line is split by , (comma), where the first value is the item ID, the second is the item name, and the third is the price.The item data is stored in a list called csv, where each item’s ID and price are stored as integers, and the item name is stored as a string.Returns the csv list containing the menu data.The csv_list() function is called when the system needs to retrieve menu data for order processing, such as when a user chooses to order a particular item.

### *breakfast() Funtion:*
Displays the breakfast items on the menu for the user to view and select from.This function prints a welcoming message, introducing the "Infinity Platter Breakfast".A list of breakfast items (Dosa, Idly, Puri, Bonda) with their respective IDs and prices is displayed using the tabulate library, which organizes the data into a neat table format.The table includes headers ("Id", "Item", "Price") and uses the grid table format for better readability.The breakfast() function is called when a user selects the "Breakfast" category from the menu, allowing them to browse the available breakfast items.

### *meals() Function:*
Displays the meals section of the menu for the user to view and select from.This function prints a message introducing the "Infinity Platter Meals".A list of meal options (Pulihora, Full Meals, Thali, Veg Pulao, Chicken Biryani, Mutton Biryani) is displayed, along with their IDs and prices, in a tabulated format using the tabulate library.The meals() function is invoked when the user chooses the "Meals" category from the menu, allowing them to explore and order meals.

### *delicacy() Function:*
Displays the delicacies section of the menu for the user to view and select from.This function introduces the "Infinity Platter Delicacies" and prints a message to encourage customers to indulge in the restaurant's specialty desserts.It displays a list of dessert items (Gulab Jamun, Halwa, Rasgulla, Rasmalai) along with their corresponding IDs and prices in a well-formatted table.The delicacy() function is used when the user selects the "Delicacies" category from the menu, allowing them to choose from a range of desserts.

### *ice() Function:*
Displays the ice cream section of the menu for the user to view and select from.This function introduces the "Infinity Platter Ice Cream" section, emphasizing the variety of ice cream flavors available.It shows a list of ice cream options (Vanilla, Chocolate, Butter Scotch, Strawberry, Dark Forest), along with their IDs and prices, in a grid format using the tabulate library.The ice() function is triggered when the user opts for the "Ice Cream" category, allowing them to browse and order ice cream flavors.

### *menu() Function:*
Displays the main menu and allows the user to choose a category (Breakfast, Meals, Delicacies, Ice Cream).This function prints the four main categories available in the restaurant: Breakfast, Meals, Delicacies, and Ice Cream.The user is prompted to enter a number corresponding to the category they want to explore.Based on the user’s choice, the function calls one of the category-specific functions (breakfast(), meals(), delicacy(), or ice()), displaying the menu items for that category.The menu() function is the entry point to the menu system, allowing users to navigate and select different food categories.

### *order() Function:*
Manages the process of selecting and ordering food items.This function allows the user to place an order by entering the item ID of the food they wish to order.It continuously asks the user for an item ID and quantity until the user is ready to proceed with the payment or exit.The function checks if the item ID entered by the user exists in the csv_list(). If valid, the order is confirmed, and the user is prompted for the number of plates to order.The total cost is updated after each item is added to the order.The user can choose to add more items, return to the menu, or proceed to payment. If an invalid item ID is entered, the user is prompted again to choose a valid ID.The order() function is called after the user has chosen a food category, and it allows them to customize their order by selecting items and specifying quantities.

### *payment() Function:*
Handles the payment process and ensures the user pays the correct amount for their order.After the order is placed, the user is prompted to enter the payment amount.The function checks if the payment is sufficient, i.e., greater than or equal to the total cost of the order.If the payment is insufficient, the user is asked to enter the correct amount.If the payment is more than the required cost, the system calculates and displays the change.After the transaction is completed, the function displays a message confirming the payment and thanking the customer for visiting.The payment() function is invoked after the user confirms their order and is ready to make the payment.

### *Try() and Except():*
The try and except blocks are used for error handling. Specifically, they are used to catch potential exceptions that may arise due to incorrect user input or other runtime errors.

## __Conclusion__
This system allows restaurant staff or developers to manage food categories, menu items, and the overall customer interaction without the need for a physical menu or point-of-sale (POS) system.

