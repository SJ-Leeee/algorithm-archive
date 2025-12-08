// https://school.programmers.co.kr/learn/courses/30/lessons/12909
function solution(s) {
  const stack = [];

  for (let i of s) {
    if (i === "(") {
      // '(' 라면 ')' 를 push
      stack.push(")");
    } else {
      // ')' 라면
      if (stack.length === 0 || stack.pop() !== ")") return false;
    }
  }

  return stack.length === 0 ? true : false;
}

let a = solution("((()()))");
console.log(a);
// 1. stack 구조 이용 LIFO
// 2. O(n)
