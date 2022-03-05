#pagina 127
import cv2 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imgOriginal = cv2.imread("/content/estacionamento.jpg", 0) 
imgTratada = cv2.Laplacian(imgOriginal, cv2.CV_8U) 

cv2_imshow(imgOriginal) 
cv2_imshow(imgTratada) 

cv2.waitKey(0)
cv2.destroyAllWindows()
