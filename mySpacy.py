import spacy
import string
import matplotlib.pyplot as plt

def test(ss):
    nlp = spacy.load('en')
    doc = nlp(ss)
    print(doc)

    print("")
    print("text", "lemma", "pos", "tag", "label", "dep", "shape", "isAlpha", "isStop")
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    print("")
    print("ent", "label")
    for ent in doc.ents:
        print(ent, ent.label_)

    #spacy.displacy.serve(doc, style='dep')
    #spacy.displacy.serve(doc, style='ent')



