import sqlite3

conn = sqlite3.connect("database.db")

print("Opened database successfully")

conn.execute("CREATE TABLE matches (team_a TEXT NOT NULL, score_a INT NOT NULL, wicket_a INT NOT NULL, four_a INT NOT NULL, six_a INT NOT NULL, team_b TEXT NOT NULL, score_b INT NOT NULL, wicket_b INT NOT NULL, four_b INT NOT NULL,six_b INT NOT NULL, winner TEXT NOT NULL, man_of_match TEXT NOT NULL,match_date DATE NOT NULL)")
        
print ("Table matches created successfully")

conn.execute("CREATE TABLE teams (team_name TEXT NOT NULL, coach_name TEXT NOT NULL, captian_name TEXT NOT NULL, no_match INT NOT NULL)")

print("Table teams created successfully")

conn.close()