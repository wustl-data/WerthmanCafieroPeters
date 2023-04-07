
  create view "postgres"."dbt"."5YWheat__dbt_tmp" as (
    SELECT month, price FROM "postgres"."dbt"."5yearmodel"
WHERE commodity = 'Corn'
  );