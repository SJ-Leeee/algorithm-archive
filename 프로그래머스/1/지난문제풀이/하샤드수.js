// https://school.programmers.co.kr/learn/courses/30/lessons/12947
function solution(x) {
  x = x + "";
  let sum = 0;
  for (let i = 0; i < x.length; i++) {
    sum += Number(x[i]);
  }

  return Number(x) % sum === 0 ? true : false;
}

solution(12345);
// console.log(a);
