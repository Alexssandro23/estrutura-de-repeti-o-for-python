from datetime import date
ano=date.today().year
d_maior=0
d_menor=0
for x in range(0,7):
    nasc=int(input("pessoa {} informe seu ano de nascimento: ".format(x+1)))
    idade=ano-nasc
    if  idade>= 18 :
        print('é maior !!!')
        d_maior+=1
    else:
        print('é menor !!!')
        d_menor+=1    
print("{} são maiores de idade".format(d_maior))
print("{} são menores de idade".format(d_menor))