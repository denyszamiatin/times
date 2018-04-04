from text_preprocessors import remove_punctuation, set_lower, set_to_root


class Pipeline:
    def __init__(self, pipelines, transformers):
        self.pipelines = pipelines
        self.transformers = transformers

    def preprocess_article(self, article):
        transformer = iter(self.transformers)
        for pipeline in self.pipelines:
            article = pipeline.preprocess_article(article)
            article = next(transformer)(article)
        return article


class SubPipeline:
    def __init__(self, *preprocessors):
        self.preprocessors = preprocessors

    def preprocess_article(self, article):
        for preprocessor in self.preprocessors:
            article = preprocessor(article)
        return article


def split_transformer(text):
    return text.split()


def fake_transformer(text):
    return text

article_pipeline = SubPipeline(remove_punctuation, set_lower)
words_pipeline = SubPipeline(set_to_root)
pipeline = Pipeline(
    [
        article_pipeline,
        words_pipeline,
    ],
    [
        split_transformer,
        fake_transformer,
    ]
)