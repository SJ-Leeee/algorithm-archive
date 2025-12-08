// https://school.programmers.co.kr/learn/courses/30/lessons/389478

function solution(n, w, num) {
  let basicLine = Math.floor(n / w); // 22/6 -> 3
  // 기본라인
  let addLine = n % w; // 22%6 -> 4
  // 추가라인
  let isReverse = basicLine % 2 !== 0 ? true : false;
  // 역방향
  let lineArr = Array.from({ length: w }, () => basicLine);

  let startIdx = isReverse ? w - 1 : 0;
  // 홀수면 반대부터 짝수면 순방향

  while (addLine > 0) {
    lineArr[startIdx]++;
    if (isReverse) startIdx--;
    else startIdx++;
    addLine--;
  }

  let row = Math.floor(num / w); // 8/6 -> 1
  let col = num % w; // 8%6 -> 2
  let locationReverse = row % 2 !== 0 ? true : false;
  let myLoacation;
  if (col === 0) {
    myLoacation = locationReverse ? w - 1 : 0;
    row--;
  } else {
    myLoacation = locationReverse ? w - col : col - 1;
  }
  let answer = lineArr[myLoacation] - row;

  return answer;
}

solution(13, 3, 7);
