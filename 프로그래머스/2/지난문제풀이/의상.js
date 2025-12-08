//https://school.programmers.co.kr/learn/courses/30/lessons/42578

function solution(clothes) {
  var answer = 0;
  const clothesObj = {};
  clothes.forEach((i) => {
    const elemant = i[1];
    if (clothesObj[elemant]) {
      clothesObj[elemant] += 1;
    } else {
      clothesObj[elemant] = 1;
    }
  });
  const numberOfClothes = Object.values(clothesObj);
  const typeClothes = numberOfClothes.length;
  for (let i = typeClothes; i > 0; i--) {
    answer += allCases(numberOfClothes, i);
  }
  return answer;
}

function allCases(arr, k) {
  if (k == 1) {
    let kequl1 = 0;
    for (let i = 0; i < arr.length; i++) {
      kequl1 += arr[i];
    }
    return kequl1;
  }
  let 값 = 0;
  function backtrack(currentCombo, start) {
    if (currentCombo.length === k) {
      let product = 1;
      for (let i = 0; i < currentCombo.length; i++) {
        product *= currentCombo[i];
      }
      값 += product;
      return;
    }

    for (let i = start; i < arr.length; i++) {
      currentCombo.push(arr[i]);
      backtrack(currentCombo, i + 1);
      currentCombo.pop();
    }
  }
  backtrack([], 0);
  return 값;
}
console.log(
  solution([
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
  ])
);
// 그냥 안입는것까지 고려했으면 됨, 조합을 사용할 필요없이

function solution(clothes) {
  const clothesObj = {};

  // 의상 종류별로 의상 수를 세기
  for (const item of clothes) {
    const category = item[1];
    if (clothesObj[category]) {
      clothesObj[category]++;
    } else {
      clothesObj[category] = 1;
    }
  }

  let totalCombinations = 1;

  // 각 종류별 의상을 입는 경우와 입지 않는 경우를 고려하여 조합 계산
  for (const category in clothesObj) {
    totalCombinations *= clothesObj[category] + 1; // 해당 종류의 의상을 입지 않는 경우도 고려
  }

  // 아무것도 입지 않는 경우 하나를 빼줌
  totalCombinations--;

  return totalCombinations;
}

// 예시 입력
const clothes = [
  ["얼굴", "동그란 안경"],
  ["상의", "파란색 티셔츠"],
  ["하의", "청바지"],
  ["겉옷", "긴 코트"],
];

console.log(solution(clothes)); // 예상 결과: 10
// 입지 않
