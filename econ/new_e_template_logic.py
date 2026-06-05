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
    template_id = count[0] + 1
    return(template_id)

# Insert Data
def new_template():
    template_id = get_id()
    cur.execute("INSERT INTO session_templates VALUES ('Test Description', 1, 1, 1, 1, 1, 1, ?)", (template_id,))
    con.commit()

# List of new templates
#session_templates = []
#
# Multiplier of templates
def multiple_templates():
    pass

new_template()