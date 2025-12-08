//https://school.programmers.co.kr/learn/courses/30/lessons/42576

function solution(participant, completion) {
  const comSet = new Set(completion);
  const participantObj = {};

  participant.forEach((i) => {
    const elemant = i;
    if (participantObj[elemant]) {
      participantObj[elemant] += 1;
    } else {
      participantObj[elemant] = 1;
    }
  });

  completion.forEach((people) => {
    if (comSet.has(people)) {
      participantObj[people] -= 1;
    }
  });

  for (const key in participantObj) {
    if (participantObj[key] !== 0) return key;
  }
}

console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]));

// 동명이인 문제

//

function solution2(participant, completion) {
  const comSet = new Set(completion);

  participant = participant.filter((participantName) => {
    if (comSet.has(participantName)) {
      comSet.delete(participantName);
      return false;
    } else {
      return true;
    }
  });
  return participant[0];
}
