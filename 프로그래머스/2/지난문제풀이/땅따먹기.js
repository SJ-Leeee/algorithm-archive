// https://school.programmers.co.kr/learn/courses/30/lessons/12913

function solution(land) {
  let excep0 = 0;
  let excep1 = 1;
  let excep2 = 2;
  let excep3 = 3;

  let sum0 = land[0][0];
  let sum1 = land[0][1];
  let sum2 = land[0][2];
  let sum3 = land[0][3];

  for (let i = 1; i < land.length; i++) {
    let zero = check([...land[i]], excep0);
    sum0 += zero.maxNum;
    excep0 = zero.nextExcepIdx;
    let one = check([...land[i]], excep1);
    sum1 += one.maxNum;
    excep1 = one.nextExcepIdx;
    let two = check([...land[i]], excep2);
    sum2 += two.maxNum;
    excep2 = two.nextExcepIdx;
    let three = check([...land[i]], excep3);
    sum3 += three.maxNum;
    excep3 = three.nextExcepIdx;
  }
  // console.log(sum0, sum1, sum2, sum3);
  return Math.max(sum0, sum1, sum2, sum3);
}

function check(arr, excepIdx) {
  let maxNum = -Infinity;
  let nextExcepIdx;
  if (excepIdx) arr[excepIdx] = 0;
  for (let i = 0; i < 4; i++) {
    if (arr[i] > maxNum) {
      maxNum = arr[i];
      nextExcepIdx = i;
    }
  }
  return { maxNum, nextExcepIdx };
}

/*
    1. 첫번째 줄은 가장 큰 것을 밟는다.
    2. 두번째 줄부터는 해당 인덱스를 제외해야한다.
*/

solution([
  [6, 7, 1, 2],
  [2, 3, 10, 8],
  [1, 3, 9, 4],
  [7, 11, 4, 9],
]);

solution([
  [1, 2, 3, 5],
  [5, 6, 7, 8],
  [4, 3, 2, 1],
]);
