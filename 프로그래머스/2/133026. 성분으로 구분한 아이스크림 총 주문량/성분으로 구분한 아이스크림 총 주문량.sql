-- 코드를 입력하세요
SELECT II.INGREDIENT_TYPE, SUM(FH.TOTAL_ORDER) TOTAL_ORDER
FROM ICECREAM_INFO II
JOIN FIRST_HALF FH ON II.FLAVOR = FH.FLAVOR
GROUP BY II.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER