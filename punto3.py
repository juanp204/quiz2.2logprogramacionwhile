dia = ["El Dia Del Apocalipsis", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
while True:
    try:
        num = int(input("ingrese numero de la semana = "))
        if num>7 or num<0:
            print("solo numeros entre 1 y 7")
        else:
            print("el dia de la semana es" ,dia[num])
            break
    except ValueError:
        print("sin letras")