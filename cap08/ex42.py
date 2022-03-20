#página 158
import cv2 
import numpy as np 

imagemOriginal = cv2.imread("/content/engrenagem-binaria.jpg", 0) 
#no livro a matriz do elemento estruturante é 3,3. Alterado após  testes para um melhor resultado. Outro bom resultado também foi obtido aumentando a iteração da erosão . 
elementoEstruturante = cv2.getStructuringElement( cv2.MORPH_CROSS, (4,4) ) 
imagemProcessada = cv2.erode( imagemOriginal, elementoEstruturante, iterations = 1 ) 

cv2_imshow(imagemOriginal) 
cv2_imshow(imagemProcessada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
