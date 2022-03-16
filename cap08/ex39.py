#página 151
import cv2 
import numpy as np 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imagemOriginal = cv2.imread("/content/arroz.jpg", 0)
elementoEstruturante = cv2.getStructuringElement( cv2.MORPH_CROSS, (100, 100) ) 
imagemProcessada = cv2.morphologyEx( imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante ) 
imagemSubtraida = cv2.subtract(imagemOriginal, imagemProcessada) 
#Ajusta o contraste da imagem 
imagemTratada = cv2.add(imagemSubtraida, imagemSubtraida) 

cv2_imshow(imagemOriginal) 
cv2_imshow(imagemProcessada) 
cv2_imshow(imagemSubtraida) 
cv2_imshow(imagemTratada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
