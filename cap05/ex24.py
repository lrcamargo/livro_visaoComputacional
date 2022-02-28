#pagina 100
import cv2
#adaptado  para rodar no google colab
from google.colab.patches import cv2_imshow

imagemFichaPosicao1 = cv2.imread("/content/ficha-posicao-1.bmp") 
imagemFichaPosicao2 = cv2.imread("/content/ficha-posicao-2.bmp") 

#adicionado codigo para redimensionar imagens para o mesmo tamanho.
#estava recebendo código de erro ao adicionar as duas imagens pois são de tamanho diferentes
ficha1= cv2.resize( imagemFichaPosicao1, (520,480))
ficha2=cv2.resize(imagemFichaPosicao2,(520,480))

imagem = cv2.subtract(ficha1, ficha2)
#alterado para Google colab
cv2_imshow(imagem) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
