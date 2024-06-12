from collection import Counter, defaultdict
from scipy.sparse import vstack
import numpy as np
import re
import math


class ContentBase:

    def __init__(self):
        pass


    def toneknize(text):
        text = re.sub('[^A-Za-z0-9]+', " ", text)
        tokens = text.split()
        return tokens


    def term_frecuency(tokens):
        term_count = Counter(tokens)
        total_term = len(tokens)
        return np.array([count/total_term for count in term_count.items()])


    def inverse_document_frequency(tokens):
        N = len(tokens)
        document_frequency = defaultdict(int)
        for tokens in tokens:
            unique_tokens = set(tokens)
            for token in tokens:
                document_frequency[token] += 1
        return np.array([math.log((N + 1)/(df_count +1)) +1 for df_count in document_frequency.items()])


    def data_generator(array, chunk_size=1):
        for start in range(0, len(array), chunk_size):
            yield array[start:start + chunk_size]


    def tf_idf_score(term_frecuency, inverse_document_frequency):
        tfidf_sparse_matrices = []
        for chunk_term_frecuency in self.data_generator(term_frecuency):
            for chunk_inverse_document_frequency in self.data_generator(inverse_document_frequency):
                tfidf_sparse_matrices.append(chunk_term_frecuency * chunk_inverse_document_frequency.reshape(-1, 1))
        return vstack(tfidf_sparse_matrices)


    def get_recommenders(title, cosine_sim=cosine_sim):
        idx = df.index[df["title"] == title].tolist()[0]
        sim_score = list(enumurate(cosine_sim[idx]))
        sim_score = sorted(sim_score, key=lambda x:x[1], reverse=Treu)
        sim_score = sim_score[:5]
        movie_indices = [i[0] for i in sim_score]
        return df["title"].iloc[movie_indices]
