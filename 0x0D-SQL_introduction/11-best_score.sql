-- Lists all records from second_table where score >= 10 asc.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
