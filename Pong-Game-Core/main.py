import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import sys

#criando a camera
camera = cv2.VideoCapture(0)
#definindo o tamanho da camera
camera.set(3, 1280)
camera.set(4, 720)

#importando todos os elementos
imgDefundo = cv2.imread("elementos/Fundo.png")
imgGameover = cv2.imread("elementos/gameOver.png")
imgbola = cv2.imread("elementos/Bola.png", cv2.IMREAD_UNCHANGED)
imgP1 = cv2.imread("elementos/Player1.png", cv2.IMREAD_UNCHANGED)
imgp2 = cv2.imread("elementos/Player2.png", cv2.IMREAD_UNCHANGED)

# Detector de mão
detector = HandDetector(detectionCon=0.8, maxHands=2)

# variavels
p_bola = [100, 100]
vel_x = 15
vel_y = 15
gameOver = False
pontos = [0, 0]

while True:
    _, img = camera.read()
    #invertendo a imagem
    img = cv2.flip(img, 1)
    img_pequena = img.copy()

    # Colocando os marcadores na mão
    hands, img = detector.findHands(img, flipType=False)  # with draw

    #hands = detector.findHands(img, flipType=False,draw=False)  -- remove os desenhos na mão, quando tiver concluido utilizar pra ficar mais legal

    # Colocando Imagem de fundo sobre a imagem da camera, fazendo "transparencia"
    img = cv2.addWeighted(img, 0.2, imgDefundo, 0.8, 0)

    # função para ver se a mão ta na tela e desenhar nosso querido P1 e o P2
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
    if p_bola[0] < 40 or p_bola[0] > 1200:
        gameOver = True

    if gameOver:
        img = imgGameover
        cv2.putText(img, str(pontos[1] + pontos[0]).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX,
                    2.5, (200, 0, 200), 5)

    
    else:

        #movendo a bola
        if p_bola[1] >= 500 or p_bola[1] <= 10:
            vel_y = -vel_y
       
        p_bola[0] += vel_x
        p_bola[1] += vel_y

        # colocando a bola
        img = cvzone.overlayPNG(img, imgbola, p_bola)

        #texto de pontuação
        cv2.putText(img, str(pontos[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(pontos[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    img[580:700, 20:233] = cv2.resize(img_pequena, (213, 120))

    cv2.imshow("CEET VASCO COUTINHO", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        p_bola = [100, 100]
        vel_x = 15
        vel_y = 15
        gameOver = False
        pontos = [0, 0]
        imgGameover = cv2.imread("elementos/gameOver.png")
    
    #fechar o jogo
    if key == ord('q'):
        exit()