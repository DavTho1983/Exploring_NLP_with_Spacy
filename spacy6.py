import spacy
nlp = spacy.load('en')
from spacy import displacy

doc_dep = nlp(u'My hovercraft is full of eels.')
displacy.serve(doc_dep, style='dep')

doc_ent = nlp(u'When Sebastian Thrun started working on self-driving cars at Google '
              u'in 2007, few people outside of the company took him seriously.')
displacy.serve(doc_ent, style='ent')
