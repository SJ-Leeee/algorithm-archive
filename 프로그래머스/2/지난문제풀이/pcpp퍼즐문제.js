// https://school.programmers.co.kr/learn/courses/30/lessons/340212
// 이분법
// 레벨을 정하는 것에 신경썼어야 함

function solution(diffs, times, limit) {
  let low = 1;
  let high = 100001;
  // diffs[i]의 최대값이 100,000
  while (low <= high) {
    let midLevel = Math.floor((low + high) / 2);

    let levelTime = helper(midLevel, diffs, times, limit);
    // console.log(`현재: ${levelTime}, 최대: ${limit}, 현재레벨:${i}`);
    if (levelTime) high = midLevel - 1;
    else low = midLevel + 1;
  }
  return low;
}

function helper(level, diffs, times, limit) {
  let sum = times[0];

  for (let i = 1; i < diffs.length; i++) {
    if (level >= diffs[i]) sum += times[i];
    else sum += (diffs[i] - level) * (times[i - 1] + times[i]) + times[i];

    if (sum > limit) return false;
  }

  return true;
}

console.log(solution([1, 5, 3], [2, 4, 7], 30));
console.log(solution([1, 4, 4, 2], [6, 3, 8, 2], 59));
console.log(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723));
console.log(
  solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)
);
/**
 * diff에는 각 레벨의 난이도가 들어있다.
 * times는 해결하는 시간이 담겨있다.
 * limit은 합치면 된다.
 *
 * 1. 숙련도를 정한다.
 * 2. 숙련도에 따라
 *
 *
 *
 * [1, 328, 467, 209, 54]	[2, 7, 1, 4, 3]	1723	294
 * // 295일 때,
 * 1. 2의 시간을 사용 = 2
 * 2. (328 - 295) * (7-2) + 7 을 사용 =172
 * 3. 467-295 * 8 + 1 = 1377
 * 4. 4의 시간
 * 5. 3의 시간
 * // 1580대
 */
