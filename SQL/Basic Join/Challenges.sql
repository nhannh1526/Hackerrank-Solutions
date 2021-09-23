/*
 Enter your query here.
 */
SELECT
   CHALLENGES.HACKER_ID,
   NAME,
   COUNT(CHALLENGES.HACKER_ID) AS CNT
FROM
   HACKERS
   RIGHT JOIN CHALLENGES ON HACKERS.HACKER_ID = CHALLENGES.HACKER_ID
GROUP BY
   CHALLENGES.HACKER_ID,
   NAME
HAVING
   CNT = (
      SELECT
         COUNT(HACKER_ID) AS CNT
      FROM
         CHALLENGES
      GROUP BY
         HACKER_ID
      ORDER BY
         CNT DESC
      LIMIT
         1
   )
   OR CNT IN (
      SELECT
         CNT
      FROM
         (
            SELECT
               COUNT(*) AS CNT
            FROM
               CHALLENGES
            GROUP BY
               HACKER_ID
         ) AS TMP
      GROUP BY
         CNT
      HAVING
         COUNT(CNT) = 1
   )
ORDER BY
   CNT DESC,
   CHALLENGES.HACKER_ID