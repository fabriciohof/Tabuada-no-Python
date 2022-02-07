# TABUADA NO PYTHON


print(' TABUADA ')

while True:
    numero = int(input('Digite um número: '))

    if numero <= 0:
        break

    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

    print('     ')

print('PROGRAMA ENCERRADO COM SUCESSO!')

