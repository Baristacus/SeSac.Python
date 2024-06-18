-- [v] 1. 미국에 거주하지 않는 고객(전체 이름, 고객 ID 및 국가)을 표시하는 쿼리를 제공합니다.

SELECT FirstName ||' '|| LastName AS FullName, CustomerId, Country FROM customers WHERE Country != 'USA';

-- [v] 2. 브라질 고객만 표시하는 쿼리를 제공합니다.

SELECT FirstName ||' '|| LastName AS FullName FROM customers WHERE Country = 'Brazil';

-- [v] 3. 브라질 고객의 송장을 보여주는 쿼리를 제공합니다. 결과 테이블에는 고객의 전체 이름, 송장 ID, 송장 날짜 및 청구 국가가 표시되어야 합니다.

SELECT FirstName ||' '|| LastName AS FullName, InvoiceId, InvoiceDate, Country FROM customers INNER JOIN Invoices WHERE customers.CustomerId = Invoices.CustomerId AND Country = 'Brazil';

-- [v] 4. 판매 대리인인 직원만 표시하는 쿼리를 제공하십시오.

SELECT FirstName ||' '|| LastName AS '판매 대리인' FROM employees WHERE Title LIKE 'Sales%';

-- [ ] 5. 송장 테이블에서 청구 국가의 고유/고유 목록을 표시하는 쿼리를 제공합니다.

SELECT DISTINCT(BillingCountry) FROM invoices;

-- [ ] 6. 각 판매 에이전트와 연결된 송장을 표시하는 쿼리를 제공합니다. 결과 테이블에는 영업 에이전트의 전체 이름이 포함되어야 합니다.

-- [ ] 7. 모든 송장 및 고객에 대한 송장 합계, 고객 이름, 국가 및 판매 대리점 이름을 표시하는 쿼리를 제공합니다.

SELECT c.FirstName ||' '|| c.LastName AS Customer, i.BillingCountry, e.FirstName ||' '|| e.LastName AS 'Sales Agent', i.Total FROM customers c INNER JOIN invoices i ON c.CustomerId = i.CustomerId INNER JOIN employees e ON c.SupportRepId = e.EmployeeId;

-- [ ] 8. 2009년과 2011년에 몇 개의 인보이스가 있었습니까?

-- [ ] 9. 각 연도의 총 매출은 얼마입니까?

-- [ ] 10. InvoiceLine 테이블을 보고 Invoice ID 37에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다.

-- [ ] 11. InvoiceLine 테이블을 보고 각 Invoice에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다. 힌트: 그룹화 기준

-- [ ] 12. 각 송장 라인 항목에 구매한 트랙 이름을 포함하는 쿼리를 제공합니다.

-- [ ] 13. 구매한 트랙 이름과 아티스트 이름을 포함하는 쿼리를 각 송장 라인 항목과 함께 제공합니다.

-- [ ] 14. 국가별 송장 수를 표시하는 쿼리를 제공합니다. 힌트: 그룹화 기준

-- [ ] 15. 각 재생 목록의 총 트랙 수를 표시하는 쿼리를 제공합니다. 재생 목록 이름은 결과 테이블에 포함되어야 합니다.

-- [ ] 16. 모든 트랙을 표시하지만 ID는 표시하지 않는 쿼리를 제공합니다. 결과에는 앨범 이름, 미디어 유형 및 장르가 포함되어야 합니다.

-- [ ] 17. 모든 송장을 표시하지만 송장 라인 항목의 수를 포함하는 쿼리를 제공합니다.

-- [ ] 18. 판매 대리점별 총 매출을 조회하는 쿼리를 제공한다.

-- [ ] 19. 2009년 가장 많은 매출을 올린 판매원은?
    -- 힌트: 하위 쿼리에서 MAX 함수를 사용하십시오.

-- [ ] 20. 전체 판매 실적이 가장 많은 판매 대리점은?

-- [ ] 21. 각 판매 대리점에 할당된 고객 수를 보여주는 쿼리를 제공한다.

-- [ ] 22. 국가별 총 매출을 보여주는 쿼리를 제공한다.

-- [ ] 23. 고객이 가장 많이 지출한 국가는 어디입니까?

-- [ ] 24. 2013년 가장 많이 구매한 트랙을 보여주는 쿼리를 제공합니다.

-- [ ] 25. 가장 많이 구매한 상위 5곡을 보여주는 쿼리를 제공합니다.

-- [ ] 26. 가장 많이 팔린 3명의 아티스트를 보여주는 쿼리를 제공합니다.

-- [ ] 27. 가장 많이 구매한 Media Type을 보여주는 쿼리를 제공한다.