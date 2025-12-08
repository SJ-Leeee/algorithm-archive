//https://school.programmers.co.kr/learn/courses/30/lessons/42626

function solution(scoville, K) {
  scoville.sort((a, b) => a - b);

  let count = 0;
  while (Math.min(...scoville) < K) {
    count++;
    let a = scoville.shift();
    let b = scoville.shift();
    let c = a + b * 2;
    scoville.push(c);
    scoville.sort((a, b) => a - b);
  }

  return count;
}

solution([1, 2, 3, 9, 10, 12], 7);
// [1, 2, 3, 9, 10, 12]	7	2
