-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP VIEW rankings;
DROP TABLE Match;
DROP TABLE Player;

-- Player table
CREATE TABLE Player (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Table for recording matches
-- If a match is a draw, the winner_Player_id is set to null
CREATE TABLE Match (
    id SERIAL PRIMARY KEY,
    Player_1_id INT NOT NULL REFERENCES Player(id),
    Player_2_id INT NOT NULL REFERENCES Player(id),
    winner_Player_id INT REFERENCES Player(id),
    CHECK (Player_1_id != Match.Player_2_id),
    CHECK (winner_Player_id = Player_1_id OR winner_Player_id = Player_2_id OR winner_Player_id is NULL)
);

-- View for selecting current rankings by score. Win is 3 points, draw is 1
CREATE VIEW rankings AS
    SELECT Player.id, name,
    ((SELECT COUNT(*) FROM Match WHERE Player.id = Match.winner_Player_id) * 3)
    + (SELECT COUNT(*) FROM Match WHERE Match.winner_Player_id is NULL) AS score,
    (SELECT COUNT(*) FROM Match WHERE Player.id = Match.Player_1_id OR Player.id = Match.Player_2_id) AS matches
    FROM Player
    ORDER BY score DESC;