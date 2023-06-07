# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# C:\Users\ac48846\Documents\Dev
import os

# caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
caminho = os.path.join('\\Users', 'ac48846', 'Documents', 'Dev')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
