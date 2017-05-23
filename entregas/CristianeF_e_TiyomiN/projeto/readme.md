
* Nosso desafio:  Contar as primeiras 1500 palavras que mais apresentam de um livro.

* Livro escolhido: alices-adventures-in-wonderland

* Resultado apresentado no arquivo saida.txt no mesmo diretório do input teste.txt

* Códigos utilizados: mapper.py, reducer.py

* Como executar o código:
	- Fazer o download desta pasta "projeto", por exemplo, em home/cloudera;
	- Descompactar "nltk.7z" na mesma pasta onde foi feito o download;
	- O código está em Python, então o mesmo deve ser/estar instalado (a versão utilizada foi 2.7);
	- Num terminal do linux, deve-se entrar no caminho da pasta deste projeto, via comando cd;
	- E, por fim, executar o comando: $ cat teste.txt | python mapper.py | sort | python reducer.py > saida.txt	
