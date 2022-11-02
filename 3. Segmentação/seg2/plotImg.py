# Importação das bibliotecas

import cv2
from matplotlib import pyplot as plt

def plotImage(image, cresc_reg, image_watershed, image_kmeans, image_otsu):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # image_watershed = cv2.cvtColor(image_watershed, cv2.COLOR_BGR2RGB)
    image_kmeans = cv2.cvtColor(image_kmeans, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 12))

    plt.subplot(1, 5, 1), plt.imshow(image), plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 5, 2), plt.imshow(image_kmeans), plt.title("Crescimento de Regiões")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 5, 3), plt.imshow(image_watershed), plt.title("Watershed")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 5, 4), plt.imshow(image_kmeans), plt.title("K-Means")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 5, 5), plt.imshow(image_otsu, cmap="gray"), plt.title("Otsu")
    plt.xticks([]), plt.yticks([])
    plt.show()