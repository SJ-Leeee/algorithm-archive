// https://school.programmers.co.kr/learn/courses/30/lessons/67256

const locaLine = {
  1: [0, 0],
  2: [0, 1],
  3: [0, 2],
  4: [1, 0],
  5: [1, 1],
  6: [1, 2],
  7: [2, 0],
  8: [2, 1],
  9: [2, 2],
  "*": [3, 0],
  0: [3, 1],
  "#": [3, 2],
};

function solution(numbers, hand) {
  hand = hand === "right" ? "R" : "L";
  let leftLoca = "*";
  let rightLoca = "#";
  // 오른손잡이라면
  var answer = "";
  for (let number of numbers) {
    if (number == 1 || number == 4 || number == 7) {
      // 1,4,7 이면 왼쪽
      leftLoca = number;
      answer += "L";
    } else if (number == 3 || number == 6 || number == 9) {
      // 3,6,9 면 오른쪽
      rightLoca = number;
      answer += "R";
    } else {
      // 2,5,8,0 일시
      // let [row, col] = locaLine[number];
      // let [rowL, colL] = locaLine[leftLoca];
      // let [rowR, colR] = locaLine[rightLoca];

      let leftAbs =
        Math.abs(locaLine[number][0] - locaLine[leftLoca][0]) +
        Math.abs(locaLine[number][1] - locaLine[leftLoca][1]);

      let rightAbs =
        Math.abs(locaLine[number][0] - locaLine[rightLoca][0]) +
        Math.abs(locaLine[number][1] - locaLine[rightLoca][1]);

      if (leftAbs > rightAbs) {
        // 값이 크면 먼거야
        answer += "R";
        rightLoca = number;
      } else if (leftAbs < rightAbs) {
        leftLoca = number;
        answer += "L";
      } else {
        answer += hand;
        hand === "R" ? (rightLoca = number) : (leftLoca = number);
      }
    }
    // console.log("answer = " + answer);
  }
  console.log(answer);
  return answer;
}
// solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right");
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left");
// solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right");
// Math.abs(locaLine[number] - locaLine[rightLoca])

// console.log([0, 1] - [2, 0]);
