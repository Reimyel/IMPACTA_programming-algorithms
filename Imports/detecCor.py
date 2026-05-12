import cv2
import numpy as np
import os

# 1. Carregar a imagem
nome_arquivo = 'odair.png'

if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
else:
    img = cv2.imread(nome_arquivo)

    # 2. Converter de BGR para HSV
    # O HSV facilita isolar a cor independente da luz
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 3. Definir a faixa de Azul que queremos detectar
    # No OpenCV, o Hue (H) vai de 0 a 180
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 4. Criar a máscara (binária: o que for azul fica branco, o resto preto)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 5. Aplicar a máscara na imagem original para ver apenas o azul
    result = cv2.bitwise_and(img, img, mask=mask)

    # 6. Mostrar os resultados
    cv2.imshow('Imagem Original', img)
    cv2.imshow('Mascara (Preto e Branco)', mask)
    cv2.imshow('Resultado (Apenas o Azul)', result)

    print("Pressione qualquer tecla para fechar.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()