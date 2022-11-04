# Importações
import cv2
from loadData import load_data
from plotImg import plotImages, plotImageKMeans
from watershed import watershed
from kmeans import kmeans
from otsu import otsu


imgs_data_segmentacao = load_data('imagens-cor-segmentacao')

for img in imgs_data_segmentacao:
    plotImages(img, watershed(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), "watershed")
    plotImageKMeans(img, kmeans(img), kmeans(img, 6), kmeans(img, 9))
    plotImages(img, otsu(img), "Otsu")
