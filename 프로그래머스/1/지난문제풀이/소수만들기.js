/*
 * https://school.programmers.co.kr/learn/courses/30/lessons/12977
 *
 * 홀홀홀, 홀짝짝
 *
 */

function solution(nums) {
  var answer = 0;
  nums = nums.sort((a, b) => a - b);
  let odd = [];
  let even = [];
  for (let num of nums) {
    if (num % 2 == 0) even.push(num);
    else odd.push(num);
  }

  let sumMemory = {};

  let sum = 0;
  if (odd.length > 2) {
    for (let i = 0; i < odd.length - 2; i++) {
      for (let j = i + 1; j < odd.length - 1; j++) {
        for (let l = j + 1; l < odd.length; l++) {
          sum = odd[i] + odd[j] + odd[l];

          if (sumMemory[sum] || isPrime(sum)) {
            // 소수가 맞아야 들어가겠지
            answer++;
            sumMemory[sum] = true;
          }
        }
      }
    }
  }

  if (even.length > 1) {
    for (let i = 0; i < even.length - 1; i++) {
      for (let j = i + 1; j < even.length; j++) {
        for (let l = 0; l < odd.length; l++) {
          sum = even[i] + even[j] + odd[l];
          if (sumMemory[sum] || isPrime(sum)) {
            // 소수가 맞아야 들어가겠지
            answer++;
            sumMemory[sum] = true;
          }
        }
      }
    }
  }

  return answer;
}

function isPrime(num) {
  // 소수만들기코드
  if (num <= 1) return false;
  if (num <= 3) return true; // 2와 3은 소수

  if (num % 2 === 0 || num % 3 === 0) return false; // 2나 3의 배수는 소수가 아님

  // 5부터 시작해 6의 배수 ± 1인 숫자만 확인
  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) {
      return false;
    }
  }

  return true;
}

solution([1, 2, 7, 6, 4]);

function solution2(nums) {
  var answer = 0;
  nums = nums.sort((a, b) => a - b);

  let sumMemory = {};
  let sum = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let l = j + 1; l < nums.length; l++) {
        sum = nums[i] + nums[j] + nums[l];

        if (sumMemory[sum] || isPrime(sum)) {
          // 소수가 맞아야 들어가겠지
          answer++;
          sumMemory[sum] = true;
        }
      }
    }
  }

  return answer;
}
