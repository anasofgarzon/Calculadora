def calcular_operacion():
    print("\nVamos a operar dos números, mediante suma, resta, multiplicación o división (+,-,*,/)")
    print("Usa los respectivos símbolos.\n")

    while True:
        entrada = input("Por favor, digite su operación (ejemplo: 5 + 3): ").strip()
        entrada = entrada.replace(" ", "")

        operadores = ['+', '-', '*', '/']
        operador_encontrado = None

        for op in operadores:
            if op in entrada:
                partes = entrada.split(op)
                if len(partes) == 2:
                    operador_encontrado = op
                    break

        if operador_encontrado is None:
            print("Error: No se encontró una operación válida. Use +, -, * o / entre dos números.\n")
            continue

        num1_str, num2_str = partes[0], partes[1]

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Error: Ambos valores deben ser números.\n")
            continue

        if operador_encontrado == '+':
            resultado = num1 + num2
        elif operador_encontrado == '-':
            resultado = num1 - num2
        elif operador_encontrado == '*':
            resultado = num1 * num2
        elif operador_encontrado == '/':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.\n")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}\n")

        continuar = input("¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar la calculadora.")
            break

calcular_operacion()