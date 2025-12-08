// https://school.programmers.co.kr/learn/courses/30/lessons/12906

function solution(arr) {
  let result = [];
  let preValue;
  arr.forEach((i) => {
    if (preValue === undefined) {
      result.push(i);
      preValue = i;
    } else if (preValue !== i) {
      result.push(i);
      preValue = i;
    }
  });
  return result;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));
