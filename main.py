import json
import names
import random
import movie_award
import movie_record
import director_award
import director as dir
import os
import time
import alive_progress
from alive_progress.styles import showtime


if os.path.exists("queries.txt"):
    os.remove("queries.txt")


def check_repetition_over_movie_awards(movie_awards_array, title, year, award):
    for e in movie_awards_array:
        if e.title == title and e.year == year and e.award == award:
            return True
    return False


def check_repetition_over_director_awards(director_awards_array, director_name, year, award):
    for e in director_awards_array:
        if e.director.name == director_name and e.year == year and e.award == award:
            return True
    return False


def generate_award():
    awards1 = ['Oscar', 'Golden Globe', 'BAFTA', 'Cannes', 'Venice']
    rnd_award1 = awards1[random.randint(0, 4)]

    awards2 = ['Best Actor', 'Best Actress', 'Best Director', 'Best Picture', 'Best Supporting Actor', 'Best Supporting Actress', 'Best Original Screenplay',
               'Best Adapted Screenplay', 'Best Animated Feature', 'Best Foreign Language Film', 'Best Documentary Feature', 'Best Original Score', 'Best Original Song']
    rnd_award2 = awards2[random.randint(0, 12)]
    return f'{rnd_award1}, {rnd_award2}'


def random_year_director():
    return random.randint(1890, 2002)


with open('film_title.json') as titles_json:
    titles = json.load(titles_json)
    records = []

    ALL_MOVIE_AWARDS = []
    ALL_DIRECTOR_AWARDS = []
    ALL_DIRECTOR_NAMES = []
    ALL_DIRECTORS = []
    ALL_FILM_TITLES = []

    with alive_progress.alive_bar(11609, title="Generating DB...", bar='filling', spinner="classic") as bar:
        # Generate 500 directors
        for i in range(0, 500):
            name = names.get_full_name()
            if name not in ALL_DIRECTOR_NAMES:
                ALL_DIRECTOR_NAMES.append(name)
                ALL_DIRECTORS.append(dir.director(
                    name, random_year_director()))
            bar()

        for film_title in titles["film_titles"]:
            this_director = random.choice(ALL_DIRECTORS)
            # meglio che il regista abbia almeno 16 anni prima di aver diretto il film
            this_year = random.randint(this_director.yearofbirth + 16, 2022)
            this_budget = random.randint(10_000, 1_000_000)
            this_gross = random.randint(100_000, 10_000_000)

            n_awards = random.randint(0, 10)
            this_movie_awards_array = []
            this_movie_director_awards_array = []

            if film_title not in ALL_FILM_TITLES:
                for j in range(0, n_awards):
                    this_generated_award = generate_award()
                    this_award_result = random.choice(['won', 'nominated'])

                    this_movie_award = movie_award.movie_award(
                        film_title, this_year, this_generated_award, this_award_result)

                    # controllo che non ci siano duplicati del premio per il film
                    if not check_repetition_over_movie_awards(ALL_MOVIE_AWARDS, film_title, this_year, this_generated_award):
                        this_movie_awards_array.append(this_movie_award)
                        ALL_MOVIE_AWARDS.append(this_movie_award)

                        # Se il premio include il regista, aggiungilo alla lista dei premi del regista
                        if "Best Director" in this_movie_award.award and check_repetition_over_director_awards(ALL_DIRECTOR_AWARDS, this_director.name, this_year, this_movie_award.award.split(",")[0]) == False:
                            this_director_awards = director_award.director_award(
                                this_director, this_year, this_movie_award.award.split(",")[0], this_movie_award.result)
                            this_movie_director_awards_array.append(
                                this_director_awards)
                            ALL_DIRECTOR_AWARDS.append(this_director_awards)

                records.append(movie_record.movie_record(film_title, this_year, this_director, this_budget,
                                                         this_gross, this_movie_director_awards_array, this_movie_awards_array))
                ALL_FILM_TITLES.append(film_title)
            bar()

    # Write queries

    sum = ALL_DIRECTORS.__len__() + ALL_MOVIE_AWARDS.__len__() + \
        ALL_DIRECTOR_AWARDS.__len__() + records.__len__()
    with alive_progress.alive_bar(sum, title="Writing on queries.txt...", bar='filling', spinner="classic") as bar:

        f = open("queries.txt", "a")

        f.write("INSERT INTO directors (director, yearofbirth) VALUES\n")
        first_run = True
        for d in ALL_DIRECTORS:
            first_run = False if first_run else f.write(",\n")
            f.write(f'(\'{d.name}\', {d.yearofbirth})')
            bar()

        f.write(
            ";\n\nINSERT INTO movies (title, year, director, budget, gross) VALUES\n")
        first_run = True
        for r in records:
            first_run = False if first_run else f.write(",\n")
            f.write(
                f'(\'{r.movie}\', {r.movie_year}, \'{r.director.name}\', {r.budget},{r.gross})')
            bar()

        f.write("\nINSERT INTO movieawards (title, year, award, result) VALUES\n")
        first_run = True
        for a in ALL_MOVIE_AWARDS:
            first_run = False if first_run else f.write(",\n")
            f.write(
                f'(\'{a.title}\', {a.year}, \'{a.award}\', \'{a.result}\')')
            bar()

        f.write("\nINSERT INTO directorawards (director, year, award, result) VALUES\n")
        first_run = True
        for a in ALL_DIRECTOR_AWARDS:
            first_run = False if first_run else f.write(",\n")
            f.write(
                f'(\'{a.director.name}\', {a.year}, \'{a.award}\', \'{a.result}\')')
            bar()

        f.close()
