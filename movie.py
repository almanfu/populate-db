class Movie:
    def __init__(self, title, year, director, budget, gross):
        self.title = title
        self.year = year
        self.director = director
        self.budget = budget
        self.gross = gross

    def __repr__(self):
        return str(self.title)
