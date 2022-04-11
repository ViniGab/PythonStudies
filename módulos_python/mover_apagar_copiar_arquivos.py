# Quando vamos selecionar um caminho no Python, para não ter problemas com as
# barras invertidas ou não nós usamos o "r" antes da string com o caminho.

# exemplo

# caminho_windows = r'C:\programas\pasta1'

import os

# esse shutil é o que vai mover e apagar arquivos.

import shutil

caminho_original = r'C:\Users\HP\Documents\rpgmaker'
caminho_novo = r'C:\Users\HP\Documents\rpgmaker2'

# Criando a pasta rpgmaker2 de acordo com o caminho_novo acima.

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existente.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        print(file)  # mostra os arquivos da pasta

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        print(new_file_path)

        # Usando o shutil para mover do caminho antigo para o novo:
        # A pasta antiga ficará vazia, pois os arquivos foram movidos.

        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')