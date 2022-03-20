#página 155
import cv2 
import numpy as np 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imagemOriginal = cv2.imread("/content/arroz.jpg", 0)
#no livro o elemento estruturante é 25,25, mas para melhor resultado após  testes deixei 30,30
elementoEstruturante = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (30,30) ) 
imagemProcessada = cv2.morphologyEx( imagemOriginal, cv2.MORPH_TOPHAT, elementoEstruturante ) 
# ajuste de contraste 
imagemTratada = cv2.add(imagemProcessada, imagemProcessada) 
cv2_imshow(imagemOriginal) 
cv2_imshow(imagemProcessada) 
cv2_imshow(imagemTratada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
