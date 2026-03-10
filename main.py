from register_sales import register_sale
from calculate_totals import calculate_summary, print_summary

def main():

    sales = []
    option = "si"

    while option == "si":

        sale = register_sale()
        sales.append(sale)

        option = input("¿Desea registrar otra venta? (si/no): ").lower()

    product_summary, total_revenue = calculate_summary(sales)

    print_summary(product_summary, total_revenue)


main()