from email.mime.text import MIMEText
import subprocess

import CFSqlDb as cfdb
import Crossfire

status_codes = ["new", "open", "feedback", "fixed", "closed", "unknown"]

usage = {
    'delete': lambda x: report_delete(x),
    'help': lambda x: report_help(x),
    'list': lambda x: report_list(x),
}

pl = Crossfire.WhoAmI()

def status(i):
    return status_codes[min(i, len(status_codes))]

def make_report():
    desc = Crossfire.ScriptParameters()

    reporter = pl.Name
    m = pl.Map.Path
    x = pl.X
    y = pl.Y
    rid = None
    with cfdb.open() as db:
        num = db.execute("""
            INSERT INTO reports (reporter, date, map, mapX, mapY, info)
            VALUES (?, unixepoch('now'), ?, ?, ?, ?)
            RETURNING id;""", (reporter, m, x, y, desc))
        rid = num.fetchone()[0]
        pl.Message("Thank you for your report. Your report was assigned an ID of %d. Use 'report list to check the status of your reports." % rid)

    details = {
        'PLAYER': reporter,
        'MAP': m,
        'X': x,
        'Y': y,
        'DESC': desc,
    }

    report = """
Reporter:   {PLAYER}
Map:        {MAP} ({X}, {Y})
Report:     {DESC}
""".format(**details)

    Crossfire.Log(Crossfire.LogInfo, "Problem %d was reported: %s" % (rid, report))

    msg = MIMEText(report)
    recipient = "crossfire"
    msg["From"] = "crossfire"
    msg["Subject"] = "Crossfire issue report %d" % rid

    try:
        subprocess.run(['sendmail', recipient], universal_newlines=True, input=msg.as_string(), timeout=2)
    except subprocess.TimeoutExpired:
        Crossfire.Log(Crossfire.LogError, "Timed out while reporting a problem")

def report_list(args):
    with cfdb.open() as db:
        query = "SELECT id, status, SUBSTRING(info, 1, 30) FROM reports WHERE reporter=?"
        if len(args) > 0:
            res = db.execute(query + " AND (id=? OR info LIKE ('%' || ? || '%'))", (Crossfire.WhoAmI().Name, args, args));
        else:
            res = db.execute(query, (Crossfire.WhoAmI().Name,));
        msg = []
        for num, state, summary in res.fetchall():
            msg.append("%d\t(%s)\t%s..." % (num, status(state), summary))
        if len(args) > 0:
            if len(msg) < 1:
                msg = ["No reports found with the specified search pattern."]
            else:
                msg.insert(0, "Found %d reports." % len(msg))
        else:
            if len(msg) < 1:
                msg = ["You have no reports."]
            else:
                msg.insert(0, "Use 'report list <SEARCH> to search your reports by text or ID.")
        Crossfire.WhoAmI().Message("\n".join(msg))

def report_delete(args):
    with cfdb.open() as db:
        res = db.execute("DELETE FROM reports WHERE reporter=? AND id=? RETURNING id;", (pl.Name, args));
        num = len(res.fetchall())
        if num < 1:
            pl.Message("No such report from you found.")
        else:
            pl.Message("Report deleted.")

def report_help(args):
    msg = ["The report command accepts the following subcommands:"]
    for k in usage.keys():
        msg.append("- %s" % k)
    pl.Message("\n".join(msg))

def cmdmain(args):
    if args is None:
        pl.Message("To report an issue, type 'report <description of the issue>'. For help, type 'report help.")
        return

    args = args.split(" ", maxsplit=1)
    rest = ""
    if len(args) > 1:
        rest = args[1]
    if args[0] in usage:
        usage[args[0]](rest)
    else:
        make_report()

cmdmain(Crossfire.ScriptParameters())
