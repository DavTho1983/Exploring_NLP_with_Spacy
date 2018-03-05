import spacy
nlp = spacy.load('en')
doc = nlp(u'Hello, world. Here are two sentences.')

nlp_de = spacy.load('de')
doc_de = nlp_de(u'Ich bin ein Berliner.')

doc = nlp(u"Peach emoji is where it has always been. Peach is the superior "
          u"emoji. It's outranking eggplant 🍑 ")

assert doc[0].text == u'Peach'
assert doc[1].text == u'emoji'
assert doc[-1].text == u'🍑'
assert doc[17:19].text == u'outranking eggplant'
assert list(doc.noun_chunks)[0].text == u'Peach emoji'

sentences = list(doc.sents)
assert len(sentences) == 3
assert sentences[1].text == u'Peach is the superior emoji.'
