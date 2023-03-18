import os

path = "download_imagens"
i = 0

for imagem in os.listdir(path):
    if imagem.endswith('.jpg'):
        old_path = os.path.join(path, imagem)
        new_path = os.path.join(path, f'{i}.jpg')
        os.rename(old_path, new_path)
        i += 1