// https://school.programmers.co.kr/learn/courses/30/lessons/134239

function solution(k, ranges) {
  var answer = [];
  let collatz = [k];
  let area = [];
  while (k > 1) {
    if (k % 2 === 0) {
      k = k / 2;
      collatz.push(k);
    } else {
      k = k * 3 + 1;
      collatz.push(k);
    }

    area.push((collatz[collatz.length - 1] + collatz[collatz.length - 2]) / 2);
  }

  let lastIdx = collatz.length - 1;
  ranges.forEach((i) => {
    if (i[0] > lastIdx + i[1]) {
      answer.push(-1.0);
    } else if (i[0] === lastIdx + i[1]) {
      answer.push(0.0);
    } else {
      let sum = area.slice(i[0], lastIdx + i[1]).reduce((acc, cur) => acc + cur, 0);
      answer.push(sum);
    }
  });
  return answer;
}

solution(3, [
  [0, 0],
  [1, -2],
  [3, -3],
]);

// 콜라츠배열을 어디다가 넣어
// 그리고 ranges로 계산
