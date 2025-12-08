// https://school.programmers.co.kr/learn/courses/30/lessons/12982

function solution(d, budget) {
  d = d.sort((a, b) => a - b);
  // 만약 budget에서 d[0] 을 빼도 괜찮다면,
  var answer = 0;
  while (d.length > 0) {
    console.log(`while ${d[0]}`);
    // d가 하나라도 있을 때
    if (budget - d[0] >= 0) {
      console.log(`if`);
      // 예산 여유있을 때
      budget -= d.shift();
      answer++;
    } else {
      console.log(`else`);
      // 여유 없을 때
      break;
    }
  }

  console.log(answer);
  return answer;
}

solution([2, 1, 3, 4, 1, 51, 6, 2], 9);
