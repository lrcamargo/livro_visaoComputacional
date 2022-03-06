#pagina 129
import cv2 
#adaptado para rodar no google colab
from google.colab.patches import cv2_imshow

imgOriginal = cv2.imread("/content/lua.jpg", 0) 
imgFiltrada = cv2.Laplacian(imgOriginal, cv2.CV_8U) 
imgRealcada = cv2.subtract(imgOriginal, imgFiltrada) 
cv2_imshow(imgOriginal) 
cv2_imshow(imgFiltrada) 
cv2_imshow(imgRealcada) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
