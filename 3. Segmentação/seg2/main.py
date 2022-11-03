# Importações
from loadData import load_data
from plotImg import plotImage
from watershed import watershed
from kmeans import kmeans
from otsu import otsu
from cresc_reg import cresc_reg


imgs_data_segmentacao = load_data('imagens-cor-segmentacao')

for img in imgs_data_segmentacao:
    plotImage(img, cresc_reg(img), watershed(img), kmeans(img), otsu(img))
