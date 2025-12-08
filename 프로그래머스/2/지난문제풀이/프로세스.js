// https://school.programmers.co.kr/learn/courses/30/lessons/42587

function solution(priorities, location) {
  var answer = 0;
  let max_value = Math.max(...priorities);
  let position = [];

  for (let i = 0; i < priorities.length; i++) {
    position.push(i);
  }

  while (priorities.length !== 0) {
    if (priorities[0] < max_value) {
      priorities.push(priorities.shift());
      position.push(position.shift());
    } else {
      answer++;
      priorities.shift();
      if (position.shift() == location) return answer;
      max_value = Math.max(...priorities);
    }
  }
}

// 그냥 뒤로 보내
solution([2, 1, 3, 2]);

// 너무어려웠다.
