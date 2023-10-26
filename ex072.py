tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', ' dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while 0 > num or num > 20:
        num = int(input('Número inválido, digite novamente um número entre 0 e 20: '))

    print(f'O número digitado foi {tupla[num]}')
