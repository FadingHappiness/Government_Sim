## Database
import sqlite3
## Creates a connection to the database
con = sqlite3.connect("session_templates.db")
## Creates a cursor
cur = con.cursor()
## Creates the table
def table_create():
    cur.execute("CREATE TABLE")