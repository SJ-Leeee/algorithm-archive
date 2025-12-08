//https:school.programmers.co.kr/learn/courses/30/lessons/172928
function solution(park, routes) {
  var answer = [];
  let location = [];

  park.forEach((i, idx) => {
    let startCol = i.indexOf("S");
    if (startCol !== -1) {
      location.push(idx, startCol);
    }
  });
  let a = "abc";
  console.log(a.indexOf("b"));

  return answer;
}

solution();

// 전략

// ["SOO","OOO","OOO"]	["E 2","S 2","W 1"]

// 현재 S를 찾는다 '[0,0]'
// S를 기준으로 명령을 수행
// 넘는지 확인 max를 잡아둔다
// 장애물확인어케하지
