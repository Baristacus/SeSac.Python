-- SELECT: 컬럼 및 테이블
SELECT COUNT(*) FROM 테이블명;
SELECT * FROM 테이블명;
SELECT * FROM LIMIT 10;

-- INSERT: 데이터 추가
INSERT INTO 테이블명(열1, 열2, ...) VALUES(값1, 값2, ...);

-- UPDATE: 데이터 변경
UPDATE 테이블명 SET 컬럼명 = 값 WHERE 컬럼명 = 값;

-- DELETE: 데이터 삭제
DELETE FROM 테이블명 WHERE 컬럼명 = 값

-- ORDER BY: 정렬
SELECT * FROM 테이블 ORDER BY 컬럼명;
SELECT * FROM 테이블 ORDER BY 컬럼명 DESC;

-- GROUP BY: 그룹
SELECT * FROM 테이블 GROUP BY 컬럼명;
SELECT * FROM 테이블 GROUP BY 컬럼명 ORDER BY 컬럼명;

-- DISTINCT: 중복 데이터 제거
SELECT DISTINCT(컬럼1, 컬럼2, ...) FROM 테이블;

-- DROP: 테이블 삭제
DROP TABLE 테이블;

-- INNER JOIN
SELECT * FROM 테이블1 INNER JOIN 테이블2 ON 테이블1.컬럼명 = 테이블2.컬럼명;
SELECT 테이블1.컬럼1, 테이블1.컬럼2 ... FROM 테이블1 INNER JOIN 테이블2 ON 테이블1.컬럼명 = 테이블2.컬럼명;

-- LEFT JOIN
SELECT * FROM 테이블1 LEFT JOIN 테이블2 ON 테이블1.컬럼명 = 테이블2.컬럼명;

-- RIGHT JOIN
SELECT * FROM 테이블1 RIGHT JOIN 테이블2 ON 테이블1.컬럼명 = 테이블2.컬럼명;

-- FULL JOIN
SELECT * FROM 테이블1 FULL OUTER JOIN 테이블2 ON 테이블1.컬럼명 = 테이블2.컬럼명;