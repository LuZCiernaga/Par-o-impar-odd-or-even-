num = int (input ("Esscribe un numero entre 0 y 1000: "))
for i in range (1,1000 +1) :
    if (num % 2 == 0):
        print (num, "es un numero par" )
        break
    elif (num %2==1):
        print ( num, "es un numero impar" )
        break
