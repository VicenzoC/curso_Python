print('\033[7;32m{}\033[m\n'
      '\033[7;38m{:^90}\033[m\n'
      '\033[7;32m{}\033[m'
      .format('-' * 90, 'EMPRÉSTIMO BANCÁRIO', '-' * 90))
vcasa = float(input('Qual o valor da casa? ').strip())
sal = float(input('Qual seu salário? ').strip())
tempo = int(input('Em quantos anos quer pagar o empréstimo? ').strip())
mens = vcasa / (tempo * 12)
if mens > sal * 0.3:
    print('\033[31m{}\n'
          '{:^90}\n'
          '{}\033[m'.format('-' * 90, 'Empréstimo Negado! A mensalidade excede 30% do seu salário.', '-' * 90))
else:
    print('\033[32m-' * 90)
    print('\033[32mSeu empréstimo foi aceito!\n'
          'Sua casa de \033[34mR${:.2f}\033[32m poderá ser comprada!\n'
          'A mensalidade do empréstimo é de \033[34mR${:.2f}'.format(vcasa, mens))
    print('\033[32m-' * 90)
print('\033[7;32m{}\033[m\n'
      '\033[7;38m{:^90}\033[m\n'
      '\033[7;32m{}\033[m'.format('-' * 90, 'Volte sempre!', '-' * 90))
