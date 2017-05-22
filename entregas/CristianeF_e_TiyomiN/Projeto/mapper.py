#!/usr/bin/env python
import sys
import re
import string
import nltk.tokenize
import nltk
nltk.download('stopwords')
import zipimport
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
from nltk.corpus import stopwords
nltk.data.path+=["."]
stops = set(stopwords.words('english'))
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = re.sub(r"<[a-zA-Z\/][^>]*>", "",line)	
    line = line.strip()
    #split each line on whitspace
    data = line.split()
    for word in data:
        #remove punctuation
        word = word.strip(string.punctuation)
        #remove numbers
        if re.search("\d+",word): continue 
        #remove stopwords
        if word.lower() in stops: continue
        #stem<
        if len(word) < 2: continue
        print '%s\t%s' % (word, 1)
