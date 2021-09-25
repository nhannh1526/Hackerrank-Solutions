/*
 Enter your query here.
 */
SELECT
   CONTESTS.CONTEST_ID,
   HACKER_ID,
   NAME,
   SUM(TOTAL_SUBMISSIONS) AS SUM_OF_TOTAL_SUBMISSIONS,
   SUM(TOTAL_ACCEPTED_SUBMISSIONS) AS SUM_OF_TOTAL_ACCEPTED_SUBMISSIONS,
   SUM(TOTAL_VIEWS) AS SUM_OF_TOTAL_VIEWS,
   SUM(TOTAL_UNIQUE_VIEWS) AS SUM_OF_TOTAL_UNIQUE_VIEWS
FROM
   CONTESTS
   INNER JOIN COLLEGES ON CONTESTS.CONTEST_ID = COLLEGES.CONTEST_ID
   INNER JOIN CHALLENGES ON COLLEGES.COLLEGE_ID = CHALLENGES.COLLEGE_ID
   LEFT JOIN (
      SELECT
         CHALLENGE_ID,
         SUM(TOTAL_VIEWS) AS TOTAL_VIEWS,
         SUM(TOTAL_UNIQUE_VIEWS) AS TOTAL_UNIQUE_VIEWS
      FROM
         VIEW_STATS
      GROUP BY
         CHALLENGE_ID
   ) AS VIEW_STATS ON CHALLENGES.CHALLENGE_ID = VIEW_STATS.CHALLENGE_ID
   LEFT JOIN (
      SELECT
         CHALLENGE_ID,
         SUM(TOTAL_SUBMISSIONS) AS TOTAL_SUBMISSIONS,
         SUM(TOTAL_ACCEPTED_SUBMISSIONS) AS TOTAL_ACCEPTED_SUBMISSIONS
      FROM
         SUBMISSION_STATS
      GROUP BY
         CHALLENGE_ID
   ) AS SUBMISSION_STATS ON CHALLENGES.CHALLENGE_ID = SUBMISSION_STATS.CHALLENGE_ID
GROUP BY
   CONTESTS.CONTEST_ID,
   HACKER_ID,
   NAME
HAVING
   SUM_OF_TOTAL_SUBMISSIONS > 0
   AND SUM_OF_TOTAL_ACCEPTED_SUBMISSIONS > 0
   AND SUM_OF_TOTAL_VIEWS > 0
   AND SUM_OF_TOTAL_UNIQUE_VIEWS > 0
ORDER BY
   CONTESTS.CONTEST_ID