import spacy
nlp = spacy.load('en')
tokens = nlp(u'dog cat banana sasquatch')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)
