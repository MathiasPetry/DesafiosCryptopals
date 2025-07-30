import base64

hexbase16_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

bytes_reais = bytes.fromhex(hexbase16_string)

base64_bytes = base64.b64encode(bytes_reais)

base64_string = base64_bytes.decode()

print(base64_string)

#Raciocínio em linguagem natural

'''
Primeiro importei a biblioteca "base64" para poder utilizar um método que converte para base 64, que é o que o desafio exige.

Depois, criei uma variável para representar a string hexadecimal em base 16 que o desafio fornece.

Na terceira linha, converti essa string de hexadecimal para o formato de bytes, que é como o computador realmente armazena a informação.

Na linha seguinte, codifiquei esses bytes para base 64, mas o resultado ainda tava no formato de bytes.

Assim, na quinta linha, converti isso para uma string normal, como o desafio pede, e depois fiz uma impressão para visualizar o resultado no terminal.
'''
