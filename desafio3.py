hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
cipher_bytes = bytes.fromhex(hex_string)

pesos = {
    ' ': 18.00,
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

def score_text(text):
    return sum(pesos.get(chr(c).upper(), 0.0) for c in text)

melhor_score = 0
melhor_texto = ""

for chave in range(256):
    #Reverter o processo da operação do XOR (Reversão da cifra)
    resultado = bytes([b ^ chave for b in cipher_bytes])

    try:
        texto = resultado.decode('ascii')
        score = score_text(resultado)
        if score > melhor_score:
            melhor_score = score
            melhor_texto = texto
    except:
        continue

if __name__ == '__main__':
    print(melhor_texto)


#Raciocínio em linguagem natural

'''
Converti a string hexadecimal fornecida pelo desafio para bytes.

Como o desafio informou que foi utilizada uma cifra XOR com um único caractere,
a ideia foi testar todas as 256 possibilidades de caractere (valores de 0 a 255) como chave.

Para cada uma dessas chaves possíveis, apliquei XOR entre todos os bytes da string
codificada e a chave atual, gerando um resultado que poderia ser a mensagem original.

Tentei decodificar esse resultado como uma string ASCII. Quando não da erro, o modelo desenvolvido analisa
se aquele texto parece uma frase em inglês. Para fazer isso, tive que criar uma função de pontuação
baseada na frequência real das letras na língua inglesa, utilizando dados da Cornell
University e do artigo “Letter frequency” da Wikipedia.

Cada letra recebe um peso fielmente proporcional à sua ocorrência média em textos.
A função soma esses pesos e define um score para cada frase possível.

A lógica foi: quanto maior a soma dos pesos, maior a chance daquela frase
ser um texto legível em inglês. O sistema vai guardando o texto com a melhor pontuação entre todos os testes.

No final, imprimi o texto que teve a maior pontuação, que é o que considero ser
a mensagem original descriptografada.
'''
