// https://school.programmers.co.kr/learn/courses/30/lessons/42889

function solution(N, stages) {
  let faliObj = {};
  stages = stages.sort((a, b) => a - b);

  for (let i = 1; i < N + 1; i++) {
    let clearIndex = stages.lastIndexOf(i);
    if (clearIndex !== -1) {
      faliObj[i] = (clearIndex + 1) / stages.length;
      stages = stages.slice(clearIndex + 1);
    } else {
      faliObj[i] = 0;
    }
  }

  return Object.entries(faliObj)
    .sort((a, b) => b[1] - a[1])
    .map((i) => Number(i[0]));
}

solution(5, [2, 1, 2, 6, 2, 4, 3, 3]);
solution(4, [4, 4, 4, 4, 4]);
// console.log([1, 1, 1, 2, 2, 3, 3, 3, 3].slice(2));
// 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]

// 스테이지 1,2,3,4,5

/*
  1스테이지 생존자 찾기
  마지막1을 찾는다
  있다? index + 1명 존재하는거다
  없다? 1은 존재하지 않기때문에 실패율은 0

*/
