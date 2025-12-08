// https://school.programmers.co.kr/learn/courses/30/lessons/12950

function solution(arr1, arr2) {
  var answer = [];
  for (let row = 0; row < arr1.length; row++) {
    // 행 순환
    let newRow = [];
    for (let col = 0; col < arr1[0].length; col++) {
      // 열 순환
      // arr1 = [[1,2],[2,3]], arr2= [[3,4],[5,6]] res= [[4,6],[7,9]]
      newRow.push(arr1[row][col] + arr2[row][col]);
    }
    answer.push(newRow);
  }
  return answer;
}

solution(
  [
    [1, 2],
    [2, 3],
  ],
  [
    [3, 4],
    [5, 6],
  ]
);
