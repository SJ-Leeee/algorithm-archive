// https://school.programmers.co.kr/learn/courses/30/lessons/148653

function solution(storey) {
  var answer = 0;

  let numArr = Array.from(String(storey), Number).reverse();
  // 1의 자리부터 나오게
  for (let i = 0; i < numArr.length - 1; i++) {
    // lastIndex 제외하고
    if (numArr[i] === 5) {
      if (numArr[i + 1] >= 5) {
        answer += 5;
        numArr[i + 1]++;
      } else {
        answer += 5;
      }
    } else if (numArr[i] > 5) {
      answer += 10 - numArr[i];
      numArr[i + 1]++;
    } else if (numArr[i] <= 5) {
      answer += numArr[i];
    }
  }
  const lastIdx = numArr[numArr.length - 1];
  answer += lastIdx > 5 ? 11 - lastIdx : lastIdx;

  return answer;
}

solution(2554);

// 내자리가 5보다 크면 무조건 올려주는게 좋아
// 내자리가 5라면 앞에있는애들을 봐야돼
// 내자리가 5보다 작으면 무조건 빼주는게 좋아

// 46
//
//

// 55
// 10
// 10

// 65
//
