import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Odair.png')
img = cv2.imread(image_path)

if img is None:
    print("Erro. Imagem não encontrada")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Odair_gray.png', gray)
    print("Imagem 'Odair_gray.png' salva")

    cv2.imshow('Imagem Original', img)
    cv2.imshow('Imagem em Preto e Branco', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()