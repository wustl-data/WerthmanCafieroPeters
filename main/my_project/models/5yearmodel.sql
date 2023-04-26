SELECT * 
FROM {{ source('5year', 'commodities2') }} 
WHERE month >= TO_DATE('2018-01-01', 'YYYY-MM-DD')
ORDER BY month DESC
