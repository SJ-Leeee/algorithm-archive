// https://school.programmers.co.kr/learn/courses/30/lessons/140107

// k의 배수로 찍는다 그 순서쌍의 개수
// 그럼 x for문 돌리고 안에서 y for문 돌려야겠다.

function solution(k, d) {
  var answer = 0;

  for (let x = 0; x <= d; x += k) {
    // 0 일때
    // 2
    // 4
    let maxY = Math.sqrt(Math.pow(d, 2) - Math.pow(x, 2));
    answer += Math.floor(maxY / k) + 1;
  }

  console.log(answer);
  return answer;
}

solution(2, 4);
