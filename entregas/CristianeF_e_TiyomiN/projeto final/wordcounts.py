import string as str
import pickle
text = open('teste.txt')
text = text.read()
text = text.lower()
for palavra in str.punctuation:
    text = text.replace(palavra,' ')

   
text = text.split()

dic={}                                       
for palavras in text:              
   if len(palavras)>4:                   
        if palavras not in dic:          
           dic[palavras] = 1            
        else:
           dic[palavras] +=1          
   else:
       del palavras

classificacao=sorted(dic,key=dic.get, reverse=True)
for palavras in classificacao[:1500]:
    print('%s : %d' %(palavras, dic[palavras]))


arq=open('saida.txt','a')
pickle.dump(palavras,arq)
arq.close()


