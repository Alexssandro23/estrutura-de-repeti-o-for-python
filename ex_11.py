# pessoa=[]
# for x in range(0,4):
#     print('*'*20)
#     cadastro=[input("nome:"),
#               input("idade:"),
#               input("sexo:")]
#     pessoa.append(cadastro)


# print(pessoa)

# curso em video
s_idade=0
m_idade=0
maior_idade_homem=0
nome_h_mais_v=''
mulher_menosd_vinte=0
for p in range(1,5):
    print("******** {} pessoa ***********".format(p))
    nome=str(input("nome: ")).strip()
    idade=int(input("idade: "))
    sexo=str(input("sexo [M/F]: ")).strip() 
    s_idade+=idade
    if p==1 and sexo in 'Mm':
        maior_idade_homem=idade
        nome_h_mais_v=nome
    if sexo in'Mm'and idade>maior_idade_homem:
        maior_idade_homem=idade 
        nome_h_mais_v=nome   
    if sexo in 'Ff'and idade<20:
        mulher_menosd_vinte+=1

m_idade=s_idade/4
print("a média de idade do grupo é de {} anos".format(m_idade))
print("o homem mais velho tem {} anos e se chama {}".format(maior_idade_homem,nome_h_mais_v))
print("{} mulheres tem menos de 20 anos".format(mulher_menosd_vinte))