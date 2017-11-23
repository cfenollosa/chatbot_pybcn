# Create chain
from pymarkovchain import MarkovChain
mc_corpus = MarkovChain('/tmp/mc_corpus')

# Generate with a corpus
import nltk
mc_corpus.generateDatabase(' '.join(word.lower().replace('_', ' ')
                                    for word in nltk.corpus.cess_esp.words()
                                    if word[0].isalpha()))
mc_corpus.dumpdb()

# Have fun!
print(mc_corpus.generateStringWithSeed('edificio'))
