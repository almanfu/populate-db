import json
import names
import random

from director import Director
from movie import Movie
from director_award import DirectorAward
from movie_award import MovieAward

def has_repetition_movie_awards(movie_awards, title, year, award):
  for a in movie_awards:
    if a.title == title and a.year == year and a.award == award:
      return True
  return False

def rnd_award():
  events = ['oscar', 'golden globe', 'bafta', 'cannes', 'venice']
  prizes = ['best actor', 'best director', 'best picture', 'best supporting actor', 'best original screenplay']
  
  rnd_event = random.choice(events)
  rnd_prize = random.choice(prizes)
  return f'{rnd_event}, {rnd_prize}'

def rnd_yearofbirth():
  return random.randint(1890, 2002)

NDIRECTORS = 5
NMOVIES = 5
MAXAWARDS = 10

def main():

  with open('movie_titles_short.json') as titles_json:
    titles = json.load(titles_json)['movie_titles'][0:NMOVIES]

    DIRECTORS = []
    DIRECTOR_NAMES = []

    MOVIES = []
    MOVIE_TITLES = []

    MOVIE_AWARDS = []
    DIRECTOR_AWARDS = []

    # generate Director
    for _ in range(0, NDIRECTORS):
      name = names.get_full_name()
      if name not in DIRECTOR_NAMES:
        DIRECTOR_NAMES.append(name)
        DIRECTORS.append(Director(name, rnd_yearofbirth()))

    # generate Movie
    for movie_title in titles:
        director = random.choice(DIRECTORS)
        year = random.randint(director.yearofbirth+18, 2022)
        budget = random.randint(10_000, 1_000_000)
        gross = random.randint(100_000, 10_000_000)

        movie = Movie(movie_title, year, director, budget, gross)

        if movie.title not in MOVIE_TITLES:
            MOVIES.append(movie)
            MOVIE_TITLES.append(movie.title)

            # generate MovieAward
            for _ in range(0, random.randint(0, MAXAWARDS)):
                movieAward = MovieAward(movie.title, movie.year, rnd_award(), random.choice(['won', 'nominated']))

                # only one movie can have an award for (year, event, prize)
                if not has_repetition_movie_awards(MOVIE_AWARDS, movie.title, movie.year, movieAward.award):
                    MOVIE_AWARDS.append(movieAward)

                    # generate DirectorAward, 
                    if 'best director' in movieAward.award:
                        directorAward = DirectorAward(
                            movie.director, movie.year, movieAward.award.split(',')[0], movieAward.result)
                        DIRECTOR_AWARDS.append(directorAward)

    # Write queries
    f = open('sql/populate_schema.sql', 'w')
    f.write('INSERT INTO directors (director, yearofbirth) VALUES\n')
    first_run = True
    for d in DIRECTORS:
        first_run = False if first_run == True else f.write(f',\n')
        f.write(f'(\'{d.name}\', {d.yearofbirth})')

    f.write(';\n\nINSERT INTO movies (title, year, director, budget, gross) VALUES\n')
    first_run = True
    for m in MOVIES:
        first_run = False if first_run == True else f.write(f',\n')
        f.write(
            f'(\'{m.title}\', {m.year}, \'{m.director.name}\', {m.budget},{m.gross})')

    f.write(';\n\nINSERT INTO movieawards (title, year, award, result) VALUES\n')
    first_run = True
    for a in MOVIE_AWARDS:
        first_run = False if first_run == True else f.write(f',\n')
        f.write(
            f'(\'{a.title}\', {a.year}, \'{a.award}\', \'{a.result}\')')

    f.write(';\n\nINSERT INTO directorawards (director, year, award, result) VALUES\n')
    first_run = True
    for a in DIRECTOR_AWARDS:
        first_run = False if first_run == True else f.write(f',\n')
        f.write(
            f'(\'{a.director.name}\', {a.year}, \'{a.award}\', \'{a.result}\')')
    f.write(';')
    f.close()

main()