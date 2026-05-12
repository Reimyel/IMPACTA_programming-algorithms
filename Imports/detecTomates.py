import cv2
import numpy as np
import os

# 1. Carregar a imagem
image_name = 'tomates.jpg'

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image_name)

if not os.path.exists(image_path):
    print(f"Erro: O arquivo '{image_name}' não foi encontrado.")
else:
    img = cv2.imread(image_path)

    # 2. Converter de BGR para HSV
    # O HSV facilita isolar a cor independente da luz
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 3. Definir a faixa de Vermelho que queremos detectar
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # 4. Criar a máscara (binária: o que for vermelho fica branco, o resto preto)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # 5. Aplicar a máscara na imagem original para ver apenas o vermelho
    result = cv2.bitwise_and(img, img, mask=mask)

    # 6. Mostrar os resultados
    cv2.imshow('Imagem Original', img)
    cv2.imshow('Mascara (Preto e Branco)', mask)
    cv2.imshow('Resultado (Apenas o Vermelho)', result)

    print("Pressione qualquer tecla para fechar.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()