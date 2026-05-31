## E-Template Logic

def template_id():
    return len(current_templates) + 1

new_template = {"Des": "n/a",
                "Edu": 0,
                "Crm": 0,
                "Hth": 0,
                "Ecn": 0,
                "Ppv": 0,
                "Col": 0,
                "Id": template_id(),
                }

def add_template():
    current_templates.append(new_template)

