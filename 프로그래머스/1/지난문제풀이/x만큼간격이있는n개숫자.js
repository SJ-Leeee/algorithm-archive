/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/12954
 */
function solution(x, n) {
  let i = 0;
  return Array.from({ length: n }, () => {
    i = i + x;
    return i;
  });
}

console.log(solution(-1, 5));
