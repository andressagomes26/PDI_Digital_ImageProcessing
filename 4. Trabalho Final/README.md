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

### Watershed
Os marcadores, definidos no algoritmo Watershed, conseguiram delimitar os objetos de interesse das imagens. Dessa forma, o algoritmo segmentou, principalmente, os objetos em destaque nas imagem, separando-os do fundo. 

![image](https://user-images.githubusercontent.com/60404990/199865774-f97d269d-cd78-4366-9d8c-08b262f206e8.png)

![image](https://user-images.githubusercontent.com/60404990/199865804-39ebcdfa-469a-4136-8f19-14a2f67f23ab.png)

![image](https://user-images.githubusercontent.com/60404990/199865856-a684abdf-d8a2-4bb4-be29-7bdebf85d3ce.png)

![image](https://user-images.githubusercontent.com/60404990/199865935-0d69f09c-0460-44d8-bae6-b42e64a3232a.png)

![image](https://user-images.githubusercontent.com/60404990/199866008-3d488146-3e40-454f-b308-e22ce5a45ed9.png)

![image](https://user-images.githubusercontent.com/60404990/199866036-e95c6840-7c8b-42c5-a566-272492eb9c1c.png)

### K-means
O número de *clusters* influencia no resultado da segmentação da imagem, dessa forma, para K=3 a segmentação dos objetos quase não é perceptível, uma vez que, as características da imagem vão ser divididas em três grupos apenas. Já para K=9 é possível observar as características dos objetos de forma mais separada. Para as imagens 1 e 2 o algoritmo K-means mostrou-se mais eficiente.

![image](https://user-images.githubusercontent.com/60404990/199865373-409867aa-f8f3-4f32-9c62-bfb24a8628a8.png)

![image](https://user-images.githubusercontent.com/60404990/199864554-64d7a4f7-dbf6-4a0c-b7bb-723db97628a3.png)

![image](https://user-images.githubusercontent.com/60404990/199864588-cfcb9903-c8f8-4424-b1e7-123f55912eb5.png)

![image](https://user-images.githubusercontent.com/60404990/199865056-f54751ba-3fba-4b38-930e-70f19a38eca6.png)

![image](https://user-images.githubusercontent.com/60404990/199864634-8fa71fd1-b382-4b98-a431-396bb6be0666.png)

![image](https://user-images.githubusercontent.com/60404990/199864669-0ba184a8-ba55-4db5-980e-1c22bd580ee6.png)

### Otsu
Por meio da segmentação por limiarização de Otsu foi possível separar os objetos de interesse e o fundo da imagem. Foi possível observar um melhor desempenho do algoritmo, principalmente, nas imagens em que existe uma diferença entre os valores em  primeiro plano ou em segundo plano, como ocorre na imagem do avião.

![image](https://user-images.githubusercontent.com/60404990/199866234-6b369b5a-8b69-4a2c-889a-efd977cf7b5b.png)

![image](https://user-images.githubusercontent.com/60404990/199866257-aacfa8d0-e898-41f1-905b-5e0cb7dfe1b9.png)

![image](https://user-images.githubusercontent.com/60404990/199866288-10ff7179-530a-483f-b03d-e7772cbcf068.png)

![image](https://user-images.githubusercontent.com/60404990/199866327-6b3fa4ad-e37b-4ce4-af13-45c7b2157c97.png)

![image](https://user-images.githubusercontent.com/60404990/199866510-5e2f2be1-65e0-43b7-a0d7-4ae01dce8667.png)

![image](https://user-images.githubusercontent.com/60404990/199866534-5d5d0ac1-0045-41ba-aaf2-a7c0b4b7faec.png)


## Referências
- **Introdução à Visão Computacional - Uma abordagem prática com Python e OpenCV** - Felipe Barelli.
- **Processamento Digital de Imagens** - 3ª edição. Gonzalez, Rafael C.; Woods, Richard E. Editora Pearson.

## Autora
- Andressa Gomes Moreira - andressagomes@alu.ufc.br.

