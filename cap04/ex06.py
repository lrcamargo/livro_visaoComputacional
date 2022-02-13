#pagina 59
import cv2

imagem = cv2.imread("frutas.jpeg")

imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
