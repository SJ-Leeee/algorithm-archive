// https://school.programmers.co.kr/learn/courses/30/lessons/12940
function maxDiv(max, min) {
  let div = min;

  for (let i = div; i > 0; i--) {
    if (max % i === 0 && min % i === 0) return i;
  }

  return 1;
}

function minMul(max, min) {
  if (max % min === 0) return max;

  const mD = maxDiv(max, min);

  return (max * min) / mD;
}

function solution(n, m) {
  const max = Math.max(n, m);
  const min = Math.min(n, m);

  return [maxDiv(max, min), minMul(max, min)];
}

// 100 150

// 15000 / 50 == 300
