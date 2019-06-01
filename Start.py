def verificar(com, total, multiplicadores, rut, rutf):
    if len(rut) != 9:
        rut = "0" + rut
    lenrut = len(rut) - 1 
    if(rut[-1] == "k" or rut[-1] == "K" and rut[-1] != 10): fino = 5
    for i in range(lenrut):
        rutf.append(rut[i])
        total += int(rutf[i]) * multiplicadores[i]
    com = 11 - (total % 11)
    if(str(rut[-1]) == str(com)): print("Rut correcto! ") 
    elif str(rut[-1]) == "k" and 10 == (fino * 2) and com == 10:  print("Rut correcto!" )
    else: print("Rut incorrecto ")  
    respuesta = input("Probar con otro rut? -1 para salir : 1 para reintentar  ")
    if(respuesta == "1"): verificar(0, 0, multiplicadores = [3, 2, 7, 6, 5, 4, 3, 2], rut = input("Ingrese el rut que desee verificar : "),  rutf = [])
verificar(com = 0, total = 0, multiplicadores = [3, 2, 7, 6, 5, 4, 3, 2], rut = input("Ingrese el rut que desee verificar : "),  rutf = [])
          