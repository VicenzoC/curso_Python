"""numeros = [0, 0, 0, 0]
for rep in range(1,6):
    num = int(input('Digite um número: '))
    if rep == 1:
        numeros.append(num)
    else:
        if num > numeros[0]:
            if num > numeros[1]:
                if num > numeros[2]:
                    if num > numeros[3]:
                        if num > numeros[4]:
                            numeros.remove(0)
                            numeros.append(num)
                        else:
                            numeros.remove(0)
                            numeros.insert(3, num)
                    else:
                        numeros.remove(0)
                        numeros.insert(2, num)
                else:
                    numeros.remove(0)
                    numeros.insert(1, num)
            else:
                numeros.remove(0)
                numeros.insert(0, num)
        else:
            numeros.remove(0)
            numeros.insert(0, num)
    print(numeros)"""
numeros = []
for rep in range(0, 5):
    n = int(input('Digite um número: '))
    if rep == 0 or n >= numeros[-1]:
        numeros.append(n)
    else:
        for pos in range(0, 6):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
print(numeros)