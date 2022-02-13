#pagina 96
import cv2

imagemFichasVermelhas = cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas = cv2.imread("fichas-pretas.jpg")

#adicionado codigo para redimensionar imagens para o mesmo tamanho.
#estava recebendo código de erro ao adicionar as duas imagens pois são de tamanho diferentes
fichasVermelhas = cv2.resize(imagemFichasVermelhas, (620,480))
fichasPretas = cv2.resize(imagemFichasPretas, (620,480))

imagem = cv2.add(fichasVermelhas, fichasPretas)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
