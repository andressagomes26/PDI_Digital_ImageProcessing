<h1 align="center">Morfologia Matemática</h1>
Atividade referente à disciplina Processamento Digital de Imagens do Programa	de	Pós-Graduação em	Engenharia	Elétrica	e	de Computação (UFC) sobre Morfologia Matemática.

## Sobre a atividade
Realize as operações de erosão, dilatação, abertura	e fechamento em todas as imagens binárias (imgs_pb.zip) e também nas	 em	 níveis	de cinza (imgs_cinza.zip). Faça a variação com os	elementos estruturantes: quadrado, linha e circular	 com até três	 dimensões distintas.	Descreva as diferenças apresentas por	operação	e	dimensão	do	elemento	estruturante.

## Dependências
- Jupyter Notebook;

## Linguagens e Bibliotecas
- Python;
- OpenCV;
- Numpy
- Matplotlib;

## Morfologia Matemática
Operações morfológicas são operações que modificam o formato ou a estrutura dos objetos representados	em uma imagem. Para submeter uma imagem a um tratamento com
operações	morfológicas é necessário a existência de um elemento estruturante, responsábel por percorrer toda a imagem a ser tratada, alterando o valor de cada pixel, de acordo com o padrão definido pelo elemento.

### Operações 

- **Erosão:** Caracterizada	pela corrosão das arestas do objeto de interesse, resultando	em uma	imagem "encolhida"	do objeto.	
- **Dilatação:** É o oposto da operação	de erosão. A área	do objeto	de interesse será	dilatada,	ou seja, o objeto	do primeiro	plano ficará maior do que era inicialmente.
- **Abertura:** Caracterizada	pela operação	de erosão seguida da operação de dilatação.	 Assim como a operação de	 erosão, também	 é usada para tratar ruídos.
- **Fechamento:** Usada	para preencher	a	imagem. Consiste na operação de dilatação, seguida	da operação	de erosão.

## O Código

* Para acessar a solução proposta: **[morfologia.ipynb](https://github.com/andressagomes26/PDI_Digital_ImageProcessing/blob/main/2.%20Morfologia%20Matem%C3%A1tica/morfologia.ipynb);**

## Sobre os resultados

### Erosão
- A operação de erosão é caracterizada por reduzir os elementos de uma imagem. É possível observar que quanto maior a dimensão do elemento estruturante, maior será o efeito de erosão da imagem. A seguir, são apresentados alguns exemplos de erosão com os elementos estruturantes (elipse, retangular, linha e cruz) em diferentes dimensões, 5x5, 11x11 e 25x25.

- O elemento estruturante retangular é indicado em casos que o objeto de interesse apresenta formato retangular. No exemplo, a seguir é possível verificar que quanto maior a dimensão do elemento estruturannte maior será a redução da área	do objeto de interesse.

![image](https://user-images.githubusercontent.com/60404990/195903722-e7faec73-555e-4e8a-bb55-f581da5996cc.png)

- Para o elemento estruturante linha é possível observar a degradação da área do objeto de interesse em formato de linha.

![image](https://user-images.githubusercontent.com/60404990/195903831-b9b8c85a-da85-43ce-b513-0ec300922024.png)

- Já para o elemento estruturante	elíptico apresenta melhores	resultados quando o objeto de interesse é em formato circular, como visto a seguir:

![image](https://user-images.githubusercontent.com/60404990/195904226-8889af78-1b23-4527-9b54-81a78f59b228.png)

- Por fim, para as imagens em tons de cinza, é possível verificar que a operação de erosão reduz os níveis de intensidade mais claros da imagem, de acordo com o formato do objeto estruturante e também da sua dimensão.

![image](https://user-images.githubusercontent.com/60404990/195904840-0fae5981-96af-486c-93df-4d319fd8441a.png)

### Dilatação
- Na operação de dilatação a área	do objeto	de interesse será	dilatada. Dessa forma, quanto maior for a dimensão do elemento estruturante, maior será a área do objeto do	primeiro plano. 

- Para um elemento estruturante retangular de tamanho 5x5 é possível observar o aumento da área do objeto no formato retangular. Já para o elemento de tamanho 25x25, a dilatação do objeto de interesse foi quase completa.

![image](https://user-images.githubusercontent.com/60404990/195905549-6a3260c1-f00f-4d27-b9c9-244054d6b3ea.png)

- Também é possível observar o objeto	de interesse	dilatado,	com	área maior que	a	representada na imagem	de	entrada, de acordo com o elemento estruturante elipse (circular). 

![image](https://user-images.githubusercontent.com/60404990/195906112-23c5b643-8986-47c6-b35f-74aa6388c946.png)

- Da mesma forma, é possível observar, nas imagens em tons de cinza, a dilatação do objeto de interesse (expasão dos pixels com intensidades mais claras).

![image](https://user-images.githubusercontent.com/60404990/195906472-13a774fc-8899-4ab7-934b-216e188a623d.png)

### Abertura
- A	operação	de	abertura	é	caracterizada	pela	operação	de	erosão seguida da	operação	 de	 dilatação.	Dessa forma, a erosão corrói as arestas	do	objeto	de	interesse, enquanto, a dilatação recupera as arestas corroídas. Logo, o resultado, da operação de abertura ocorre com a degradação das arestas do objeto, seguido, pela recuperação dessas. Vale destacar, que o formato e dimensão do objeto estruturante é essencial no resultado da operação.

![image](https://user-images.githubusercontent.com/60404990/195907551-02023afb-0662-4db7-a2a2-464ef0a17ae3.png)

![image](https://user-images.githubusercontent.com/60404990/195907611-744593da-7ea0-431d-98d9-d95f20c86d43.png)

- A operação também é válida para as imagens em tons de cinza. A operação de abertura em imagens em tons de cinza, tende	 a	 suprimir	 pequenas	 regiões	 brilhantes da imagem e são utilizadas com intuito	 de	 uniformizar	 a	 iluminação	 dos objetos.

![image](https://user-images.githubusercontent.com/60404990/195907795-c8fa8dba-fdc6-4f0f-ad4d-66c4a87d3d80.png)

### Fechamento
- A	operação	de	fechamento consiste	 na operação	de	dilatação,	seguida	da	operação	de	erosão. Logo,	é	usada	para	preencher	a	imagem, corrigindo pontos no	 objeto	 de	 interesse que foram danificados. Para o elemento estruturante de dimensão 25x25 os	elementos pretos, presentes no interior do objeto de interesse,	são quase completamente preenchidos.

![image](https://user-images.githubusercontent.com/60404990/195909371-fee38325-6103-4c22-8350-c624033dcfe4.png)

![image](https://user-images.githubusercontent.com/60404990/195909400-e8b0a36f-d7b0-49e8-9475-6a96ee60cd38.png)

- Por fim, para as imagens em tons de cinza, a operação de fechamento tende a suprimir pequenas	regiões	escuras, uniformizando a iluminação dos objetos	fotografados.
![image](https://user-images.githubusercontent.com/60404990/195909833-30d5fca2-99dd-49f6-bb55-682945e197fc.png)

- Todos os resultados para todas as operações estão expostos no código.

## Referências
- Estudo baseado no livro "Introdução à Visão Computacional - Uma abordagem prática com Python e OpenCV"

## Autores
- Andressa Gomes Moreira - andressagomes@alu.ufc.br.
