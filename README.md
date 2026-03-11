# Store Sales Automation
# Daily Sales Log

## Description
This project is a Python script designed to help a small store record daily sales and generate a summary report.

The system allows the user to:
- Record multiple sales during execution
- Store the product name, price, and quantity
- Automatically calculate totals
- Generate a final report of products sold and total revenue

## Strategy

The solution uses a list to store sales data. Each sale is represented as a dictionary containing product information.

The program is divided into functions:

- register_sale() → captures user input
- calculate_totals() → processes sales data and displays a summary of the day's sales
- main() → controls program execution

## Technologies
- Python