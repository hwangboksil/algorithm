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
  const fruits = "π, π₯, π, π";
  const result = fruits.split();
  console.log(result);

  // [Output]
  // ['π, π₯, π, π']
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
  // μνλ λΆλΆλ§ λ°μμ μ λ°°μ΄λ‘ μμ±νλ€ .slice(x, n-1)
  const result1 = array.slice(2, 5); // κΈ°μ‘΄ λ°°μ΄μμ μΈλ±μ€ xλΆν° n-1κΉμ§ μ λ°°μ΄λ‘ μμ±λλ€.

  // κΈ°μ‘΄ λ°°μ΄μμ νΉμ  μΈλ±μ€λΆν° nκ°λ₯Ό μ κ±° λ° λ°ν
  const result2 = array.splice(0, 2);

  //μ²« λ²μ§Έ μμ μ κ±° λ° λ°ν
  const result3 = array.shift();

  console.log(result1);
  console.log(result2);
  console.log(result3);
  console.log(array);

  // [Output]
  // [3, 4, 5]
  // [1, 2]
  // 3
  // [4, 5] result1μμλ μλ‘μ΄ λ°°μ΄μ΄ μμ λμ΄ arrayλ μν₯μ΄ μκ³ , result2μ 3μ κΈ°μ‘΄ λ°°μ΄μ μμ νλ€.
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
// λλ¦Όμ½λ©
{
  const result = students.filter((item) => item.enrolled);
  console.log(result);
}

// λ΄κ° μκ°ν λ‘μ§
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
  const result = students.some((student) => student.score < 50); // νλλΌλ μ΄ μ‘°κ±΄μ λ§μ‘±λλ μ¬λμ΄ μλ€λ©΄ True
  const result2 = students.every((student) => student.score < 50); // λͺ¨λ  μ¬λμ΄ μ΄ μ‘°κ±΄μ λ§μ‘±λλ€λ©΄ True

  console.log(result);
  console.log(result2);
  console.log(!result2); // κ²°κ³Ό κ°μ λ°λλ‘ μΆλ ₯νκ³  μΆλ€λ©΄ ! μ¬μ©ν΄μλ κ°λ₯νλ€.
}

// Q9. compute students' average score
{
  // μ½λ κ°κ²°ν
  const result = students.reduce((prev, student) => prev + student.score, 0);
  console.log(result / students.length);

  // // previou(μ΄μ ), current(νμ¬) κ°, currentλ μλ―Έλ₯Ό νμνκΈ° μν΄ studentλ‘ λ³κ²½.
  // const result = students.reduce((prev, student) => {
  //   // console.log(prev);
  //   // console.log(student);
  //   return prev + student.score;
  // }, 0); // ν¨μ μ€ν μ 0μ prev μΈμκ°μ λ£μ΄μ€λ€.
  // console.log(result / students.length);
}

// Q10. make a string containing all the scores
// result should be: '45, 80, 90, 66, 88'
{
  const result = students.map((student) => student.score).join();
  // console.log(result.join()); λλ λ³μμμ joinμ μ§μ 
  console.log(result);
}

// Q10-1[ν¨μλ₯Ό μ¬λ¬κ° μ?μ΄ μ¬μ© κ°λ₯ === ν¨μν νλ‘κ·Έλλ°] filter() ν¨μλ₯Ό μΆκ°νμ¬ 50μ  μ΄μμΈ μ μλ§ κ°μ Έμ€κΈ°
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
  // ν° μκ° λ¨Όμ μ€λλ‘ μ λ ¬
  const result = students
    .map((student) => student.score)
    .sort((a, b) => b - a)
    .join();
  console.log(result);
}
