// https://school.programmers.co.kr/learn/courses/30/lessons/42747

function solution(citations) {
  citations.sort((a, b) => a - b);

  let a = citations.length;

  citations.forEach((i) => {
    if (a <= i) return;
    else a--;
  });
  return a;
}

solution([9, 7, 6, 2, 1]);
// 9, 7, 6, 2, 1개의 인용이 있는 5개의 출판물을 가지고 있는
// 경우(가장 큰 것부터 작은 것 순으로) 저자의 h-index는 3입니다. 왜냐하면 저자가 3개 이상의 인용이 있는 3개의 출판물을 가지고 있기 때문 입니다
// 그러나 저자는 4회 이상 인용된 4편의 저작물을 보유하고 있지 않습니다 .
