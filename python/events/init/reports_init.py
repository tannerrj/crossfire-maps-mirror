import CFSqlDb as cfdb

with cfdb.open() as db:
    db.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY,
        reporter TEXT,
        date DATE,
        client TEXT,
        status INT DEFAULT 0,
        map TEXT,
        mapX INT,
        mapY INT,
        info TEXT
    );
    """)
