import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import sys
import pyautogui

# Criando a câmera
camera = cv2.VideoCapture(0)
# Definindo o tamanho da câmera
camera.set(3, 1280)
camera.set(4, 720)

# Importando todos os elementos
imgDefundo = cv2.imread("elementos/Fundo.png")
imgGameOverPlayer1 = cv2.imread("elementos/gameOver_player1.png")
imgGameOverPlayer2 = cv2.imread("elementos/gameOver_player2.png")
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

            h1, w1, _ = imgp2.shape
            #print(h1)

            y1 = y - 179 // 2

            y1 = np.clip(y1, 5, 380)
            # Desenhando e numerando os pontos dos dedos
            lmList = hand['lmList']
            for i, lm in enumerate(lmList):
                cv2.circle(img, (lm[0], lm[1]), 5, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, str(i), (lm[0], lm[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

            # Verificando se os pontos 8 e 4 se encontram
            if len(lmList) > 8 and len(lmList) > 4:
                x8, y8 = lmList[12][0], lmList[12][1]
                x4, y4 = lmList[4][0], lmList[4][1]
                dist = np.hypot(x8 - x4, y8 - y4)
                if dist < 20:
                    pyautogui.press('r')

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgP1, (59, int(y1)))
                if 59 < p_bola[0] < 59 + w1 and y1 < p_bola[1] < y1 + h1:
                    vel_x = -vel_x
                    p_bola[0] += 30
                    #pontos[0] += 1

            if hand['type'] == "Right":
                img = cvzone.overlayPNG(img, imgp2, (1195, int(y1)))
                if 1195 - 50 < p_bola[0] < 1195 and y1 < p_bola[1] < y1 + h1:
                    vel_x = -vel_x
                    p_bola[0] -= 30
                    #pontos[1] += 1

        if p_bola[0] < 40:
            pontos[1] += 1
        elif p_bola[0] > 1200:
            pontos[0] += 1
        if p_bola[0] < 40 or p_bola[0] > 1200:
            p_bola = [100, 100]
            vel_x = 15
            vel_y = 15
                
        
    if pontos[1] >= 3:
        img = imgGameOverPlayer1

    elif pontos[0] >= 3:
        img = imgGameOverPlayer2
            
    
    else:
        if hands:
            # Movendo a bola
            if p_bola[1] >= 500 or p_bola[1] <= 10:
                vel_y = -vel_y

            p_bola[0] += vel_x
            p_bola[1] += vel_y

            # Colocando a bola
            img = cvzone.overlayPNG(img, imgbola, p_bola)

            # Texto de pontuação
            cv2.putText(img, str(pontos[0]), (300, 660), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
            cv2.putText(img, str(pontos[1]), (915, 660), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255,255), 5)

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
