// Q1. make a string out of an array
{
  const fruits = ["apple", "banana", "orange"];
  console.log(fruits.join());
  console.log(fruits.join(" and "));

  // [Output]
  // apple,banana,orange
  // apple and banana and orange
}

// Q2. make an array out of a string
{
  const fruits = "🍎, 🥝, 🍌, 🍒";
  const result = fruits.split();
  console.log(result);

  // [Output]
  // ['🍎, 🥝, 🍌, 🍒']
}

// Q3. make this array look like this: [5, 4, 3, 2, 1]
{
  const array = [1, 2, 3, 4, 5];
  const result = array.reverse();
  console.log(result);

  // [Output]
  // [5, 4, 3, 2, 1]
}

// Q4. make new array without the first two elements
{
  const array = [1, 2, 3, 4, 5];
  // 원하는 부분만 받아서 새 배열로 생성한다 .slice(x, n-1)
  const result1 = array.slice(2, 5); // 기존 배열에서 인덱스 x부터 n-1까지 새 배열로 생성된다.

  // 기존 배열에서 특정 인덱스부터 n개를 제거 및 반환
  const result2 = array.splice(0, 2);

  //첫 번째 원소 제거 및 반환
  const result3 = array.shift();

  console.log(result1);
  console.log(result2);
  console.log(result3);
  console.log(array);

  // [Output]
  // [3, 4, 5]
  // [1, 2]
  // 3
  // [4, 5] result1에서는 새로운 배열이 생선되어 array는 영향이 없고, result2와 3은 기존 배열을 수정한다.
}

class Student {
  constructor(name, age, enrolled, score) {
    this.name = name;
    this.age = age;
    this.enrolled = enrolled;
    this.score = score;
  }
}
const students = [
  new Student("A", 29, true, 45),
  new Student("B", 28, false, 80),
  new Student("C", 30, true, 90),
  new Student("D", 40, false, 66),
  new Student("E", 18, true, 88),
];

// Q5. find a student with the score 90
// arrow function
{
  const result = students.find((item) => item.score === 90);
  console.log(result);
}

// function
// {
//   const result = students.find(function (item) {
//     return item.score === 90;
//   });
//   console.log(result);
// }

// Q6. make an array of enrolled students
// 드림코딩
{
  const result = students.filter((item) => item.enrolled);
  console.log(result);
}

// 내가 생각한 로직
// {
//   let array = [];
//   const result = students.find((item) => {
//     if (item.enrolled === true) {
//       array.push(item.name);
//     }
//   });

//   console.log(array);
// }

// Q7. make an array containing only the students' scores
// result should be: [45, 80, 90, 66, 88]
{
  const result = students.map((item) => item.score);
  const result2 = students.map((item) => item.score * 2);

  console.log(result);
  console.log(result2);
}

// Q8. check if there is a student with the score lower than 50
{
  console.clear();
  const result = students.some((student) => student.score < 50); // 하나라도 이 조건에 만족되는 사람이 있다면 True
  const result2 = students.every((student) => student.score < 50); // 모든 사람이 이 조건에 만족된다면 True

  console.log(result);
  console.log(result2);
  console.log(!result2); // 결과 값을 반대로 출력하고 싶다면 ! 사용해서도 가능하다.
}

// Q9. compute students' average score
{
  // 코드 간결화
  const result = students.reduce((prev, student) => prev + student.score, 0);
  console.log(result / students.length);

  // // previou(이전), current(현재) 값, current는 의미를 파악하기 위해 student로 변경.
  // const result = students.reduce((prev, student) => {
  //   // console.log(prev);
  //   // console.log(student);
  //   return prev + student.score;
  // }, 0); // 함수 실행 시 0을 prev 인자값에 넣어준다.
  // console.log(result / students.length);
}

// Q10. make a string containing all the scores
// result should be: '45, 80, 90, 66, 88'
{
  const result = students.map((student) => student.score).join();
  // console.log(result.join()); 또는 변수에서 join을 지정
  console.log(result);
}

// Q10-1[함수를 여러개 엮어 사용 가능 === 함수형 프로그래밍] filter() 함수를 추가하여 50점 이상인 점수만 가져오기
{
  const result = students
    .map((student) => student.score)
    .filter((score) => score >= 50)
    .join();
  console.log(result);
}

// Bonus! do Q10 sorted in ascending order
// result should be: '45, 66, 80, 88, 90'
{
  const result = students
    .map((student) => student.score)
    .sort()
    .join();
  console.log(result);
}

{
  // 큰 수가 먼저오도록 정렬
  const result = students
    .map((student) => student.score)
    .sort((a, b) => b - a)
    .join();
  console.log(result);
}
