// https://school.programmers.co.kr/learn/courses/30/lessons/42862
function solution(n, lost, reserve) {
  // 잃어버린 사람 오름차순
  lost = lost.sort((a, b) => a - b);

  // 전체 - 잃어버린 사람
  var answer = n - lost.length;

  // 여유있는 분들 List
  let reserveObj = {};
  reserve.forEach((i) => {
    reserveObj[i] = 1;
  });

  // 내 것 없는 사람 다시 배열화
  let noMe = [...lost];

  // 내 것 있는 사람들 제외 루프
  for (let i = 0; i < lost.length; i++) {
    if (reserveObj[lost[i]]) {
      answer++;
      let index = noMe.indexOf(lost[i]); // 나의 인덱스를 찾습니다.
      if (index !== -1) {
        // 만약 요소가 발견되었다면
        noMe.splice(index, 1); // 해당 인덱스의 요소를 제거합니다.
      }
      reserveObj[lost[i]] -= 1;
    }
  }

  // 내 것이 아닌 사람들 루프
  for (let i = 0; i < noMe.length; i++) {
    if (reserveObj[noMe[i] - 1] && reserveObj[noMe[i] - 1] > 0) {
      answer++;
      reserveObj[noMe[i] - 1] -= 1;
    } else if (reserveObj[noMe[i] + 1] && reserveObj[noMe[i] + 1] > 0) {
      answer++;
      reserveObj[noMe[i] + 1] -= 1;
    }
  }

  return answer;
}
solution(24, [1, 3, 4, 5, 7, 21], [1, 3, 5, 7, 21, 22]);
// 만약에 [3,4] [2,3] or [2,5]

// reserve를 객체에다가 저장
// lost+1,-1를 체크..

// 근데 만약에 [3,4,7], [1,4,5,7]
