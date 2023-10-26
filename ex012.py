p = float(input('Qual o preço do produto? '))
pd = p - (p * 5 / 100)
print('O preço do produto com 5% de desconto será de R${:.2f}!'.format(pd))
