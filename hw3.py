from typing import List


class CountVectorizer():
    def __init__(self):
        self.features = None

    def fit_transform(self, corpus: List):
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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
