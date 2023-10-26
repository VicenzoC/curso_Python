#Tratando vários valores v1.0
soma = 0
cont = 0
e = 0
while e != 999:
    e = int(input('Digite um valor (999 para sair): '))
    if e != 999:
        cont += 1
        soma += e
print('A soma dos {} números foi de {}'.format(cont, soma))