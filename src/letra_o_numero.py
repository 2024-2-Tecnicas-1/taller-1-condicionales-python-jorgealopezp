def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    if len(caracter) != 1:
        return "Error: el argumento debe ser un caracter"
    character = caracter[0]
    if character.isdigit():
        return "Es número"
    elif character.isalpha():
        if character.isupper():
            return "Es letra mayúscula"
        else:
            return "Es letra minúscula"
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
