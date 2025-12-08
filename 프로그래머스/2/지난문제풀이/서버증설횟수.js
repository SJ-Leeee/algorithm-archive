// 당신은 온라인 게임을 운영하고 있습니다. 같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가로 필요합니다.
// 어느 시간대의 이용자가 m명 미만이라면, 서버 증설이 필요하지 않습니다. 어느 시간대의 이용자가 n x m명 이상 (n + 1) x m명 미만이라면
// 최소 n대의 증설된 서버가 운영 중이어야 합니다.
// 한 번 증설한 서버는 k시간 동안 운영하고 그 이후에는 반납합니다. 예를 들어, k = 5 일 때 10시에 증설한 서버는 10 ~ 15시에만 운영됩니다.

// 하루 동안 모든 게임 이용자가 게임을 하기 위해 서버를 최소 몇 번 증설해야 하는지 알고 싶습니다. 같은 시간대에 서버를 x대증설했다면 해당 시간대의 증설 횟수는 x회입니다.

// 본인의 서버 수를 기억할 변수 a

function solution(players, m, k) {
  let count = 0;
  const myServer = {};
  for (let i = 0; i < 24; i++) {
    myServer[i] = 0;
  }

  for (let i = 0; i < players.length; i++) {
    let needServer = Math.floor(players[i] / m) - myServer[i];
    if (needServer > 0) {
      count += needServer;
      for (let j = 1; j < k; j++) {
        // 추가서버저장
        myServer[i + j] += needServer;
      }
    }
  }
  return count;
}

solution(
  [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
  1,
  1
);
