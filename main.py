from register_sales import register_sale
from calculate_totals import calculate_summary, print_summary
from ask_another_sale import ask_another_sale

sales = []

another_sale = True

while another_sale == True:
    sale = register_sale()
    sales.append(sale)

    another_sale = ask_another_sale()

product_summary, total_revenue = calculate_summary(sales)

print_summary(product_summary, total_revenue)