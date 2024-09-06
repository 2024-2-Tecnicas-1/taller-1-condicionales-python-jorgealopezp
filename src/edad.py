from time import localtime
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year

    edad = anno_actual - anno

    if mes_actual < mes:
        edad -= 1
    elif mes_actual == mes and dia_actual < dia:
        edad -= 1

    return f"Usted tiene {edad} años"


if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
