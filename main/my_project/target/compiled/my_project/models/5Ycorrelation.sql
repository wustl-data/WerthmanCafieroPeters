SELECT corr(CAST(price AS numeric), EXTRACT(epoch FROM month)::numeric) as correlation
FROM "postgres"."dbt"."5yearmodel"

-- https://www.geeksforgeeks.org/sql-query-to-convert-datetime-to-epoch/
-- https://stackoverflow.com/questions/43845138/ms-sql-server-cast-int-to-price-format