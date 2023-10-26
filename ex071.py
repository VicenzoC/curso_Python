cont = 0
valor = int(input('Qual valor será sacado? R$'))
quantidade50 = valor // 50
quantidade20 = (valor % 50) // 20
quantidade10 = ((valor % 50) % 20) // 10
quantidade5 = (((valor % 50) % 20) % 10) // 5
quantidade2 = ((((valor % 50) % 20) % 10) % 5) // 2
print(f'Para o valor de R${valor:.2f} serão necessárias:\n'
      f'{quantidade50} notas de R$50.00\n'
      f'{quantidade20} notas de R$20.00\n'
      f'{quantidade10} notas de R$10.00\n'
      f'{quantidade5} notas de R$5.00\n'
      f'{quantidade2} notas de R$2.00')