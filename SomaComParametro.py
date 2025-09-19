def soma(n1, n2):
    try:
        # Garantindo que n1 e n2 sejam inteiros
        n1 = int(n1)
        n2 = int(n2)
        resultado = n1 + n2
        print(f'Soma igual: {resultado}')
    except ValueError:
        print('Valor inválido, digite números inteiros.')

# Chamadas da função com números
soma(10, 5)    # Soma igual: 15
soma('3', '7') # Soma igual: 10
soma('a', 4)   # Valor inválido, digite números inteiros.
