import spacy
nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion, where will it all end??')

#tokenisation splits into words and punctuation
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

# Text: The original word text.
# Lemma: The base form of the word.
# POS: The simple part-of-speech tag.
# Tag: The detailed part-of-speech tag.
# Dep: Syntactic dependency, i.e. the relation between tokens.
# Shape: The word shape – capitalisation, punctuation, digits.
# is alpha: Is the token an alpha character?
# is stop: Is the token part of a stop list, i.e. the most common words of the language?

#A named entity is a real-world object that's assigned a name
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Text: The original entity text.
# Start: Index of start of entity in the Doc.
# End: Index of end of entity in the Doc.
# Label: Entity label, i.e. type.

#Word vectors and similarity
