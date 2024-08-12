import random

def algortim(code):
    validate = False
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
        validate = True
        
        return validate
    
    else:
        print("La tarjeta no es valida")


def searchCV(code):
    print(code)
    

#Validacion, tarjeta de credito
while True:
    numero = ''
    for ale in range(0,16):
        ale = random.randint(0,9)
        numero += str(ale)
    print(numero)
    resultado = algortim(numero)
    
    if resultado:
        break
        
      
    

    

