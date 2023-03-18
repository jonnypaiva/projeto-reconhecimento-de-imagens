import os
import cv2
import numpy as np
folder = "no_monster"
num_imagens = len(os.listdir(folder))

imagens = []
for i in range(num_imagens):
    imagem = cv2.imread(f'{folder}/{i}.jpg')
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_redm = cv2.resize(imagem_cinza, (64, 128))
    imagens.append(imagem_redm)

imagens = np.array(imagens)/255

if not os.path.exists("no_monster_cinza"):
    os.makedirs("no_monster_cinza")

for i in range(num_imagens):
    cv2.imwrite(f"no_monster_cinza/{i}.jpg", imagens[i]*255)
#print(imagens)
