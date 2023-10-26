dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
pd = dia * 60
pk = km * 0.15
t = pd + pk
print('Você irá pagar R${:.2f}'.format(t))
