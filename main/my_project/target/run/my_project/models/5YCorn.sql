
  create view "postgres"."dbt"."5YCorn__dbt_tmp" as (
    SELECT month, price FROM "postgres"."dbt"."5yearmodel"
WHERE commodity = 'Cotton'
  );