// https://school.programmers.co.kr/learn/courses/30/lessons/388351?language=javascript

function solution(schedules, timelogs, startday) {
  let successCount = 0;

  let ignoreDay = [6 - startday, 7 - startday];
  if (ignoreDay[0] < 0) ignoreDay[0] = 6;

  for (let i = 0; i < schedules.length; i++) {
    // schedule 루프
    schedules[i] = schedules[i] + 10;
    // console.log(schedules);
    let getCountBool = true;
    for (let j = 0; j < 7; j++) {
      // if ((j + startday) % 7 === 6 || (j + startday) % 7 === 0) continue;
      // timelog 루프
      if (schedules[i] % 100 >= 60) schedules[i] += 40;
      // console.log(`조정된 스케줄${schedules[i]}`);
      if (
        schedules[i] < timelogs[i][j] &&
        j != ignoreDay[0] &&
        j != ignoreDay[1]
      ) {
        getCountBool = false;
        break;
      }
    }

    if (getCountBool) successCount++;
  }
  console.log(successCount);
  return successCount;
}
solution(
  [751, 855, 750, 1051, 1050],
  [
    [710, 700, 650, 735, 700, 931, 912],
    [908, 901, 805, 815, 800, 831, 835],
    [705, 701, 702, 705, 710, 710, 711],
    [707, 731, 859, 913, 934, 931, 905],
    [707, 731, 859, 913, 934, 931, 905],
    [707, 731, 859, 913, 934, 931, 905],
  ],
  7
);

// startday = 1
// 월              토 일
// 0, 1, 2, 3, 4, 5, 6,

// startday = 2
// 화 수  목  금  토 일 월
// 0, 1, 2, 3, 4, 5, 6,

// startday = 3
// 수 목  금 토 일  월  화
// 0, 1, 2, 3, 4, 5, 6,

// startday = 6
// 토  일
// 0, 1, 2, 3, 4, 5, 6

// startday = 7
// 일 월  화  수 목 금  토
// 0, 1, 2, 3, 4, 5, 6

// 6-1 하고다음거
// 6-2 하고다음거
// 6-6
/**
 * 1. 스케줄 루프
 *      1-1 타임로그 0-6 루프
 *      1-2 만약
 */
