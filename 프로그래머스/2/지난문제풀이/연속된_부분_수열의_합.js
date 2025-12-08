// https://school.programmers.co.kr/learn/courses/30/lessons/178870
function solution(sequence, k) {
  let answerArr = [];

  let plusIdx = 0;
  while (sequence.length !== 0) {
    let sum = 0;
    for (let i = 0; i < sequence.length; i++) {
      let idx = [];
      idx.push(plusIdx);

      sum += sequence[i];
      if (sum === k) {
        idx.push(i + plusIdx);
        answerArr.push(idx);
        plusIdx++;
        break;
      }

      if (sum > k) {
        plusIdx++;
        break;
      }
    }
    sequence.shift();
  }
  let bestIdx = 0;
  let previousSub = 100;
  answerArr.forEach((i, idx) => {
    if (previousSub > i[1] - i[0]) {
      previousSub = i[1] - i[0];
      bestIdx = idx;
    }
  });

  return answerArr[bestIdx];
}

let sequence = [2, 2, 2, 2, 2];
let k = 6;
let answer = [2, 3];
solution(sequence, k);
