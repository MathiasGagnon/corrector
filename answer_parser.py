import polars as pl

class answerParser():
    def __init__(self):
        pass

    def parse_answers(self, source):
        answers = pl.read_csv(source=source)

        return answers