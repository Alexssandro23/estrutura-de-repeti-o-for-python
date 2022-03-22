# frase=input("digite uma frase...:").lower()
# frase=frase.replace(" ","")
# print(frase)
# frase_inversa=frase[::-1]
# if frase==frase_inversa:
#     print("é palidromo")

#usando o for

frase=input('digite uma frase: ')
junto=frase.replace(" ","")
inverso=''
for letra in range(len(junto)-1, -1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('temos um palidromo !!!')
else:
    print('não é um palidromo !!!')
