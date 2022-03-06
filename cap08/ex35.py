#página 143
import cv2 
import numpy as np 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imagemOriginal = cv2.imread("/content/rolamento.jpg", 0) 
elementoEstruturante = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (5,5) ) 
imagemProcessada = cv2.erode( imagemOriginal, elementoEstruturante, iterations = 2 ) 

cv2_imshow(imagemOriginal) 
cv2_imshow(imagemProcessada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
