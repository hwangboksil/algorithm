// 평균 구하기
// 정수를 담고 있는 배열 arr의 평균값을 return하는 함수를 작성하세요.

function average(arr) {
  return arr.reduce((prev, num) => prev + num, 0) / arr.length;
}

console.log(average([1, 2, 3, 4]));
console.log(average([5, 5]));

// 1. 인자 값 arr는 배열이므로 reduce 메서드를 사용하여 배열의 전체 값을 계산한다.
// 2. prev를 0으로 세팅하여 첫 시작 값을 0으로 시작한다.
// 3. reduce가 실행되면서 누적된 값 prev와 새로운 값 num을 더하여 전체 값의 합계를 저장한다.
// 4. 저장된 값에 arr의 전체 개수를 세어 나눠준다.
