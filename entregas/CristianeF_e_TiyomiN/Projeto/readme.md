
* Nosso desafio:  Contar as primeiras 1500 palavras que mais apresentam de um livro.

* Livro escolhido para teste: alices-adventures-in-wonderland

* Resultado apresentado no arquivo output saida.txt no mesmo diretório do input teste.txt

* Código utilizado: mapper.py, reducer.py

* Como executar o código:
	- O código esta em Python, e para executa-lo deve ter instalado o ptyhon (versão 2.7). 	
	- Carregar o arquivo "teste.txt" no hadoop;
	- Fazer o download da pasta "Projeto" pois contem os arquivos necessários.
	- Dentro do diretório dos arquivos - Executar o comando no terminal do linux: $ cat teste.txt | python mapper.py | sort | python reducer.py > saida.txt
	
	
	
