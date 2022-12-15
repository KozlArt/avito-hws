from math import log


class CountVectorizer:
    def __init__(self):
        self.features = None

    def fit_transform(self, corpus: list):
        # fit
        features = set()
        for i, elm in enumerate(corpus):
            corpus[i] = [i.lower() for i in elm.split()]
        for elm in corpus:
            features = features | set(elm)
        self.features = list(features)
        # transform
        count_matrix = []
        for elm in corpus:
            count_elm = []
            for feature in features:
                count_elm.append(elm.count(feature))
            count_matrix.append(count_elm)
        return count_matrix

    def get_feature_names(self):
        return self.features


def tf_transform(count_matrix: list) -> list:
    tf_matrix = []
    for emb in count_matrix:
        N = sum(emb)
        tf_matrix.append([])
        for elm in emb:
            tf_matrix[-1].append(elm / N)
    return tf_matrix


def idf_transform(count_matrix: list) -> list:

    sum_count_matrix = [0 for i in count_matrix[0]]
    for emb in count_matrix:
        for i, elm in enumerate(emb):
            sum_count_matrix[i] += elm

    idf_matrix = [
        1 + log((len(count_matrix) + 1) / (elm + 1)) for elm in sum_count_matrix
    ]
    return idf_matrix


class idf_transformer:
    def __init__(self) -> None:
        pass

    def fit_transform(self, count_matrix: list) -> list:
        tf_matrix = []
        for emb in count_matrix:
            N = sum(emb)
            tf_matrix.append([])
            for elm in emb:
                tf_matrix[-1].append(elm / N)

        sum_count_matrix = [0 for i in count_matrix[0]]
        for emb in count_matrix:
            for i, elm in enumerate(emb):
                sum_count_matrix[i] += elm

        idf_matrix = [
            1 + log((len(count_matrix) + 1) / (elm + 1)) for elm in sum_count_matrix
        ]

        tfidf_matrix = []

        for emb in tf_matrix:
            tfidf = []
            for i, elm in enumerate(idf_matrix):
                tfidf.append(elm * emb[i])
            tfidf_matrix.append(tfidf)
        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self.tdidf = idf_transformer()

    def fit_transform(self, corpus: list) -> list:
        count_matrix = super().fit_transform(corpus)
        return self.tdidf.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
    print("tf", tf_transform(count_matrix))
    print("idf", idf_transform(count_matrix))
    vectorizer = idf_transformer()
    tfidf_matrix = vectorizer.fit_transform(count_matrix)
    print("tfidf", tfidf_matrix)
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print("tfidf from corpus", tfidf_matrix)
