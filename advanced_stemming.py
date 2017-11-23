# Stemming
from nltk.stem.snowball import SpanishStemmer
ss = SpanishStemmer()
print(ss.stem('amigos'))

# Tokenize
import nltk
print(nltk.word_tokenize("I like long sentences. Let's write software.", "english"))

# Remove accents
import unicodedata
nfkd = unicodedata.normalize('NFKD', 'áéíóúçñ')
print([c for c in nfkd if not unicodedata.combining(c)])

# Lowercase
'I HATE CAPS LOCK'.lower()

# Find words with stemming
tokens = nltk.word_tokenize('Los adolescentes van con malas compañías'.lower(), 'spanish')
stems = [ss.stem(token) for token in tokens]
print(ss.stem('adolescente') in stems)
print(ss.stem('compañero') in stems)
print(ss.stem('compañía') in stems)
