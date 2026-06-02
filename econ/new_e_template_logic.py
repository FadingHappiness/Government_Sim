## New E-Templates
# Imports
import sqlite3
from db import con
from db import cur

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

get_id()