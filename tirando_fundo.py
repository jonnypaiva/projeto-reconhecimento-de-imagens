from rembg import remove
from PIL import Image
import os

folder = "download_imagens"

for i in range(len(os.listdir(folder))):
    input = Image.open(f"download_imagens/{i}.jpg")
    output = remove(input)
    output.save(f"imagens_sem_fundo/{i}.png")