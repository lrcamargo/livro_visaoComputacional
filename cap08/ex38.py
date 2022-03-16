#página 149
import cv2 
import numpy as np 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imagemOriginal = cv2.imread("/content/rolamento-ruido-interno.jpg", 0) 
#no livro o parâmetro do elemento estruturante era 3,3, mas quando executei o código continuou
#apresentando ruídos então  após  testes o melhor resultado ficou em 7,7
elementoEstruturante = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (7,7) ) 
imagemProcessada = cv2.morphologyEx( imagemOriginal, cv2.MORPH_CLOSE, elementoEstruturante ) 
cv2_imshow(imagemOriginal) 
cv2_imshow(imagemProcessada) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
