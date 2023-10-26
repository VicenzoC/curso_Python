numeros = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um número (-1 para sair): '))
    if num != -1:
        numeros.append(num)
        print('Adicionado com sucesso!')
    else:
        break
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
numeros.sort()
par.sort()
impar.sort()
print(f'A lista de números é {numeros}\n'
      f'A lista de números pares é {par}\n'
      f'A lista de números ímpares é {impar}')
