# Slight adaptation of code from
# http://stackoverflow.com/questions/36610179/how-to-get-the-dependency-tree-with-spacy

from nltk import Tree
import spacy

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

def get_nouns_from_instruction(instruction):
	en_nlp = spacy.load('en')
	nouns = []
	doc = en_nlp(instruction)
	for i, sent in enumerate(doc.sents):
		for token in sent:
			if token.pos_ in ["NOUN", "PROPN"]: # PROPN is proper noun.
				nouns.append(token.orth_)
	return nouns
	
if __name__ == "__main__":

	fake_instruction = "WORDS in CAPITALS are NOUNS"
	nouns = get_nouns_from_instruction(fake_instruction)
	print("In fake instruction " + fake_instruction + ", identified these nouns:")
	print(nouns)