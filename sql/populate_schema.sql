INSERT INTO directors (director, yearofbirth) VALUES
('Philip Howard', 1916),
('Nora Rucker', 1920),
('Vivian Dudley', 1991),
('Gary Sullivan', 1984),
('Mildred Hartz', 1994);

INSERT INTO movies (title, year, director, budget, gross) VALUES
('A Blast', 2013, 'Nora Rucker', 200440,4309282),
('A Ciambra', 2009, 'Vivian Dudley', 352984,7035626),
('A l`origine', 2012, 'Philip Howard', 63653,4194798),
('A War', 1934, 'Philip Howard', 191969,6394275),
('A-Team', 2019, 'Vivian Dudley', 118526,2164400);

INSERT INTO movieawards (title, year, award, result) VALUES
('A Blast', 2013, 'oscar, best actor', 'nominated'),
('A Blast', 2013, 'bafta, best supporting actor', 'won'),
('A Ciambra', 2009, 'cannes, best actor', 'nominated'),
('A Ciambra', 2009, 'venice, best actor', 'won'),
('A Ciambra', 2009, 'bafta, best supporting actor', 'won'),
('A Ciambra', 2009, 'bafta, best actor', 'won'),
('A l`origine', 2012, 'cannes, best original screenplay', 'won'),
('A l`origine', 2012, 'cannes, best supporting actor', 'nominated'),
('A l`origine', 2012, 'oscar, best director', 'nominated'),
('A l`origine', 2012, 'golden globe, best actor', 'nominated'),
('A l`origine', 2012, 'oscar, best supporting actor', 'nominated'),
('A l`origine', 2012, 'bafta, best picture', 'won'),
('A l`origine', 2012, 'venice, best original screenplay', 'won'),
('A l`origine', 2012, 'golden globe, best supporting actor', 'nominated'),
('A l`origine', 2012, 'venice, best actor', 'nominated'),
('A l`origine', 2012, 'cannes, best actor', 'won'),
('A War', 1934, 'golden globe, best original screenplay', 'nominated'),
('A War', 1934, 'golden globe, best actor', 'nominated'),
('A War', 1934, 'cannes, best original screenplay', 'nominated'),
('A-Team', 2019, 'cannes, best supporting actor', 'won'),
('A-Team', 2019, 'cannes, best picture', 'nominated'),
('A-Team', 2019, 'oscar, best supporting actor', 'won'),
('A-Team', 2019, 'venice, best actor', 'nominated'),
('A-Team', 2019, 'golden globe, best original screenplay', 'won'),
('A-Team', 2019, 'bafta, best supporting actor', 'nominated'),
('A-Team', 2019, 'bafta, best director', 'won');

INSERT INTO directorawards (director, year, award, result) VALUES
('Philip Howard', 2012, 'oscar', 'nominated'),
('Vivian Dudley', 2019, 'bafta', 'won');