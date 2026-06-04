## Database 1.0
# Imports
import sqlite3

# Creates a connection to the db and creates the db if it's not already
con = sqlite3.connect('econ.db')
# Creates a cursor
cur = con.cursor()

# Creates the table
def table_create():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS session_templates(description, education, crime, health, economy, property_value, cost_of_living, template_id)")
    con.commit()


# Insert Data
def new_template():
    cur.execute("INSERT INTO session_templates VALUES ('Test Description', 1, 1, 1, 1, 1, 1, 1)")
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


# Close Connection
def close_connection():
    con.close()
