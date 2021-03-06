/*
 Enter your query here.
 */
SELECT ID,
       AGE,
       COINS_NEEDED,
       POWER
FROM WANDS AS MAIN_WANDS
         LEFT JOIN WANDS_PROPERTY AS MAIN_WANDS_PROPERTY ON MAIN_WANDS.CODE = MAIN_WANDS_PROPERTY.CODE
WHERE IS_EVIL = 0
  AND COINS_NEEDED = (
    SELECT MIN(COINS_NEEDED)
    FROM WANDS AS SUB_WANDS
             LEFT JOIN WANDS_PROPERTY AS SUB_WANDS_PROPERTY ON SUB_WANDS.CODE = SUB_WANDS_PROPERTY.CODE
    WHERE SUB_WANDS.POWER = MAIN_WANDS.POWER
      AND SUB_WANDS_PROPERTY.AGE = MAIN_WANDS_PROPERTY.AGE
)
ORDER BY POWER DESC,
         AGE DESC