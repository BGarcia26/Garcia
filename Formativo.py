precios = [4500, 5000, 5200, 4800]
nombres = ["Pikachu Roll", "Otaku Roll", "Pulpo Venenoso Roll", "Anguila Eléctrica Roll"]

while True:
    pedidos = [0, 0, 0, 0]

    while True:
        # Mostrar menú
        print("\nBienvenido a SushiOtaku")
        print("1. Pikachu Roll $4500")
        print("2. Otaku Roll $5000")
        print("3. Pulpo Venenoso Roll $5200")
        print("4. Anguila Eléctrica Roll $4800")
        print("5. Finalizar pedido")

        # Pedir opción
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 4:
                cantidad = int(input("¿Cuántas unidades desea?: "))
                pedidos[opcion - 1] += cantidad
            elif opcion == 5:
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Calcular subtotal
    subtotal = sum(pedidos[i] * precios[i] for i in range(len(precios)))

    # Aplicar descuento
    while True:
        tiene_codigo = input("¿Posee un código de descuento? (s/n): ").strip()[0].lower()
        if tiene_codigo == "s":
            codigo = input("Ingrese el código de descuento: ").strip().lower()
            if codigo == "soyotaku":
                descuento = 0.1 * subtotal
                break
            else:
                print("Código no válido.")
                opcion = input("¿Desea reingresar el código de descuento o volver al resumen? (r/x): ").strip().lower()
                if opcion == "x":
                    descuento = 0
                    break
        elif tiene_codigo == "n":
            descuento = 0
            break
        else:
            print("Opción inválida.")

    # Mostrar resumen
    print("\n****************** RESUMEN DEL PEDIDO ******************")
    total_productos = sum(pedidos)
    print(f"TOTAL PRODUCTOS: {total_productos}")
    print("----------------------------------------------------------")
    for i in range(len(pedidos)):
        print(f"{nombres[i]}: {pedidos[i]}")
    print("----------------------------------------------------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${int(descuento)}")
    print(f"TOTAL A PAGAR: ${int(subtotal - descuento)}")
    print("**********************************************************")

    # Consultar si desea otro pedido
    otro = input("¿Desea realizar otro pedido? (s/n): ").strip()[0].lower()
    if otro != "s":
        print("\nGracias por preferirnos\n")
        break
