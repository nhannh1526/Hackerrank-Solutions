/*
 Enter your query here.
 */
SET
@r1 = 0,
   @r2 = 0,
   @r3 = 0,
   @r4 = 0;
SELECT MIN(DOCTOR),
       MIN(PROFESSOR),
       MIN(SINGER),
       MIN(ACTOR)
FROM (
         SELECT CASE
                    WHEN OCCUPATION = 'DOCTOR' THEN (@r1:= @r1 + 1)
                    WHEN OCCUPATION = 'PROFESSOR' THEN (@r2:= @r2 + 1)
                    WHEN OCCUPATION = 'SINGER' THEN (@r3:= @r3 + 1)
                    WHEN OCCUPATION = 'ACTOR' THEN (@r4:= @r4 + 1)
                    END AS ROWNUMBER,
                CASE
                    WHEN OCCUPATION = 'DOCTOR' THEN NAME
                    END AS DOCTOR,
                CASE
                    WHEN OCCUPATION = 'PROFESSOR' THEN NAME
                    END AS PROFESSOR,
                CASE
                    WHEN OCCUPATION = 'SINGER' THEN NAME
                    END AS SINGER,
                CASE
                    WHEN OCCUPATION = 'ACTOR' THEN NAME
                    END AS ACTOR
         FROM OCCUPATIONS
         ORDER BY NAME
     ) AS TEMPORARY
GROUP BY
    ROWNUMBER