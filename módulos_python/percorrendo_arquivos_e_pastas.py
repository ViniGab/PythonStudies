import os

caminho_procura = 'C:/Users/HP/Documents/League of Legends/Replays'
termo_procura = 'BR1-2325494661'

# Retorna os arquivos de caminho_procura.

conta = 0


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:  # Para procurar o elemento no arquivo.
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                print(nome_arquivo, ext_arquivo, sep='---')  # Separador de nome e formato
                tamanho = os.path.getsize(caminho_completo)  # Arquivos em bytes
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho formatado: ',formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissão para acessar este arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido.', e)



# Resultado dos prints acima.

"""
Encontrei o arquivo:  BR1-2325494661.rofl
Caminho:  C:/Users/HP/Documents/League of Legends/Replays\BR1-2325494661.rofl
Nome:  BR1-2325494661
Extensão: .rofl
Tamanho: 13954611
"""