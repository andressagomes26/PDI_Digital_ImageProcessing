<h1 align="center">Segmentação de Imagens</h1>
Atividade referente à disciplina Processamento Digital de Imagens do Programa	de	Pós-Graduação em	Engenharia	Elétrica	e	de Computação (UFC) sobre Morfologia Matemática.

## Sobre a atividade
Implementar	os	algoritmos	de	segmentação	que	seguem,	utilizando	as imagens	de	teste e avaliando	o	desempenho do	algoritmo	em cada	imagem.	

a.	Crescimento	de	Regiões;

b.	Watershed;

c.	K-Means.

d.	Otsu

## Dependências
- PyCharm;

## Linguagens e Bibliotecas
- Python;
- OpenCV;
- Numpy;
- Matplotlib;
- Skimage .

## Segmentação de imagens
A	 segmentação de	 objetos em	 imagens consiste em separar a área de interesse em	uma	nova imagem, excluindo o segundo plano da região.
O	 objeto	 de interesse é	considerado o primeiro plano da imagem. Dessa forma, a segmentação é o princípio para a extração de características	de um objeto.

## Algoritmos	de	segmentação 

### Crescimento	de Regiões 
O crescimento de região é um procedimento que agrupa os pixels em regiões maiores com base em critérios predefinidos para o crescimento. A abordagem básica é começar 
com um conjunto de pontos “semente” e, a partir deles, fazer as regiões crescerem anexando a cada semente aos pixels vizinhos que têm propriedades predefinidas semelhantes às das sementes.

### Watershed
O algoritmo é baseado no conceito de bacias hidrográficas, na qual, a visualização de uma imagem em três dimensões. Desse modo, uma das principais aplicações da segmentação por watershed é a extração de objetos quase uniformes do fundo. O algoritmo utiliza o conceito de marcadores, para controlar a supersegmentação, ou seja, o excesso de regiões segmentadas. Logo, são definidos marcadores internos associados aos objetos de interesse e indicadores externos associados ao fundo.

### K-Means
O K-Means é um algoritmo de clusterização (ou agrupamento), responsável por dividir os dados em *clusters* de acordo com suas características. É possível definir K números de *clusters*, cada um com um centroide definido aleatoriamente. Dessa forma, será calculado, para cada ponto, o centroide de menor distância.

### Otsu

A segmentação por limiarização de Otsu consiste em separar os objetos de interesse e o fundo da imagem. Nesse algoritmo, é definido um limiar (threshold), que servirá como base para realizar a binarização dos pixels. Logo, a limiarização de Otsu funciona iterando sobre todos os valores de limiar possíveis e calculando uma medida de dispersão para os pontos de amostra em ambos os lados do limiar, ou seja, em primeiro plano ou em segundo plano.


## O Código

* Para acessar as soluções proposta: **[Segmentação]();**

## Resultados
- Imagem 1

![image](https://user-images.githubusercontent.com/60404990/199855803-306b7e97-d462-41d5-819c-23138daa9134.png)

- Imagem 2

![image](https://user-images.githubusercontent.com/60404990/199855844-f9252c88-dc55-46f6-a69b-352eff78ac2b.png)

- Imagem 3
![image](https://user-images.githubusercontent.com/60404990/199855975-5f1d2df8-e9ea-4960-b397-67fe836bdd67.png)

- Imagem 4
![image](https://user-images.githubusercontent.com/60404990/199856006-c930bb77-769c-42ea-94a9-a10b31dcb720.png)


- Imagem 5
![image](https://user-images.githubusercontent.com/60404990/199856036-026eeec2-b3b1-469c-b093-3832ec3a268b.png)


- Imagem 6
![image](https://user-images.githubusercontent.com/60404990/199856056-dfc7b45e-4243-41c1-9522-ad2d3d75883e.png)

## Referências
- **Introdução à Visão Computacional - Uma abordagem prática com Python e OpenCV** - Felipe Barelli.
- **Processamento Digital de Imagens** - 3ª edição. Gonzalez, Rafael C.; Woods, Richard E. Editora Pearson.

## Autora
- Andressa Gomes Moreira - andressagomes@alu.ufc.br.

