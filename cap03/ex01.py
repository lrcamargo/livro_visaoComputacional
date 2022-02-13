#página 48
import cv2

imagem = cv2.imread("teste.jpg")
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
