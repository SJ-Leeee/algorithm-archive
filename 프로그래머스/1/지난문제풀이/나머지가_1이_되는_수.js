// https://school.programmers.co.kr/learn/courses/30/lessons/87389

function solution(n) {
  let div = 2;

  while (div <= n / 2) {
    if (n % div === 1) return div;
    div++;
  }

  return n - 1;
}
//

solution(10);
// 3, 5
