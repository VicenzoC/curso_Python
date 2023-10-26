cdd = str(input('Qual o nome da sua cidade? '))
reg = cdd.upper().split()

print('Sua cidade começa com Santo? {}'.format('SANTO' in reg[0]))
