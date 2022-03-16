#página 147
import cv2 
import numpy as np 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imagemOriginal = cv2.imread("/content/rolamento-ruido-externo.jpg", 0)
#no livro o parâmetro do elemento estruturante era 3,3, mas quando executei o código continuou
#apresentando ruídos ,  então  teste 4,4 e 5,5 e o 4,4 apresentou um resultado melhor.
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4) ) 
imagemProcessada = cv2.morphologyEx( imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante ) 
cv2_imshow(imagemOriginal) 
cv2_imshow(imagemProcessada) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
