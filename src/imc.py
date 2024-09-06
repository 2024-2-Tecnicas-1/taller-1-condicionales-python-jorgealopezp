def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = peso / (estatura ** 2)

    if edad < 45:
        if imc < 22:
            return "bajo"
        elif imc < 27:
            return "medio"
        else:
            return "alto"
    else:
        if imc < 25:
            return "medio"
        elif imc < 30:
            return "alto"
        else:
            return "alto"

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
