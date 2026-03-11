from register_sales import register_sale
from calculate_totals import calculate_summary, print_summary

def main():

    sales = []
    option = "yes"

    while option == "yes":

        sale = register_sale()
        sales.append(sale)

        option = input("Do you want to register another sale? (yes/no) : ").lower()

    product_summary, total_revenue = calculate_summary(sales)

    print_summary(product_summary, total_revenue)


main()