import polars as pl

class solutionParser():
    def __init__(self):
        pass

    def parse_solution(self, source):
        solution = pl.read_excel(source=source)
        return solution