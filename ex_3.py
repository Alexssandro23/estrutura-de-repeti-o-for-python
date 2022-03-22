count=0
soma=0
for x in range(1,501,2):
    if x%3==0:
        print(x, end=' ')
        count+=1
        soma+=x
print("\na soma de todos os {} valores impares multiplos de 3 é :{}".format(count,soma))