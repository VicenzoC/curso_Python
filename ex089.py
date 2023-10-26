lista = list()
nome = list()
nota = list()
while True:
    nm = input('nome ("SAIR" para parar): ')
    if nm == 'SAIR':
        break
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    nota.append(n1)
    nota.append(n2)
    nome.append(nm)
    nome.append(nota[:])
    lista.append(nome[:])
    nota.clear()
    nome.clear()
print()
print(f'{"NÚM":^4}/{"NOME":^10}/{"MÉDIA":^5}')
for num, aluno in enumerate(lista):
    print(f'{num:^4}/{aluno[0]:^10}/{(aluno[1][0] + aluno[1][1])/2:^5.1f}')
while True:
    numero = int(input('Deseja ver as notas de qual aluno? (999 para sair) '))
    if numero == 999:
        break
    print(f'As notas do aluno {lista[numero][0]} são: {lista[numero][1][0]} e {lista[numero][1][1]}')
