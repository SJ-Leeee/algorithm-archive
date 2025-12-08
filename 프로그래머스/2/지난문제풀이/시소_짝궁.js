// https://school.programmers.co.kr/learn/courses/30/lessons/152996

function solution(weights) {
  var answer = 0;
  let dict = {};
  for (let weight of weights) {
    if (dict[weight] === undefined) dict[weight] = 1;
    else dict[weight] += 1;
  }

  weights.sort();

  for (let weight of weights) {
    if (dict[weight] > 1) answer += dict[weight] - 1;
    if (dict[weight * 2] > 0) answer += dict[weight * 2];
    if (dict[weight * (4 / 3)] > 0) answer += dict[weight * (4 / 3)];
    if (dict[weight * (3 / 2)] > 0) answer += dict[weight * (3 / 2)];

    dict[weight] -= 1;
  }
  return answer;
}
solution([100, 180, 360, 100, 270]);
// 따져보면 2:1, 3:2, 4:3 만해주며된다

// weight = [100,200,100,150]
// [100,100,150,200]
// [200,300,400, 450, 600,] +3 +1 +3

// 본질은 각각의 배수들의 조합을 구하는 것
// 1. 정렬을 한다 (안해도될 수도)
// 2. 0번째부터 2,3,4 한것을 배열에 넣는다.
// 3. 배열에서 해당숫자가 있으면 count++ 없으면 삽입
// 4. 만약 같은수라면? [100,100,150] 이러면 짝궁은 3개
// [200,300,400,300,450,600] +1 +3 +1
