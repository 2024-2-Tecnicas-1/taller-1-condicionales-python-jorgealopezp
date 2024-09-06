def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    cociente = dividendo // divisor
    residuo = dividendo % divisor

    if residuo == 0:
        return f"La división es exacta. \nCociente: {cociente}\nResiduo: {residuo}"
    else:
        return f"La división no es exacta. \nCociente: {cociente}\nResiduo: {residuo}"

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
