-- For the update from schema 1 to 2, we add a primary key
-- to the regions table. This prevents duplicate entries being added
-- on every initialization of the reputation code.
-- To keep most configurations functional, we will select the set of distinct
-- table entries into a temporary table, then drop the cluttered table, and
-- rename the tmp table to be the same name as the dropped table.

CREATE TABLE regions_tmp(
    faction      TEXT,
    region       TEXT,    -- region name (or 'ALL') this faction controls
    influence    NUMERIC,
    PRIMARY KEY  (faction, region),
    CONSTRAINT   influence_range CHECK(influence BETWEEN 0 AND 1)
);

INSERT INTO regions_tmp
    SELECT DISTINCT faction, region, influence FROM regions;

DROP TABLE regions;

ALTER TABLE regions_tmp RENAME TO regions;

UPDATE schema SET version = 2;
