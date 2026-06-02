## New E-Templates
# Imports
import sqlite3

# Creates a connection to the database
con = sqlite3.connect("simulation.db")
# Creates a cursor
cur = con.cursor()


# Gets count of template in database
def get_id():
    template_id = cur.execute("SELECT COUNT(*) FROM simulation.db")
# List of new templates
session_templates = []
#
# Multiplier of templates
def multiple_templates():
    pass