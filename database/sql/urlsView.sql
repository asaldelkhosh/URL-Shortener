CREATE VIEW urls_get_view AS
    SELECT * FROM urls ORDER BY count desc LIMIT 3;