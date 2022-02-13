#pagina 58
import cv2

imagem = cv2.imread("frutas.jpeg")
azul, verde, vermelho = cv2.split(imagem)

imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
