-- 1.
SELECT * FROM user WHERE name LIKE '박%' LIMIT 10;

-- 2.
SELECT t.id, u.name, s.name, i.name FROM user u JOIN order o ON u.id=o.userId JOIN store s ON o.storeid=s.Id JOIN orderitem oi ON o.id=oi.orderId JOIN item i ON oi.itemId = i.Id WHERE u.Id="6da2aec9-5aa2-4cc4-aba1-df81cef0cc02";

-- 3.

-- 4.

-- 5. 특정 사용자가 주문한 매출액의 합산