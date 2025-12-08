// https://school.programmers.co.kr/learn/courses/30/lessons/132265

function solutionFalse(topping) {
  var answer = 0;

  for (let i = 1; i < topping.length; i++) {
    const chulsoo = topping.slice(0, i);
    const brother = topping.slice(i);

    if (new Set(chulsoo).size === new Set(brother).size) answer++;
  }

  return answer;
}

function solution(topping) {
  let answer = 0;

  let cakeA = {};
  let cakeAType = 0;

  let cakeB = new Set();

  for (let i = 0; i < topping.length; i++) {
    if (cakeA[topping[i]]) {
      cakeA[topping[i]]++;
    } else {
      cakeA[topping[i]] = 1;
      cakeAType++;
    }
  }

  for (let i = 0; i < topping.length; i++) {
    cakeA[topping[i]]--;
    cakeB.add(topping[i]);

    if (!cakeA[topping[i]]) cakeAType--;

    if (cakeAType === cakeB.size) answer++;
  }
  return answer;
}

// [1, 2, 1, 3,  1, 4, 1, 2]
// topping 이라는 배열안에서
// 최대 숫자 = 토핑의 가짓수
// const slicedArray2 = array.slice(1, 4); // [2, 3, 4] (인덱스 1부터 4 전까지)
solution([1, 2, 1, 3, 1, 4, 1, 2]);
// const set = new Set([1, 3, 4, 5, 2, 2, 21, 1]);
// console.log(set.size);
// console.log(set.has(1));
