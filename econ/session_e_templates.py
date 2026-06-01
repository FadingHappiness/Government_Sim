## Session E-Templates

session_templates = [dict(Des="Built a police station", Edu=0, Crm=-3, Hth=0, Ecn=0, Ppv=0, Col=0, Id=1),
                     dict(Des="Built a school", Edu=3, Crm=0, Hth=0, Ecn=0, Ppv=0, Col=0, Id=2), ]


# Adds the different stats together #
def total_edu():
    return sum(template["Edu"] for template in session_templates)


def total_crm():
    return sum(template["Crm"] for template in session_templates)


def total_hth():
    return sum(template["Hth"] for template in session_templates)


def total_ecn():
    return sum(template["Ecn"] for template in session_templates)


def total_ppv():
    return sum(template["Ppv"] for template in session_templates)


def total_col():
    return sum(template["Col"] for template in session_templates)


#Dictionary of total percentage changes
def econ_impact():
    dict(Edu=total_edu(), Crm=total_crm(), Hth=total_hth(), Ecn=total_ecn(), Ppv=total_ppv(), Col=total_col())
