CREATE TYPE awardresult AS ENUM
('won', 'nominated');
CREATE TABLE directors
(
director varchar(50) NOT NULL,
yearofbirth integer NOT NULL,
CONSTRAINT "directors_pkey" PRIMARY KEY (director)
);
CREATE TABLE movies
(
title varchar(100) NOT NULL,
year integer NOT NULL,
director varchar(50) NOT NULL,
budget integer NOT NULL,
gross integer NOT NULL,
CONSTRAINT "movies_pkey" PRIMARY KEY (title, year),
CONSTRAINT "directorawards_director_fkey" FOREIGN KEY (director)
REFERENCES directors(director)
);
CREATE TABLE directorawards
(
director varchar(50) NOT NULL,
year integer NOT NULL,
award varchar(100) NOT NULL,
result awardresult NOT NULL,
CONSTRAINT "DirectorAwards_pkey" PRIMARY KEY (director, year, award),
CONSTRAINT "DirectorAwards_director_fkey" FOREIGN KEY (director)
REFERENCES Directors(director)
);
CREATE TABLE movieawards
(
title varchar(100) NOT NULL,
year integer NOT NULL,
award varchar(100) NOT NULL,
result awardresult NOT NULL,
CONSTRAINT "movieawards_pkey" PRIMARY KEY (title, year, award),
CONSTRAINT "movieawards_year_title_fkey" FOREIGN KEY (title, year)
REFERENCES movies(title, year)
);