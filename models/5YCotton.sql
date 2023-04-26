SELECT month, price FROM {{ref('5yearmodel')}}
WHERE commodity = 'Cotton'
