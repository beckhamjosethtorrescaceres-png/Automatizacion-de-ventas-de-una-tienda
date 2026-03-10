# Function to register a sale
def register_sale():
    print ("\nRegistro de venta")
    product = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio unitario: "))
    quantity = int(input("Ingrese la cantidad vendida: "))

    total = price * quantity

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    return sale
