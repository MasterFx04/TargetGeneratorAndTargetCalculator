#valinitial = input("Ingresa el numero de la tarjeta: ")


def algortim(code):
    
    fullcode = code
    #longitud = code[4]
    #longitud = len(code)

    #code = code[:-1]
    sumtotal = 0
    #print(code)
    for digito in str(code)[0::2]:
        multi = int(digito) * 2
    
        multi = sum(int(suma) for suma in str(multi))
    
        sumtotal += multi
        #print(multi)
    
    newlist = str(code)[1::2]

    for sum2 in newlist:
        #print(sum2)
        sumtotal += int(sum2)

    #print(f'el total es: {sumtotal}')

    #sumtotal *= 9
    #print(sumtotal)

    sumtotal = str(sumtotal)

    #print(sumtotal[len(sumtotal) -1])



    #if sumtotal[len(sumtotal) -1] == fullcode[len(fullcode) -1]:
        #print("La tarjeta es valida")
    #else:
        #print("La tarjeta no es valida")
        
    if int(sumtotal) % 10 == 0:
        print("La tarjeta es valida")
    else:
        print("La tarjeta no es valida")







#VALIDACION DE NUMERO DE DIGITOS DE LA TARJETA


#print(f'el numero de la tarjeta es: {code}')
while True:
    try:
        valinitial = input("Ingresa el numero de la tarjeta: ")
        
        if len(valinitial) != 16:
            raise ValueError("El numero de digitos de la tarjeta no son los correctos, intente denuevo..")
        
        algortim(valinitial)
        print("La verificacion de la tarjeta fue un exito!")
        print("Saliendo...")
        break
    
    except ValueError as e:
        print(f"Error: {e}")


    