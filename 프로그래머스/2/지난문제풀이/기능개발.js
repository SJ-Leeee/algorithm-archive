// https://school.programmers.co.kr/learn/courses/30/lessons/42586

function solution(progresses, speeds) {
  var answer = [];
  let finished = []; // 완료 작업일을 표시해줄 배열
  for (let i = 0; i < progresses.length; i++) {
    finished.push(Math.ceil((100 - progresses[i]) / speeds[i]));
  } // 작업속도로 나눈 후 소수올림

  let count = 1; // 일괄 처리될 작업의 개수
  let previous = finished[0]; // 작업일을 비교해줄 값
  for (let j = 1; j < finished.length; j++) {
    if (previous >= finished[j]) {
      // 현재 작업일이 이전작업일보다 작으면
      count++;
    } else {
      // 그게 아니면
      answer.push(count);
      previous = finished[j];
      count = 1;
    }
  }
  if (count > 0) answer.push(count);
  return answer;
}

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]);
// Math.ceil;

// [93, 30, 55]	[1, 30, 5]	[2, 1]
