def calcular():
    operacao = input('''
    Digite a operação matemática que deseja concluir:
     + para adição
     - para subtração
     * para multiplicação
     / para divisão
    ''')

    numero_1 = int(input('Digite seu primeiro número:'))
    numero_2 = int(input('Digite seu segundo número: '))

    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)
    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)
    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)
    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)
    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

    # Adicione a função again() à função calculate()
    again()


def again():
    calc_again = input('''
                Deseja calcular novamente?
                Digite S para SIM ou N para NÃO.
                ''')

    if calc_again.upper() == 'S': 
        calcular()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()


calcular()