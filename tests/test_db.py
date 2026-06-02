## Database
# Imports
import sqlite3

# Creates a connection to the database
con = sqlite3.connect("testsimulation.db")
# Creates a cursor
cur = con.cursor()

# Creates the table
def table_create():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS testsession_templates(description, education, crime, health, economy, property_value, cost_of_living)")
    con.commit()
# Insert Data
def new_template():
    cur.execute("""
        INSERT INTO testsession_templates VALUES
        ('Test Description', 1, 1, 1, 1, 1, 1)
    """)
    con.commit()
# Print table
def print_table():
    cur.execute("SELECT * FROM testsession_templates")
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Clear Table
def clear_table():
    cur.execute("DELETE FROM testsession_templates")
    con.commit()


# Tests
#table_create()
new_template()
#clear_table()
print_table()
