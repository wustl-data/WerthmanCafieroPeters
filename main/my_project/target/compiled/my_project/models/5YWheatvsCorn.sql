SELECT 
    DATE_PART('year', month) AS year,
    DATE_PART('month', month) AS month,
    CORR(price, 
         (SELECT price 
          FROM "postgres"."dbt"."5yearmodel" 
          WHERE commodity = 'Wheat' AND 
                DATE_PART('year', month) = DATE_PART('year', commodities2.date) AND 
                DATE_PART('month', month) = DATE_PART('month', commodities2.date)
         )
    ) AS correlation
FROM 
    "postgres"."dbt"."5yearmodel" 
WHERE 
    commodity = 'Corn'
GROUP BY 
    DATE_PART('year', month), 
    DATE_PART('month', month)