// https://school.programmers.co.kr/learn/courses/30/lessons/135807

// 공약수 처리함수
function commonDiv(array) {
  // array는 0일 수 없다.
  let div = [];
  let min = array.sort((a, b) => a - b)[0];
  let startDiv = 1;

  let isDivisible = true; // 초기값을 true로 설정

  // 1, 2
  while (startDiv <= min) {
    ++startDiv;
    isDivisible = true;
    for (let i = 0; i < array.length; i++) {
      if (array[i] % startDiv !== 0) {
        isDivisible = false;
        break;
      }
    }
    if (isDivisible === true) div.push(startDiv);
  }

  return div;
}

function check(array, common) {
  let isDivisible;
  for (let i = common.length - 1; i >= 0; i--) {
    isDivisible = false;
    for (let j = 0; j < array.length; j++) {
      if (array[j] % common[i] === 0) isDivisible = true;
    }
    if (isDivisible === false) return common[i];
  }
  return 0;
}

// console.log(check([13, 15, 17], [5, 6, 13]));

function solution(arrayA, arrayB) {
  const commonA = commonDiv(arrayA);
  const answerA = check(arrayB, commonA);
  const commonB = commonDiv(arrayB);
  if (Math.max(commonB) <= answerA) return answerA;

  const answerB = check(arrayA, commonB);
  return answerA >= answerB ? answerA : answerB;

  //   const commonB = commonDiv(arrayB);
  //   var answer = 0;
  //   return answer;
}

// 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
// 영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고, 철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a

// 즉... 둘의 공약수를 나열하고, 그 공약수로 상대것이 안나눠지면 리턴

// 공약수란..

// 2,3,6
// 6이 되면 다 되는거야
// 6이 안되면 3은 될수 있지

// 21, 27

// Math.min 은 런타임오류발생할수있따.
