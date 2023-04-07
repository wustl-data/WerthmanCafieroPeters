
  create view "postgres"."dbt"."5yearmodel__dbt_tmp" as (
    SELECT * FROM commodities2 WHERE month >= TO_DATE('2018-01-01', 'YYYY-MM-DD')
ORDER BY month DESC
  );