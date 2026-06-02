## Database
# Imports
import sqlite3

# Creates a connection to the database
con = sqlite3.connect("simulation.db")
# Creates a cursor
cur = con.cursor()


# Creates the table
def table_create():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS session_templates(description, education, crime, health, economy, property_value, cost_of_living, template_id)")
    con.commit()

# Print table
def print_table():
    cur.execute("SELECT * FROM session_templates")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Clear Table
def clear_table():
    cur.execute("DELETE FROM session_templates")
    con.commit()

table_create()