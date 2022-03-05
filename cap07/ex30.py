#pagina 125
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

import cv2 
imagem = cv2.imread("/content/estacionamento.jpg", 0) 
sobelx = cv2.Sobel(imagem, cv2.CV_8U, 1, 0, ksize = 3) 
sobely = cv2.Sobel(imagem, cv2.CV_8U, 0, 1, ksize = 3) 

cv2_imshow(imagem) 
cv2_imshow(sobelx) 
cv2_imshow(sobely) 

cv2.waitKey(0)
cv2.destroyAllWindows()
