import cv2
import numpy as np

# 1. Carregar a imagem
img = cv2.imread('Odair.png', 0)

# 2. Detectar as bordas
bordas = cv2.Canny(img, 150, 300)

# 3. Converter a imagem de bordas (Preto e Branco) para BGR (Colorida)
# Agora ela continua parecendo P&B, mas aceita 3 canais de cor
bordas_coloridas = cv2.cvtColor(bordas, cv2.COLOR_GRAY2BGR)

# 4. Mudar a cor (Exemplo: Verde)
# No OpenCV o padrão é BGR, então (B, G, R)
# Onde houver borda (255), aplicamos a cor [0, 255, 0]
bordas_coloridas[np.where((bordas_coloridas == [255, 255, 255]).all(axis=2))] = [0, 255, 0]

cv2.imshow('Bordas Verdes', bordas_coloridas)
cv2.waitKey(0)
print("Bordas verdes adicionadas a imagem")