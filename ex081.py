cont = 0
numeros = list()
while True:
    num = int(input('Digite um número (-1 para sair): '))
    if num != -1:
        cont += 1
        numeros.append(num)
        print('Adicionado com sucesso!')
    else:
        break
if numeros.count(5) > 0:
    tem5 = True
else:
    tem5 = False
numeros.sort(reverse=True)
print(f'A) A quantidade de números digitados foi {cont}\n'
      f'B) A lista de números de forma decrescente é {numeros}\n'
      f'C) O número 5 está na lista? {tem5}')