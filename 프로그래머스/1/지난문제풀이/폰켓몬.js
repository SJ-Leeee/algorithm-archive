// https://school.programmers.co.kr/learn/courses/30/lessons/1845

function solution(nums) {
  const uniqueArr = [...new Set(nums)];
  if (uniqueArr.length >= nums.length / 2) return Math.floor(nums.length / 2);
  else return uniqueArr.length;
}

// console.log(solution([1, 2, 3, 3, 3, 3, 3, 3]));
