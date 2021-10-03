SET
   @RANGE = 1000;
SELECT
   GROUP_CONCAT(R2.N SEPARATOR '&')
FROM
   (
      SELECT
         @ctr2:= @ctr2 + 1 AS N
      FROM
         INFORMATION_SCHEMA.TABLES R2IS1,
         INFORMATION_SCHEMA.TABLES R2IS2,
         (
            SELECT
               @ctr2:= 1
         ) TI
      WHERE
         @ctr2 < @RANGE
   ) AS R2
WHERE
   NOT EXISTS (
      SELECT
         R1.N
      FROM
         (
            SELECT
               @ctr1:= @ctr1 + 1 AS N
            FROM
               INFORMATION_SCHEMA.TABLES R1IS1,
               INFORMATION_SCHEMA.TABLES R1IS2,
               (
                  SELECT
                     @ctr1:= 1
               ) I1
            WHERE
               @ctr1 < @RANGE
         ) AS R1
      WHERE
         R2.N % R1.N = 0
         AND R2.N > R1.N
   )