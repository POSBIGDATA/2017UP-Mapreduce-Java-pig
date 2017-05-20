#!/usr/bin/python3
import sys
from nltk.corpus import wordnet as wn
from nltk import pos_tag
import nltk

#as bases do NLTK necessárias para a execução deste projeto são: 'punkt' e 'averaged_perceptron_tagger'. Elas poderão ser instaladas a partir do código Python da seguinte forma:

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

(lastKey, sum, listagem, listagemNova)=(None, 0, {}, {})

for line in sys.stdin:
	(key, value) = line.strip().split("\t")
	
	#nova palavra
	if lastKey and lastKey != key:
		listagem[lastKey] = sum
		(lastKey, sum) = (key, int(value))
	
	#primeira palavra ou a mesma palavra
	else:
		(lastKey, sum) = (key, sum + int(value))

if lastKey:
	listagem[lastKey] = sum

for palavra, contagem in listagem.items():
	words = nltk.word_tokenize(palavra)
	classificacao = pos_tag(words)
	for word in classificacao:
		#removendo as preposicoes do texto
		if (word[1] != 'IN'):
			listagemNova[word[0]] = contagem

for key, value in sorted(listagemNova.items(), key=lambda listagemNova: listagemNova[1], reverse=True):
	print (key + '\t' + str(value))
