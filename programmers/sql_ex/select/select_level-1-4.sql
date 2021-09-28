-- 동물 중 젊은 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
-- 1. INTAKE_CONDITION이 Aged가 아닌 경우를 뜻함
SELECT animal_id, name FROM animal_ins WHERE intake_condition <> "Aged" ORDER BY animal_id;