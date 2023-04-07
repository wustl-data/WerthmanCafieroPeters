
  create view "postgres"."dbt"."CornVsWheat__dbt_tmp" as (
    SELECT 
    CONCAT(DATE_PART('year', c.month), '-', DATE_TRUNC('quarter', c.month)) AS period,
    CORR(c.price, w.price) AS correlation
FROM 
    (SELECT price, DATE_TRUNC('month', month) AS month FROM "postgres"."dbt"."5YCorn") AS c 
JOIN 
    (SELECT price, DATE_TRUNC('month', month) AS month FROM "postgres"."dbt"."5YWheat") AS w 
ON 
    DATE_PART('year', c.month) = DATE_PART('year', w.month) AND 
    DATE_PART('month', c.month) = DATE_PART('month', w.month)
GROUP BY 
    period
ORDER BY 
    period
  );