from nltk.corpus import wordnet as wn
from itertools import product

wordx, wordy = "cat","dog"
sem1, sem2 = wn.synsets(wordx), wn.synsets(wordy)

maxscore = 0
for i,j in list(product(*[sem1,sem2])):
  score = i.wup_similarity(j) # Wu-Palmer Similarity
  maxscore = score if maxscore < score else maxscore
  
print(maxscore)