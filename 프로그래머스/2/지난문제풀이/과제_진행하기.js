// https://school.programmers.co.kr/learn/courses/30/lessons/176962\

function solution(plans) {
  const newPlans = plans.map(([name, start, playtime]) => {
    const [hour, minute] = start.split(":").map((str) => Number(str));
    const time = hour * 60 + minute;
    const N_playTime = Number(playtime);
    return { name, start: time, playtime: N_playTime };
  });
  const stack = [];
  const done = [];
  let idx = 0;
  newPlans.sort((a, b) => a.start - b.start);

  // 핵심 : 시간이 되면 스택에 넣는다. for문을 시간순서대로 돌린다.

  for (let i = 0; i < 1440; i++) {
    if (stack.length !== 0) {
      const playSub = stack[stack.length - 1];
      playSub.playtime--;
      if (playSub.playtime === 0) {
        done.push(playSub.name);
        stack.pop();
      }
    }

    if (i === newPlans[idx]?.start) {
      stack.push(newPlans[idx]);
      idx++;
    }
  }

  const unfinished = stack.reverse().map(({ name }) => name);
  return [...done, ...unfinished];
}
// push pop 이용
solution([
  ["science", "12:40", "50"],
  ["music", "12:20", "40"],
  ["history", "14:00", "30"],
  ["computer", "12:30", "100"],
]);

solution([
  ["korean", "11:40", "30"],
  ["english", "12:10", "20"],
  ["math", "12:30", "40"],
]);

solution([
  ["aaa", "12:00", "20"],
  ["bbb", "12:10", "30"],
  ["ccc", "12:40", "10"],
]);
// [("science", "history", "computer", "music")];

// for (let i = 0; i < plans.length - 1; i++) {
//     let canTime = plans[i + 1][1] - plans[i][1];
//     // 여유시간
//     if (plans[i][2] === canTime) {
//       // 만약 시간이 딱 맞는다면
//       answer.push(plans[i][0]);
//     } else if (plans[i][2] > canTime) {
//       // 만약 시간이 모자르다면
//       let remainTime = plans[i][2] - canTime;
//       queue.push({ [plans[i][0]]: remainTime });
//     } else {
//       // 시간이 남는다면
//       let restTime = canTime - plans[i][2];
//       let sub = queue.pop();
//     }
//   }
