n=int(input("numero: "))
div=0
for x in range(n,0,-1):
    if n%x==0:
        print('\033[33m', end=' ')
        div+=1
    else:
        print('\033[31m', end=' ')
    print(x, end=' ')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(n,div))
if div==2:
    print('é primo !!!')
else:
    print("não é primo !!!")