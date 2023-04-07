SELECT 
    DATE_PART('year', subquery.month) AS year,
    AVG(subquery.correlation) AS avg_correlation
FROM (
    SELECT 
        DATE_TRUNC('month', c.month) AS month,
        CORR(c.price, w.price) AS correlation
    FROM 
        (SELECT price, month FROM "postgres"."dbt"."5YCotton") AS c 
    JOIN 
        (SELECT price, month FROM "postgres"."dbt"."5YWheat") AS w 
    ON 
        DATE_PART('year', c.month) = DATE_PART('year', w.month) AND 
        DATE_PART('month', c.month) = DATE_PART('month', w.month)
    GROUP BY 
        DATE_TRUNC('month', c.month)
) AS subquery
GROUP BY 
    DATE_PART('year', subquery.month)
ORDER BY 
    year