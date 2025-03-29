-- 코드를 입력하세요
SELECT BOOK.CATEGORY, SUM(SALES.SALES) AS TOTAL_SALES
FROM BOOK_SALES AS SALES
JOIN BOOK ON SALES.BOOK_ID = BOOK.BOOK_ID
WHERE MONTH(SALES.SALES_DATE) = 1
GROUP BY MONTH(SALES.SALES_DATE), BOOK.CATEGORY
ORDER BY BOOK.CATEGORY