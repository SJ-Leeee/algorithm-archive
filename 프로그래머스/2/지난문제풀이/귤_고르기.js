// https://school.programmers.co.kr/learn/courses/30/lessons/138476
function solution(k, tangerine) {
  let tangerineObj = {};
  let answer = 0;
  for (num of tangerine) {
    if (tangerineObj[num]) tangerineObj[num]++;
    else tangerineObj[num] = 1;
  }

  let a = Object.values(tangerineObj).sort((a, b) => b - a);
  for (let i = 0; i < a.length; i++) {
    k -= a[i];
    answer++;
    if (k <= 0) break;
  }
  return answer;
}

let test = solution(2, [1, 1, 1, 1, 2, 2, 2, 3]);
console.log(test);
// k는 내가 팔고싶은 개수, targerine 귤 크기의 배열
// 귤배열을
