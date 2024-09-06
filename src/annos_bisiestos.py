def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    if anno < 1582:  # Calendario juliano
        if anno % 4 == 0:
            return f"{anno} es bisiesto"
        else:
            return f"{anno} no es bisiesto"
    else:  # Calendario gregoriano
        if (anno % 4 == 0 and anno % 100 != 0) or anno % 400 == 0:
            return f"{anno} es bisiesto"
        else:
            return f"{anno} no es bisiesto"

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
