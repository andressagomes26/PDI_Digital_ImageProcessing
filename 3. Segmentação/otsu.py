# Importação das bibliotecas
import cv2
from skimage import filters

def otsu(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = filters.threshold_otsu(img)
    binarized_img = (img > threshold)*1
    return binarized_img
