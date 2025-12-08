// https://school.programmers.co.kr/learn/courses/30/lessons/42840

function type1(answers) {
  const answerType = [1, 2, 3, 4, 5];
  let point = 0;
  // 만약 6번이랑 비교 === idx % answerType.length
  answers.forEach((i, idx) => {
    if (i === answerType[idx % answerType.length]) {
      point++;
    }
    // console.log(`i = ${i}`);
    // console.log(`answerType[idx % answerType.length] = ${answerType[idx % answerType.length]}`);
    // console.log(`a = ${a}`);
  });

  return point;
}

function type2(answers) {
  const answerType = [2, 1, 2, 3, 2, 4, 2, 5];
  let point = 0;
  // 만약 6번이랑 비교 === idx % answerType.length
  answers.forEach((i, idx) => {
    if (i === answerType[idx % answerType.length]) {
      point++;
    }
  });

  return point;
}

function type3(answers) {
  const answerType = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let point = 0;
  // 만약 6번이랑 비교 === idx % answerType.length
  answers.forEach((i, idx) => {
    if (i === answerType[idx % answerType.length]) {
      point++;
    }
  });

  return point;
}

function solution(answers) {
  var answer = [];
  const type1Point = type1(answers);
  const type2Point = type2(answers);
  const type3Point = type3(answers);
  const maxPoint = Math.max(type1Point, type2Point, type3Point);

  // 최대 값과 같은 변수들 찾기
  const maxVariables = [];
  if (type1Point === maxPoint) {
    maxVariables.push(1);
  }
  if (type2Point === maxPoint) {
    maxVariables.push(2);
  }
  if (type3Point === maxPoint) {
    maxVariables.push(3);
  }

  return maxVariables;
}

solution([1, 3, 3, 5, 5]);
// 1. 1,2,3,4,5 ...
// 2. 2,1,2,3,2,4,2,5,2,1
// 3. 3,3,1,1,2,2,4,4,5,5,3,3 ...
