import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import sys

# Criando a câmera
camera = cv2.VideoCapture(0)
# Definindo o tamanho da câmera
camera.set(3, 1280)
camera.set(4, 720)

# Importando todos os elementos
imgDefundo = cv2.imread("elementos/Fundo.png")
imgGameover = cv2.imread("elementos/gameOver.png")
imgbola = cv2.imread("elementos/Bola.png", cv2.IMREAD_UNCHANGED)
imgP1 = cv2.imread("elementos/Player1.png", cv2.IMREAD_UNCHANGED)
imgp2 = cv2.imread("elementos/Player2.png", cv2.IMREAD_UNCHANGED)

# Detector de mão
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Variáveis
p_bola = [100, 100]
vel_x = 15
vel_y = 15
gameOver = False
pontos = [0, 0]

# Definindo o tamanho da moldura
moldura_width = 213
moldura_height = 120
moldura_x = 30  # Ajuste para mover a moldura para a direita
moldura_y = 570  # Ajuste para mover a moldura para cima

while True:
    _, img = camera.read()
    # Invertendo a imagem
    img = cv2.flip(img, 1)
    img_pequena = img.copy()

    # Colocando os marcadores na mão
    hands, img = detector.findHands(img, flipType=False)  # with draw

    # Colocando Imagem de fundo sobre a imagem da câmera, fazendo "transparência"
    img = cv2.addWeighted(img, 0.2, imgDefundo, 0.8, 0)

    # Função para ver se a mão está na tela e desenhar os personagens P1 e P2
    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']

            h1, w1, _ = imgP1.shape

            y1 = y - h1 // 2

            y1 = np.clip(y1, 20, 415)

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgP1, (59, y1))
                if 59 < p_bola[0] < 59 + w1 and y1 < p_bola[1] < y1 + h1:
                    vel_x = -vel_x
                    p_bola[0] += 30
                    pontos[0] += 1

            if hand['type'] == "Right":
                img = cvzone.overlayPNG(img, imgp2, (1195, y1))
                if 1195 - 50 < p_bola[0] < 1195 and y1 < p_bola[1] < y1 + h1:
                    vel_x = -vel_x
                    p_bola[0] -= 30
                    pontos[1] += 1

    # Game Over
    if p_bola[0] < 40:
        img = imgGameover
        cv2.putText(img, str("Player 2 venceu").zfill(2), (700, 500), cv2.FONT_HERSHEY_COMPLEX,
                    1, (200, 0, 200), 3)

    elif p_bola[0] > 1200:
        img = imgGameover
        cv2.putText(img, str("Player 1 venceu").zfill(2), (700, 500), cv2.FONT_HERSHEY_COMPLEX,
                    1, (200, 0, 200), 3)
    
    else:
        # Movendo a bola
        if p_bola[1] >= 500 or p_bola[1] <= 10:
            vel_y = -vel_y

        p_bola[0] += vel_x
        p_bola[1] += vel_y

        # Colocando a bola
        img = cvzone.overlayPNG(img, imgbola, p_bola)

        # Texto de pontuação
        cv2.putText(img, str(pontos[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(pontos[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    # Redimensionando e posicionando a imagem pequena da câmera na moldura
    img_pequena = cv2.resize(img_pequena, (moldura_width, moldura_height))
    img[moldura_y:moldura_y + moldura_height, moldura_x:moldura_x + moldura_width] = img_pequena

    cv2.imshow("CEET VASCO COUTINHO", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        p_bola = [100, 100]
        vel_x = 15
        vel_y = 15
        gameOver = False
        pontos = [0, 0]
        imgGameover = cv2.imread("elementos/gameOver.png")

    # Fechar o jogo
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
sys.exit()
