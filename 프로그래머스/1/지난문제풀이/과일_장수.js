//https://school.programmers.co.kr/learn/courses/30/lessons/135808

function solution(k, m, score) {
  var answer = 0;

  score.sort((a, b) => b - a);
  for (let i = m - 1; i < score.length; i += m) {
    console.log(score[i] * m);
    answer = answer + score[i] * m;
  }

  console.log(`총 점수 : ${answer}`);
  return answer;
}

solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]);
// k는 최대 점수
// m은 한 상자당 사과의 개수
// score는 사과 개당의 점수들
