<h1 align="center">Realce no Domínio Espacial</h1>
Atividade referente à disciplina Processamento Digital de Imagens do Programa	de	Pós-Graduação em	Engenharia	Elétrica	e	de Computação (UFC) sobre Realce no Domínio Espacial.

## Sobre a atividade
Construa sete	filtros	passa-baixa	e	discuta	sobre	as	mudanças de	aplicações,	dimensões	dos	filtros	e	efeitos	em	tipos	de	ruídos para as imagens de teste (imagens-Sal-e-Pimenta.zip)	com	ruído	sal	e	pimenta	aplicado	nas	mesmas.	Realize	a	 filtragem	nessas	imagens	e	veja qual	 técnica	apresentou	 o	melhor	 desempenho	e	 qual	a	melhor definição de	janela para	 alcançar	o	filtro	mais	eficiente.

**(a)** Filtro da Média: 3x3 (N=9),	5x5	(N=25) e 7x7 (N=49)

![image](https://user-images.githubusercontent.com/60404990/195727581-a57a7361-8f72-496e-92c4-17e26cc58153.png)

**(b)** Filtro da Média: 3x3

![image](https://user-images.githubusercontent.com/60404990/195727700-ab7cb82c-6175-4b3d-9779-d1a75ccd5ea8.png)

**(c)** Filtro da	Mediana: 3x3, 5x5,	7x7

## Dependências
- Jupyter Notebook;

## Linguagens e Bibliotecas
- Python;
- OpenCV;
- Numpy
- Matplotlib;

## Suavização de imagens
A suavização da imagens ou "blur" é o processo de tratamento de ruído em imagens. O	filtro de	média é um	filtro	linear,	 passa-baixa,	utilizado	para suavização	de	imagens.	O filtro é responsável por substituir	cada	pixel da	imagem	 pelo	 valor	médio	 de	 sua	 vizinhança. Quanto	maior	o kernel (matriz ou máscara),	maior	 será	o	número de	pixels	vizinhos	considerados,	logo,	mais	intenso	será	o	efeito	de suavização. Já o filtro da mediana é não	linear e	apresenta	bons	resultados no tratamento	 de	 ruído do	 tipo	 "sal	e pimenta". O filtro atua	 alterando	 o	 valor	 de	 cada pixel-alvo	pela	mediana	estatística	dos	valores	dos	pixels vizinhos.

## O Código

* Para acessar a solução proposta: **[filtragem.ipynb](https://github.com/andressagomes26/PDI_Digital_ImageProcessing/blob/main/1.%20Realce%20no%20Dom%C3%ADnio%20Espacial/filtragem.ipynb);**

## Sobre os resultados

### (a) Filtro da Média: 3x3 (N=9),	5x5	(N=25) e 7x7 (N=49)
- Para aplicar o filtro da média nas imagens foram criadas três máscaras (kernel) com dimensões iguais a 3x3, 5x5	e 7x7. A constante multiplicadora (N) é definida como a divisão pela soma dos valores dos de seus coeficientes. As constantes foram definidas, respectivamente, como (N=9),	(N=25) e (N=49).

- O resultado, exibido na figura abaixo, apresenta a aplicação do filtro da média para a primeira imagem com ruído do tipo "sal	e pimenta". Vale ressaltar, que quanto maior a máscara mais	intenso	será o efeito	de suavização. Logo, para a máscara do filtro de tamanhos 7x7 o efeito de suavização da imagem foi maior. Entretanto, o filtro não foi suficiente para remover o ruído da imagem.

![image](https://user-images.githubusercontent.com/60404990/195731113-50c69d42-4be1-472f-8e26-a759ffc502dd.png)

<p align="center">Imagem original (lenna) seguida pelas imagens com a aplicação do filtro da média 3x3 (N=9), 5x5 (N=25) e 7x7 (N=49)</p>

- Para a segunda imagem é possível observar o efeito de "borramento" à medida que o tamanho da máscara aumenta.
 
![image](https://user-images.githubusercontent.com/60404990/195731845-3493b8c0-6e3d-4aee-b5df-14b740e641a1.png)

<p align="center">Imagem original (cameraman) seguida pelas imagens com a aplicação do filtro da média 3x3 (N=9), 5x5 (N=25) e 7x7 (N=49)</p>

### (b) Filtro da Média: 3x3 (N=16)

- Para a segunda tarefa foi criada uma máscara de filtro para aplicar o filtro da média com dimensões iguais a 3x3. A constante multiplicadora (N=16) é dada por 1 dividido pela soma dos valores dos coeficientes do kernel. O resultado foi bastante semelhante ao apresentado na atividade anterior para o kernel 3x3.

imagem

### (b) Filtro da Mediana: 3x3, 5x5, 7x7
- Por fim, foi aplicado o filtro da mediana, conhecido por apresentar	bons resultados no tratamento	de ruído do	tipo "sal	e pimenta". As máscaras definidas possuem dimensões iguais a 3x3, 5x5, 7x7. Nessa processo, o filtro atua alterando	 o valor de	cada pixel-alvo	pela mediana dos valores dos pixels vizinhos.
- É possível ressaltar que o desempenho para tratar o ruído "sal	e pimenta" nas imagens foi superior ao desempenho obtido pelo filtro da média

![image](https://user-images.githubusercontent.com/60404990/195733056-e2e26f1d-ed2d-4d76-91e7-3f58ddbcd132.png)

<p align="center">Imagem original (lenna) seguida pelas imagens com a aplicação do filtro da mediana 3x3, 5x5, 7x7</p>

![image](https://user-images.githubusercontent.com/60404990/195733123-954773e7-a7b5-4f59-8db6-c6f654000ad6.png)

<p align="center">Imagem original (cameraman) seguida pelas imagens com a aplicação do filtro da mediana 3x3, 5x5, 7x7</p>

![image](https://user-images.githubusercontent.com/60404990/195733156-315b57dc-24a5-4603-be05-00439f3a0654.png)

<p align="center">Imagem original (SaltAndPepperNoise) seguida pelas imagens com a aplicação do filtro da mediana 3x3, 5x5, 7x7</p>

## Referências
- Estudo baseado no livro "Introdução à Visão Computacional - Uma abordagem prática com Python e OpenCV"

## Autores
- Andressa Gomes Moreira - andressagomes@alu.ufc.br.

## Status do Projeto
- O projeto encontra-se finalizado, pois o objetivo foi alcançado, porém, está sujeito a devidas mudanças e melhorias.
