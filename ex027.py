nome = str(input('Qual seu nome? '))
n = nome.title().strip().split()
pn = n[0]
x = len(n) - 1
un = n[x]
print('Primeiro nome: {}\nÚltimo nome: {}'.format(pn, un))
