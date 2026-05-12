import cv2
import os

# 1. Carregar o classificador de rostos pré-treinado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Carregar a imagem
nome_arquivo = 'Odair.png'

if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado na pasta do script.")
else:
    img = cv2.imread(nome_arquivo)
    
    # 3. Converter para tons de cinza (o algoritmo funciona melhor assim)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 4. Detectar rostos
    # scaleFactor=1.1: compensa rostos que parecem maiores por estarem perto da câmera
    # minNeighbors=5: define quantos retângulos vizinhos devem detectar o rosto para validar
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    print(f"Foram detectados {len(faces)} rostos.")

    # 5. Desenhar retângulos nos rostos encontrados
    for (x, y, w, h) in faces:
        # Desenha o retângulo: (imagem, (x,y inicial), (x+w, y+h final), cor_BGR, espessura)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Coloca um texto acima do retângulo
        cv2.putText(img, 'Odair', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # 6. Exibir o resultado
    cv2.imshow('Deteccao em Imagem Estatica', img)
    
    print("Pressione qualquer tecla na janela da imagem para fechar.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()