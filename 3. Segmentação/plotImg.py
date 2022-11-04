# Importação das bibliotecas

import cv2
from matplotlib import pyplot as plt

def plotImageKMeans(image, image_kmeans3, image_kmeans6, image_kmeans9):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_kmeans3 = cv2.cvtColor(image_kmeans3, cv2.COLOR_BGR2RGB)
    image_kmeans6 = cv2.cvtColor(image_kmeans6, cv2.COLOR_BGR2RGB)
    image_kmeans9 = cv2.cvtColor(image_kmeans9, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 12))

    plt.subplot(1, 4, 1), plt.imshow(image), plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 4, 2), plt.imshow(image_kmeans3), plt.title("K-Means (K=3)")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 4, 3), plt.imshow(image_kmeans6), plt.title("K-Means (K=6)")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 4, 4), plt.imshow(image_kmeans9), plt.title("K-Means (K=9)")
    plt.xticks([]), plt.yticks([])

    plt.show()

def plotImages(image, image_seg, title):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 12))

    plt.subplot(1, 2, 1), plt.imshow(image), plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(image_seg, cmap="gray"), plt.title(title)
    plt.xticks([]), plt.yticks([])

    plt.show()