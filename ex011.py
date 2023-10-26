l = float(input('Qual a largura de sua parede em metros? '))
a = float(input('Qual a altura de sua parede em metros? '))
ar = l * a
t = ar/2
print('Você precisará de {} litros de tinta para pintar os {}m² desta parede.'.format(t, ar))
