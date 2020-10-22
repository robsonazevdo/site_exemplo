def hash(palavra, tamanho_tabela):
    soma = 0
    for pos in range(len(palavra)):
        soma = soma + ord(palavra[pos])
        
    return soma % tamanho_tabela

print(hash('impacta', 23))
print(hash('faculdade',23))
print(hash('atividade', 23))