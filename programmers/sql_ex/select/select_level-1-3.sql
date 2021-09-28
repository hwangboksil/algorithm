-- 동물 중 아픈 동물1의 아이디와 이름을 조회하는 SQL 문을 작성. 이때 결과는 아이디 순으로 조회
SELECT animal_id, name FROM animal_ins WHERE intake_condtion = "Sick" ORDER BY animal_id;