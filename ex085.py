numeros = [[], []]
for p in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'A lista de números é: {numeros}\n'
      f'A lista de pares é: {numeros[0]}\n'
      f'A lista de ímpares é: {numeros[1]}')
