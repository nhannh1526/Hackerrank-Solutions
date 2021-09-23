/*
 Enter your query here.
 */
SELECT
   START_DATE,
   MIN(END_DATE)
FROM
   (
      SELECT
         START_DATE
      FROM
         PROJECTS
      WHERE
         START_DATE NOT IN (
            SELECT
               END_DATE
            FROM
               PROJECTS
         )
   ) AS START_DATE_STATS,
   (
      SELECT
         END_DATE
      FROM
         PROJECTS
      WHERE
         END_DATE NOT IN (
            SELECT
               START_DATE
            FROM
               PROJECTS
         )
   ) AS END_DATE_STATS
WHERE
   START_DATE < END_DATE
GROUP BY
   START_DATE
ORDER BY
   DATEDIFF(MIN(END_DATE), START_DATE),
   START_DATE