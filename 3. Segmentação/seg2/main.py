# Importações
from loadData import load_data
from plotImg import plotImage
from watershed import watershed
from kmeans import kmeans
from otsu import otsu


imgs_seg = load_data('imagens-cor-segmentacao')

for image in imgs_seg:
    image_watershed = watershed(image)
    image_kmeans = kmeans(image)
    image_otsu = otsu(image)

    plotImage(image, image, image_watershed, image_kmeans, image_otsu)
