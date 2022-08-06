from sklearn.feature_extraction.text import TfidfVectorizer

textFile = ["data/doc1.txt", "data/doc2.txt"]
document = [open(f, encoding="utf-8").read() for f in textFile ]

tfidf  = TfidfVectorizer().fit_transform(document)
pairwise_similarity = (tfidf * tfidf.T).A

print(pairwise_similarity)