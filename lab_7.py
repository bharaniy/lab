import nltk
nltk.download('punkt')
file = open("/content/drive/My Drive/Lab1/nlp_input.txt","r",encoding='cp1252')
data=file.read()

wordtoken = nltk.word_tokenize(data)
for words in wordtoken:
    print(words)

#%%

# Lemmatization
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
for lem in wordtoken:
    print(lemmatizer.lemmatize(lem))

from nltk.util import ngrams
output = []
trigrams=ngrams(wordtoken,3)
for t in trigrams:
  output.append(t)
print(output)

frequency = nltk.FreqDist(output)
commonwords = frequency.most_common()
print("Trigrams Frequency : \n", commonwords)
top10 = frequency.most_common(10)
print("Top 10 Trigrams : \n", top10)

sentencetokens = nltk.sent_tokenize(data)
result = []
for sentence in sentencetokens:
  for a,b,c in output:
    for((d,e,f),length) in top10:
      if(a,b,c==d,e,f):
        result.append(sentence)
print("concatenated result : ",result)

