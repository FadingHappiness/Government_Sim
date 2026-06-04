## New E-Templates
# Imports
import sqlite3

# Creates a connection to the db and creates the db if it's not already
con = sqlite3.connect('econ.db')
# Creates a cursor
cur = con.cursor()

# Gets count of template in database
def get_id():
    cur.execute("SELECT COUNT(*) FROM session_templates")
    count = cur.fetchone()
    template_id = count[0]
    print(template_id)

# List of new templates
#session_templates = []
#
# Multiplier of templates
def multiple_templates():
    pass