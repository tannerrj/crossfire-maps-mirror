from email.mime.text import MIMEText
import subprocess

import Crossfire

def report(pl):
    desc = Crossfire.ScriptParameters()
    if desc == None:
        pl.Message("To report an issue, type 'report <description of the issue>'.")
        return

    details = {
        'PLAYER': Crossfire.WhoAmI().Name,
        'MAP': Crossfire.WhoAmI().Map.Path,
        'X': Crossfire.WhoAmI().X,
        'Y': Crossfire.WhoAmI().Y,
        'DESC': desc,
    }

    report = """
Reporter:   {PLAYER}
Map:        {MAP} ({X}, {Y})
Report:     {DESC}
""".format(**details)

    Crossfire.Log(Crossfire.LogInfo, "A problem was reported: %s" % (report))

    msg = MIMEText(report)
    recipient = "crossfire"
    msg["From"] = "crossfire"
    msg["Subject"] = "Crossfire issue report"

    try:
        result = subprocess.run(['sendmail', recipient], universal_newlines=True, input=msg.as_string(), timeout=2)
        if result.returncode == 0:
            pl.Message("Thank you for your report.")
        else:
            error(pl)
    except subprocess.TimeoutExpired:
        error(pl)
        Crossfire.Log(Crossfire.LogError, "Timed out while reporting a problem")

def error(pl):
    pl.Message("There was an error reporting your problem. Please try again or contact a Dungeon Master to report your problem.")

report(Crossfire.WhoAmI())
