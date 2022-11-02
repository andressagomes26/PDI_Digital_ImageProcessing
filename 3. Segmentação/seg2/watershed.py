# Importação das bibliotecas
import numpy as np
import cv2
from skimage import filters

def watershed(img):
    # Binarização Otsu (negativo)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold = filters.threshold_otsu(gray)
    binarized_img = (gray < threshold) * 1
    binarized_img = binarized_img.astype('uint8')

    # Operação de abertura
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opening_ellipse = cv2.morphologyEx(binarized_img, cv2.MORPH_OPEN, kernel_ellipse, iterations=2)

    # Operação de Dilatação
    dilate_ellipse = cv2.dilate(opening_ellipse, kernel_ellipse, iterations=3)

    # Determinando a área do primeiro plano
    dist_transform = cv2.distanceTransform(opening_ellipse, cv2.DIST_L2, 5)

    # Binarização Otsu
    threshold1 = filters.threshold_otsu(dist_transform)
    binarized_img1 = (dist_transform > threshold1) * 1

    # Subtração das imagens
    binarized_img1 = np.uint8(binarized_img1)
    img_subtract = cv2.subtract(dilate_ellipse, binarized_img1)

    # Cria um marcador para rotular as regiões dos objetos e fundo.
    ret, markers = cv2.connectedComponents(binarized_img1)

    # Define o rótulo do fundo como 1
    markers = markers + 1

    # Define o rótulo das regiões desconhecidas como 0
    markers[img_subtract == 255] = 0
    markers = cv2.watershed(img, markers)

    # Aplica o watershed
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img