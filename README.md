# Automatizaci-n-de-ventas-de-una-tienda
# Daily Sales Register

## Description
This project is a Python script designed to help a small store register daily sales and generate a summary report.

The system allows the user to:
- Register multiple sales during the execution
- Store product name, price, and quantity
- Calculate totals automatically
- Generate a final report of products sold and total revenue

## Strategy

The solution uses a list to store sales data. Each sale is represented as a dictionary containing product information.

The program is divided into functions:

- register_sale() → captures user input
- calculate_summary() → processes sales data
- print_summary() → prints the final report
- main() → controls program execution

The script also imports the `datetime` module to display when the report was generated.

## Technologies
- Python
