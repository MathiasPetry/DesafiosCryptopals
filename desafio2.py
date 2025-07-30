str_hex1 = '1c0111001f010100061a024b53535009181c'
str_hex2 = '686974207468652062756c6c277320657965'

bytes1 = bytes.fromhex(str_hex1)
bytes2 = bytes.fromhex(str_hex2)

resultado_xor = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])

print(resultado_xor.hex())

#Raciocínio em linguagem natural

'''
Armazenei as duas strings hexadecimais que o desafio fornece e converti para bytes para conseguir fazer a operação.

Usei uma list comprehension com zip para percorrer os dois ao mesmo tempo e aplicar o XOR entre os pares de bytes.

O resultado foi um nova cifra com os valores já processados.

Converti esse resultado para hexadecimal e então imprimi o resultado para conferir no terminal.
'''
