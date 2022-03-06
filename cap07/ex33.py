#pagina 132
import cv2 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imgOriginal = cv2.imread("/content/radiografia.jpg", 0) 
imgSuavizada = cv2.GaussianBlur(imgOriginal, (13,13), 3) 
imgDetalhes = 3 * cv2.subtract(imgOriginal, imgSuavizada) 
imgRealcada = cv2.add(imgOriginal, imgDetalhes)

cv2_imshow(imgOriginal) 
cv2_imshow(imgSuavizada) 
cv2_imshow(imgDetalhes) 
cv2_imshow(imgRealcada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
