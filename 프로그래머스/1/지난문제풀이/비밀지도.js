/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/17681
 * 2진수로 바꾼 후
 * 둘다 0 인경우 공백 아니면 #을 대입한다.
 *
 * 2의 16승일 경우
 * 2진수로 바꾸는 작업 = n log n
 *
 * 비밀지도를 만드는작업 = n log n
 *
 * => O(n log n)
 */

function arrToBin(arr, n) {
  let result = [];

  for (let i of arr) {
    let sqrt = n - 1;
    let binaryStr = "";
    while (sqrt >= 0) {
      if (i >= 2 ** sqrt) {
        i -= 2 ** sqrt;
        binaryStr += "1";
      } else {
        binaryStr += "0";
      }
      sqrt--;
    }
    result.push(binaryStr);
  }
  return result;
}

// arrToBin([30, 1, 21, 17, 28], 5);

function solution(n, arr1, arr2) {
  let arr1ToBin = arrToBin(arr1, n);
  let arr2ToBin = arrToBin(arr2, n);

  let result = [];

  for (let i = 0; i < arr1ToBin.length; i++) {
    let resultLine = "";
    for (let j = 0; j < n; j++) {
      if (arr1ToBin[i][j] === "0" && arr2ToBin[i][j] === "0") resultLine += " ";
      else resultLine += "#";
      // console.log(`${i}번째 resultLine ${resultLine}`);
    }
    result.push(resultLine);
  }

  // return result;
}

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]);
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]);
