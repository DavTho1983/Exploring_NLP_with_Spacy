#Pipelines

# Name: ID of the pipeline component.
# Component: spaCy's implementation of the component.
# Creates: Objects, attributes and properties modified and set by the component.

# Name	Component	Creates	Description
# tokenizer	Tokenizer 	Doc	Segment text into tokens.
# tagger	Tagger 	Doc[i].tag	Assign part-of-speech tags.
# parser	DependencyParser 	Doc[i].head, Doc[i].dep, Doc.sents, Doc.noun_chunks	Assign dependency labels.
# ner	EntityRecognizer 	Doc.ents, Doc[i].ent_iob, Doc[i].ent_type	Detect and label named entities.
# textcat	TextCategorizer 	Doc.cats	Assign document labels.
# ...	custom components	Doc._.xxx, Token._.xxx, Span._.xxx	Assign custom attributes, methods or properties.

#Vocab, hashes and lexemes

# Token: A word, punctuation mark etc. in context, including its attributes, tags and dependencies.
# Lexeme: A "word type" with no context. Includes the word shape and flags, e.g. if it's lowercase, a digit or punctuation.
# Doc: A processed container of tokens in context.
# Vocab: The collection of lexemes.
# StringStore: The dictionary mapping hash values to strings, for example 3197928453018144401 → "coffee".

import spacy
from spacy.tokens import Doc
from spacy.vocab import Vocab
nlp = spacy.load('en')

doc = nlp(u'I love coffee')
assert doc.vocab.strings[u'coffee'] == 3197928453018144401
assert doc.vocab.strings[3197928453018144401] == u'coffee'

for word in doc:
    lexeme = doc.vocab[word.text]
    print(lexeme.text, lexeme.orth, lexeme.shape_, lexeme.prefix_, lexeme.suffix_, lexeme.is_alpha, lexeme.is_digit, lexeme.is_title, lexeme.lang_)

# Text: The original text of the lexeme.
# Orth: The hash value of the lexeme.
# Shape: The abstract word shape of the lexeme.
# Prefix: By default, the first letter of the word string.
# Suffix: By default, the last three letters of the word string.
# is alpha: Does the lexeme consist of alphabetic characters?
# is digit: Does the lexeme consist of digits?

empty_doc = Doc(Vocab()) #new Doc with empty vocab
# doc.vocab.strings[3197928453018144401] will raise an error :(

empty_doc.vocab.strings.add(u'coffee') # add "coffee" and generate hash
assert doc.vocab.strings[3197928453018144401] == u'coffee' # 👍

new_doc = Doc(doc.vocab) # create new doc with first doc's vocab
assert doc.vocab.strings[3197928453018144401] == u'coffee' # 👍
