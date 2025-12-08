// https://school.programmers.co.kr/learn/courses/30/lessons/42885

function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => a - b);
  let start = 0;
  let end = people.length - 1;
  while (end >= start) {
    if (people[end] + people[start] <= limit) {
      start++;
      end--;
    } else {
      end--;
    }
    answer++;
  }
  return answer;
}

solution([50, 70, 80], 100);
// [70, 50, 80, 50]	 limit 100
