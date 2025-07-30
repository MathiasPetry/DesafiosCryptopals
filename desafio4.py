from desafio3 import score_text

def decifrar_linha_xor_unico(hex_string):
    cipher_bytes = bytes.fromhex(hex_string)
    melhor_score = 0
    melhor_texto = ""

    for chave in range(256):
        resultado = bytes([b ^ chave for b in cipher_bytes])
        try:
            texto = resultado.decode('ascii')
        except UnicodeDecodeError:
            continue

        texto_em_bytes = texto.encode('latin1')
        score = score_text(texto_em_bytes)

        if score > melhor_score:
            melhor_score = score
            melhor_texto = texto

    return melhor_score, melhor_texto

melhor_score_global = 0
mensagem_mais_provavel = ''

with open('challenge4.txt', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        linha = linha.strip()
        print(f"[{i}] Testando linha: {linha[:30]}...")

        score, texto = decifrar_linha_xor_unico(linha)

        print(f"[{i}] Score: {score} | Texto: {texto[:50]!r}")

        if score > melhor_score_global:
            melhor_score_global = score
            mensagem_mais_provavel = texto

print('\n Mensagem decifrada: ')
print(mensagem_mais_provavel)

# Raciocínio em linguagem natural

'''
O desafio propõe identificar, entre várias strings hexadecimais,
qual foi criptografada com XOR de um único caractere e contém uma frase em inglês plausível.

Inicialmente, utilizei a mesma lógica aplicada no Desafio 3:
testar todas as 256 chaves possíveis e medir a semelhança do resultado com o inglês
usando a função score_text, que importei do desafio 3, baseada na frequência das letras.

No entanto, como agora temos várias linhas no arquivo, foi necessário
adaptar o código para iterar sobre cada linha individualmente.

Para isso, abri o arquivo e percorri cada linha usando um loop.
A cada linha, converti o texto hexadecimal para bytes.

Em seguida, apliquei XOR com todas as 256 chaves possíveis,
tentando decodificar o resultado com ASCII.
Se a decodificação fosse válida, apliquei a função score_text.

Nesse ponto, percebi que a função score_text esperava bytes e não strings,
e por isso o código não funcionava corretamente.
Pesquisando, encontrei que era possível reverter a string para bytes
usando a codificação 'latin1', que mantém os valores originais dos caracteres.

Com isso, consegui pontuar corretamente os textos gerados.
A cada linha, guardei o melhor texto e seu score.
Ao final, comparei os melhores resultados de todas as linhas
e selecionei aquele com o score mais alto como a mensagem decifrada.
'''

