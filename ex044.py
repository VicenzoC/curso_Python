#Gerenciador de pagamento
valor = float(input('Qual o valor das suas compras? R$'))
fpag = int(input('[1] = Á vista dinheiro/cheque (10% de desconto)\n[2] = Á vista no cartão (5% de desconto)\n[3] = 2x no cartão\n[4] = 3x ou mais no cartão (20% de juros)\nDigite sua escolha: '))
if fpag == 1:
    valorf = valor - (valor * 0.1)
elif fpag == 2:
    valorf = valor - (valor * 0.05)
elif fpag == 3:
    valorf = valor / 2
    print('O valor de R${:.2f} será parcelado em 2x de R${:.2f}'.format(valor, valorf))
elif fpag == 4:
    parc = int(input('Quantas parcelas? '))
    valorf = (valor / parc) + ((valor / parc) * 0.2)
    print('O valor de R${:.2f} será parcelado em {}x de R${:.2f}'.format(valor, parc, valorf))
else:
    print('Forma de pagamento inválida, tente novamente.')
    exit()
if fpag == 1 or fpag == 2:
    print('O valor final para pagamento será de R${:.2f}'.format(valorf))
