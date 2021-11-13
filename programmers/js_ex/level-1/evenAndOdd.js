// 짝수와 홀수
// 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수를 작성해주세요.

function solution(num) {
  if (num % 2 === 0) {
    return "Even";
  } else {
    return "Odd";
  }
}

console.log(solution(3));
console.log(solution(4));

// 1. if 문을 사용하여 인자 값 num을 2로 나눴을 떄 나머지가 0이면 'Even' 리턴
// 2. 0이 아니면 'Odd' 리턴을 한다.
