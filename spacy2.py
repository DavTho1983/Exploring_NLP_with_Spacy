import spacy
nlp = spacy.load('en')

tokens = nlp(u'dog cat banana')

# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.similarity(token2))

[print(token1.similarity(token2)) for token1 in tokens for token2 in tokens]
