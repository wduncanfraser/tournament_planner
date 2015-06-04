-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP TABLE Match;
DROP TABLE Player;

CREATE TABLE Player (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE Match (
  id SERIAL PRIMARY KEY,
  Player_1_id INT NOT NULL REFERENCES Player(id),
  Player_2_id INT NOT NULL REFERENCES Player(id),
  winner_Player_id INT REFERENCES Player(id),
  CHECK (Player_1_id != Match.Player_2_id),
  CHECK (winner_Player_id = Player_1_id OR winner_Player_id = Player_2_id)
);