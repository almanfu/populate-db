import json

MAXLENGTH=25
MAXWORDS=2

fin = open('movie_titles.json', 'r')
fout = open('movie_titles_short.json', 'w+')
movie_titles = json.load(fin)['movie_titles']
movie_titles_short = {"movie_titles":[]}

for movie_title in movie_titles:
  if len(movie_title.split(' ')) <= MAXWORDS and len(movie_title) <= MAXLENGTH:
    movie_titles_short["movie_titles"].append(movie_title)

json.dump(movie_titles_short, fout)

fin.close()
fout.close()
