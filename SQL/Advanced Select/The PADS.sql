/*
 Enter your query here.
 */
SELECT
   CONCAT(NAME, '(', LEFT(OCCUPATION, 1), ')')
FROM
   OCCUPATIONS
ORDER BY
   NAME;
SELECT
   CONCAT(
      'There are a total of ',
      COUNT(*),
      ' ',
      LOWER(OCCUPATION),
      's.'
   )
FROM
   OCCUPATIONS
GROUP BY
   OCCUPATION
ORDER BY
   COUNT(*),
   OCCUPATION;