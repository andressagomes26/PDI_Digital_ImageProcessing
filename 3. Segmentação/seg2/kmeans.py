# Importação das bibliotecas
import numpy as np
import cv2

def kmeans(image):
    pixel_vals = image.reshape((-1,3))
    pixel_vals = np.float32(pixel_vals)
    checkpoint = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.9)
    k = 6
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, checkpoint, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape((image.shape))
    return segmented_image
