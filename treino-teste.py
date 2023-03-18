import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os
import joblib

folder_monster = "monster_cinza"
folder_no_monster = "no_monster_cinza"
num_imagens_monster = len(os.listdir(folder_monster))
num_imagens_no_monster = len(os.listdir(folder_no_monster))

imagens = []
labels = []

for i in range(num_imagens_monster):
    imagem = cv2.imread(f'{folder_monster}/{i}.jpg')
    imagens.append(imagem)
    labels.append(1)

for i in range(num_imagens_no_monster):
    imagem = cv2.imread(f'{folder_no_monster}/{i}.jpg')
    imagens.append(imagem)
    labels.append(0)

x_treino, x_teste, y_treino, y_teste = train_test_split(imagens, labels, test_size=0.2)

def extrairCaracteristicas(imagem):
    color_hist = cv2.calcHist([imagem], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    color_hist = cv2.normalize(color_hist, color_hist).flatten()
    return color_hist

caract_x_treino = [extrairCaracteristicas(imagem) for imagem in x_treino]
caract_x_teste = [extrairCaracteristicas(imagem) for imagem in x_teste]

x = SVC(kernel = 'linear', C=1000)

x.fit(caract_x_treino, y_treino)
acuracia = x.score(caract_x_teste, y_teste)
print(acuracia)

joblib.dump(x, f'modelo{acuracia}.joblib')
