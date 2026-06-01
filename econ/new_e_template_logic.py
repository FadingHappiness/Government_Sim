## New E-Template Logic

import session_e_templates as session
# Creates the template ID
def template_id():
    return len(session.session_templates) + 1
# Adds the new template session templates
def add_template():
    new_template = dict(Des="n/a", Edu=0, Crm=0, Hth=0, Ecn=0, Ppv=0, Col=0, Id=template_id())
    session.session_templates.append(new_template)

