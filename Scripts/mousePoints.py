import cv2 
import numpy as np 

circles = np.zeros((4,2), np, int)

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
        print(circles)

img = cv2.imread('Photos/cards.jpg')

width, height = 250, 350
pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))


#for x in range (0,4):
#    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0,0,255), cv2.FILLED)

img = cv2.imread('Photos/cards.jpg')
cv2.imshow("Original Image ", img)
cv2.setMouseCallback("Oriqinal Images", mousePoints)

cv2.waitKey(0)