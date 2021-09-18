-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
SELECT HOUR(datetime), COUNT(datetime) FROM animal_outs 
WHERE 9 <= HOUR(datetime) AND HOUR(datetime) < 20
GROUP BY HOUR(datetime) ORDER BY HOUR(datetime) ;