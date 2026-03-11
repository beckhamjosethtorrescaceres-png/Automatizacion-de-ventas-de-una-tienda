def register_sale():
    print("\nSale Registration")
    

      # Validación del producto
    while True:
        product = input("Enter the product name: ").strip()
        if product:
            break
        else:
            print("El nombre del producto no puede estar vacío.")
    # Price validation
    validating_price = True
    while validating_price:
        price_input = input("Enter the unit price: ")
        try:
            price = float(price_input)
            if price > 0:
                validating_price = False
            else:
                print(" The price must be greater than 0.")
        except ValueError:
            print(" You must enter a valid number for the price.")

    # Quantity validation
    validating_quantity = True
    while validating_quantity:
        quantity_input = input("Enter the quantity sold: ")
        try:
            quantity = int(quantity_input)
            if quantity > 0:
                validating_quantity = False
            else:
                print(" The quantity must be greater than 0.")
        except ValueError:
            print(" You must enter a valid integer for the quantity.")

    total = price * quantity

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    return sale