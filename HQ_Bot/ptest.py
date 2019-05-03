import nltk.tokenize as nt
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
text="Being more Pythonic is good for health Policeman William Shakespeare."
ss=nt.sent_tokenize(text)
tokenized_sent=[nt.word_tokenize(sent) for sent in ss]
pos_sentences=[nltk.pos_tag(sent) for sent in tokenized_sent]
print(pos_sentences)