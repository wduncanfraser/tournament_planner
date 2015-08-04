#!/usr/bin/env python
"""tournament.py -- implementation of a Swiss-system tournament"""

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    # Create connection and cursor
    conn = connect()
    c = conn.cursor()

    # Execute sql for deleting all entries in the Match table
    c.execute('DELETE FROM Match;')

    # Commit transaction and close connection.
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    # Create connection and cursor
    conn = connect()
    c = conn.cursor()

    # Execute sql for deleting all entries in the Player table
    c.execute('DELETE FROM Player;')

    # Commit transaction and close connection.
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    # Create connection and cursor
    conn = connect()
    c = conn.cursor()

    # Executes sql for counting all entries in the Player table
    c.execute('SELECT COUNT(*) AS num FROM Player;')
    player_count = c.fetchone()[0]

    # Commit transaction and close connection.
    conn.commit()
    conn.close()

    # Return the player count retrieved from the query
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # Create connection and cursor
    conn = connect()
    c = conn.cursor()

    # Execute sql for creating new player
    c.execute('INSERT INTO Player (name) VALUES (%s);', (name,))

    # Commit transaction and close connection.
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Create connection and cursor
    conn = connect()
    c = conn.cursor()

    # Execute sql for selecting all entries from the rankings view. List of all players sorted by rankings.
    c.execute('SELECT * FROM rankings;')

    # Commit transaction
    conn.commit()

    # Fetch all returned rows (complete standings list)
    standings = c.fetchall()

    # Close the connection
    conn.close()

    # Return the full list of standings
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Create connection and cursor
    conn = connect()
    c = conn.cursor()

    # Execute sql for inserting a singe match result. Format: Player 1 ID, Player 2 ID, Winning Player ID.
    c.execute('INSERT INTO Match (Player_1_id, Player_2_id, winner_Player_id) VALUES (%s, %s, %s);',
              (winner, loser, winner))

    # Commit transaction and close connection.
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Call playerStandings() to get the current standings
    standings = playerStandings()

    # Loop through the standings 2 at a time, assigning each set as a pairings.
    pairs = [(standings[i][0], standings[i][1], standings[i - 1][0], standings[i - 1][1])
             for i in range(1, len(standings), 2)]

    # Return list of pairs
    return pairs
