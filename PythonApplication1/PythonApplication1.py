# recebe os valores de entrada
x = int(input('Mac inicio: '))
y = int(input('Mac final: '))

# calcula a quantidade de endereços MAC
z = y - x
i = x
p = int(1)

# abre o arquivo para escrita
with open('saida.txt', 'w') as arquivo:
    
    while i < y :
    
        # Conversão de decimal para hexadecimal
        conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                            4: '4', 5: '5', 6: '6', 7: '7',
                            8: '8', 9: '9', 10: 'A', 11: 'B',
                            12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        def decimalToHexadecimal(decimal):
            if(decimal <= 0):
                return ''
            remainder = decimal % 16
            return decimalToHexadecimal(decimal//16) + conversion_table[remainder]

        decimal_number = int(x)
        
        # escreve a linha no arquivo
        linha = f"{p}) {x} --- {x+10000} ==> 10k {decimalToHexadecimal(decimal_number)} ~~ {decimalToHexadecimal(decimal_number+10000)} Disponivel GROUP(----) - ---- Inicio XX.XX.2023 - Final XX.XX.2023\n"
        arquivo.write(linha)

        x = x + 10001
        p = p + 1
        i = i + 10001

# informa ao usuário que a escrita do arquivo foi concluída
print('A saída do programa foi gravada em "saida.txt".')

