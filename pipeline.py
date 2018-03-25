from text_preprocessors import remove_punctuation, set_lower, set_to_root


class Pipeline:
    def __init__(self, article):
        self.words = article['Text'].split()
        self.preprocessors = [remove_punctuation, set_lower, set_to_root]

    def preprocess_article(self):
        for preprocessor in self.preprocessors:
            self.words[:] = preprocessor(self.words)
        return self.words
