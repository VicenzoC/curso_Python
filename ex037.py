n = int(input('Digite um número: '))
b = int(input('Escolha uma base numérica para conversão\n1 = Binário\n2 = Octal\n3 = Hexadecimal\nDigite: '))
if b == 1:
    num = bin(n)
    btipo = 'binário'
elif b == 2:
    num = oct(n)
    btipo = 'octal'
elif b == 3:
    num = hex(n)
    btipo = 'hexadecimal'
else:
    print('ERROR\nVocê digitou um valor inválido para a base numérica!')
    exit()
print('O número {} convertido para {} é igual a {}'.format(n, btipo, num[2:]))
