#pagina 102
import cv2 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imagemFichasVermelhas = cv2.imread("/content/fichas-vermelhas.bmp") 
imagemFichasPretas = cv2.imread("/content/fichas-pretas.jpg") 

#adicionado codigo para redimensionar imagens para o mesmo tamanho.
#estava recebendo código de erro ao adicionar as duas imagens pois são de tamanho diferentes
pretas=cv2.resize(imagemFichasPretas,(520,480))
vermelhas=cv2.resize(imagemFichasVermelhas,(520,480))

imagem = cv2.addWeighted( pretas, 0.2, vermelhas, 1.0, 0 ) 
#alterado para Google colab
cv2_imshow(imagem) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
