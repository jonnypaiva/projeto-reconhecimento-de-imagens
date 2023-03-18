import joblib
import cv2
import os

folder_imagens = "images"
num_imagens = len(os.listdir(folder_imagens))
modelo = joblib.load('modelo_de_reconhecimento_monster.joblib')

def extrairCaracteristicas(imagem):
    color_hist = cv2.calcHist([imagem], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    color_hist = cv2.normalize(color_hist, color_hist).flatten()
    return color_hist

def reconhecerEnergetico(imagem):
    caracteristicas = extrairCaracteristicas(imagem)
    predicao = modelo.predict([caracteristicas])
    if predicao:
        return "Monster"
    else:
        return "Outro Energetico"


for i in range(num_imagens):
    imagem = cv2.imread(f'{folder_imagens}/{i}.jpg')
    resultado = reconhecerEnergetico(imagem)

    print(f'A imagem {i}.jpg é {resultado}.')