/*
 Enter your query here.
 */
SELECT HACKERS.HACKER_ID,
       NAME
FROM (
         SELECT SUBMISSIONS.HACKER_ID,
                COUNT(SUBMISSION_ID) AS NUMBER_OF_FULL_SCORE
         FROM (
                  SELECT CHALLENGE_ID,
                         SCORE
                  FROM DIFFICULTY
                           INNER JOIN CHALLENGES ON DIFFICULTY.DIFFICULTY_LEVEL = CHALLENGES.DIFFICULTY_LEVEL
              ) AS DIFFICULTY_OF_THE_CHALLENGE
                  INNER JOIN SUBMISSIONS ON DIFFICULTY_OF_THE_CHALLENGE.CHALLENGE_ID = SUBMISSIONS.CHALLENGE_ID
         WHERE DIFFICULTY_OF_THE_CHALLENGE.SCORE = SUBMISSIONS.SCORE
         GROUP BY SUBMISSIONS.HACKER_ID
     ) AS FULL_SCORE_STATS
         INNER JOIN HACKERS ON FULL_SCORE_STATS.HACKER_ID = HACKERS.HACKER_ID
WHERE NUMBER_OF_FULL_SCORE > 1
ORDER BY NUMBER_OF_FULL_SCORE DESC,
         HACKER_ID