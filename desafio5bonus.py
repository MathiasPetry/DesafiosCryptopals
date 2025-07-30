from itertools import cycle

texto = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

chave = b'ICE'

texto_bytes = texto.encode()

resultado_xor = bytes([b ^ k for b, k in zip(texto_bytes, cycle(chave))])

print(resultado_xor.hex())

#Raciocínio em linguagem natural

'''
Nesse desafio, era preciso aplicar uma cifra XOR usando uma chave que se repete combinando cada byte de "ICE" a cada caractere do texto.

No começo, fiquei um pouco em dúvida sobre como repetir a chave na hora de fazer o XOR com cada caractere do texto.

Pesquisando, encontrei uma função chamada "cycle", que repete automaticamente os caracteres da chave.

Com isso, consegui aplicar o XOR byte por byte entre o texto e a chave repetida, usando zip com list comprehension.

Por fim, converti o resultado para hexadecimal, que era o formato que o desafio pedia.
'''


