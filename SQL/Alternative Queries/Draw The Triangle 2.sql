/*
 Enter your query here.
 */
SET
@n = 0;
SELECT REPEAT('* ', @n:= @n + 1)
FROM INFORMATION_SCHEMA.TABLES
WHERE @n < 20;