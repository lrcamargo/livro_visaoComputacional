import cv2

imagem = cv2.imread("frutas.jpeg")
azul, verde, vermelho = cv2.split(imagem)

cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

cv2.imwrite("frutas-vermelho.jpeg", vermelho)
cv2.imwrite("frutas-verde.jpeg", verde)
cv2.imwrite("frutas-azul.jpeg", azul)

cv2.waitKey(0)
cv2.destroyAllWindows()
