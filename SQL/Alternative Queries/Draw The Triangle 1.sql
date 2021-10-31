/*
 Enter your query here.
 */
SET
@n = 21;
SELECT REPEAT('* ', @n:= @n - 1)
FROM INFORMATION_SCHEMA.TABLES
WHERE @n > 0;