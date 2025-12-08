// https://school.programmers.co.kr/learn/courses/30/lessons/181187

function solution(r1, r2) {
  let answer = 0;
  for (let x = 1; x <= r2; x++) {
    let bigY = Math.sqrt(Math.pow(r2, 2) - Math.pow(x, 2));
    let smallY = Math.sqrt(Math.pow(r1, 2) - Math.pow(x, 2));
    if (!smallY) smallY = 0;
    let conut = Math.floor(bigY) - Math.ceil(smallY) + 1;
    answer += conut;
  }
  return answer * 4;
}

console.log(solution(2, 4));
