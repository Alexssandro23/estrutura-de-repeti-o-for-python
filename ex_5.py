soma=0
cont=0
for x in range(0,6):
    n=int(input("numero..:"))
    if n%2==0:
        cont+=1
        soma+=n
print("voçê informou {} valores e a soma é :{}".format(cont,soma))