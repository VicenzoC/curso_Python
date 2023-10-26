tupla = ('Pão', 1.50,
         'Manteiga', 7.30,
         'Ovo', 14.50,
         'Queijo', 10.00)
print('{:_^50}'.format('listagem de preços'))
print('{:.<43}R${:>6.2f}\n'#tupla[0], tupla[1],
      '{:.<43}R${:>6.2f}\n'#tupla[2], tupla[3],
      '{:.<43}R${:>6.2f}\n'#tupla[4], tupla[5],
      '{:.<43}R${:>6.2f}'  #tupla[6], tupla[7]
      .format(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7]))
