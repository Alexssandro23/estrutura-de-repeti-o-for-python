maior=0
menor=0
for x in range(0,5):
    peso=float(input("peso da {} pessoa:".format(x+1)))
    if x==0:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso    
print('o maior peso lido foi de: {}kg'.format(maior))     
print('o menor peso lido foi de: {}kg'.format(menor))     
