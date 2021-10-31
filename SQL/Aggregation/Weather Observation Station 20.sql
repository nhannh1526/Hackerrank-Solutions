/*
 Enter your query here.
 */
SET
@rowIdx := -1;
SELECT ROUND(AVG(LAT_N), 4)
FROM (
         SELECT @rowIdx := @rowIdx + 1 AS rowIdx,
         LAT_N
         FROM
             STATION
         ORDER BY
             LAT_N
     ) AS STATION_INDEXED
WHERE rowIdx IN (FLOOR(@rowIdx / 2), CEIL(@rowIdx / 2))