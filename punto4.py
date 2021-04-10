print("no coloque nada para cerrar")
print("para usar el programa use la siguiente sintaxys:","valor1","operacion","valor2","  ejemplo: 1 + 1")
while True:
    caja = input()
    valor1 = ""
    valor2 = ""
    operacion = str
    paso = 0
    for numf in caja:
        if numf in " ":
            paso +=1
        if numf in "/*-+%x":
            operacion = numf
            paso += 1
        elif paso == 0:
            valor1 = valor1 + numf
        else:
            valor2 = valor2 + numf
    if paso>=3:
        print("a ocurrido un error muchos espacios")
        continue
    if bool(valor1) == False:
        print("cerrando...")
        break
    try:
        valor1 = float(valor1)
        if paso == 0:
            print(valor1)
            continue
        valor2 = float(valor2)
    except ValueError:
        print("solo números")
        continue
    if operacion in "*x":
        re = valor1*valor2
    elif operacion in "/%":
        re = valor1/valor2
    elif operacion in "+":
        re = valor1+valor2
    elif operacion in "-":
        re = valor1-valor2
    else:
        print("no hay operación que hacer")
        continue
    print(re)