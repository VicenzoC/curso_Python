inverso = ''
f = str(input('Digite uma frase: ')).strip().upper()
fsem = f.replace(' ','')
for inv in range (len(fsem) - 1, -1 , -1):
    inverso += fsem[inv]
if fsem == inverso:
    print(fsem, inverso, '\né palíndromo')
else:
    print('Não é palíndromo')
