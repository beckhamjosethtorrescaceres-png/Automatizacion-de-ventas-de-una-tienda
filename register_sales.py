def register_sale():
    print("\nRegistro de venta")

    product = input("Ingrese el nombre del producto: ").strip()

    # Validación del precio
    validando_precio = True
    while validando_precio:
        price_input = input("Ingrese el precio unitario: ")
        try:
            price = float(price_input)
            if price > 0:
                validando_precio = False  
            else:
                print(" El precio debe ser mayor a 0.")
        except ValueError:
            print(" Debe ingresar un número válido para el precio.")

    # Validación de la cantidad
    validando_cantidad = True
    while validando_cantidad:
        quantity_input = input("Ingrese la cantidad vendida: ")
        try:
            quantity = int(quantity_input)
            if quantity > 0:
                validando_cantidad = False 
            else:
                print(" La cantidad debe ser mayor a 0.")
        except ValueError:
            print(" Debe ingresar un número entero válido para la cantidad.")

    total = price * quantity

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    return sale