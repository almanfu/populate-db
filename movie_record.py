class movie_record:
    def __init__(self, movie, movie_year, director, budget, gross, year_of_birth, movie_awards):
        self.movie = movie
        self.movie_year = movie_year
        self.director = director
        self.budget = budget
        self.gross = gross
        self.year_of_birth = year_of_birth
        self.movie_awards = movie_awards

    def __repr__(self):
        return str(self.movie)
