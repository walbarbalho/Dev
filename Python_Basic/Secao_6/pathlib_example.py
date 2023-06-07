from pathlib import Path

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

caminho_arquivo.touch()  # Cria o arquivo
# print(arquivo)

# arquivo.write_text('Olá Mundo')

# print(arquivo.read_text())

# arquivo.unlink()  # Apaga o arquivo
# print(Path.home() / 'Desktop')

caminho_arquivo.write_text('')
# para escrecer várias linhas
with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(caminho_arquivo.read_text())
