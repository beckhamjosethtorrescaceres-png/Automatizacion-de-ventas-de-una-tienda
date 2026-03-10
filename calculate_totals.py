# Function to calculate totals
def calculate_summary(sales):

    product_summary = {}
    total_revenue = 0

    for sale in sales:

        product = sale["product"]
        quantity = sale["quantity"]
        price = sale["price"]

        total_revenue += sale["total"]

        if product in product_summary:
            product_summary[product]["quantity"] += quantity
        else:
            product_summary[product] = {
                "price": price,
                "quantity": quantity
            }

    return product_summary, total_revenue


# Function to print final report
def print_summary(product_summary, total_revenue):

    print("\nRESUMEN DE VENTAS DEL DÍA")
    print("-------------------------")

    for product, data in product_summary.items():

        print(f"Producto: {product}")
        print(f"Precio unitario: ${data['price']}")
        print(f"Cantidad total vendida: {data['quantity']}\n")

    print(f"Total recaudado: ${total_revenue}")