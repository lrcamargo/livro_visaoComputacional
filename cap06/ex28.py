#pagina 118
import cv2 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imgOriginal = cv2.imread("/content/moedas.jpg") 
imgTratada = cv2.medianBlur(imgOriginal, 5) 

cv2_imshow(imgOriginal) 
cv2_imshow(imgTratada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
