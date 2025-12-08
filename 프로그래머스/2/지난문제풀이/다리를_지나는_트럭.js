// https://school.programmers.co.kr/learn/courses/30/lessons/42583

// function solution(bridge_length, weight, truck_weights) {
//   let inBridgeArr = [];
//   let inBridgeKg = 0;
//   let downTime = [];
//   let seconds = 0;
//   while (truck_weights.length > 0) {
//     if (inBridgeKg <= weight) {
//       // 다리의 무게가 적다면
//       seconds = seconds + 1;

//       let inTruck = truck_weights.shift();
//       // 앞트럭
//       inBridgeArr.push(inTruck);
//       // 다리에 올려
//       inBridgeKg += inTruck;
//       // 다리 무게 증가
//       downTime.push(seconds + bridge_length);
//       console.log(`무게가 적다면 ${seconds}`);
//       console.log(downTime);
//       // 내려오는 시간
//     } else {
//       // 다리에 무게가 꽉 찼다면
//       let outTruck = inBridgeArr[0];
//       // 다리에 올라간 맨 앞 트럭
//       while (inBridgeKg - outTruck > weight) {
//         // 맨앞트럭을 뺀값조차 무게보다 크다
//         inBridgeKg -= inBridgeArr.shift();
//         // 전체무게에서 나간거
//         outTruck = inBridgeArr[0];
//         // 맨 앞트럭을 삭제하고 새로운 맨 앞 트럭 할당
//         downTime.shift();
//         // 나간트럭의 나간 시각
//       }
//       let outTruck2 = inBridgeArr.shift();
//       inBridgeKg -= outTruck2;
//       // 나간트럭
//       seconds = downTime.shift();
//       downTime.push(seconds + bridge_length);
//       console.log(`무게가 많다면 ${seconds}`);
//       console.log(downTime);
//       let inTruck = truck_weights.shift();
//       inBridgeArr.push(inTruck);
//     }
//   }
// }
// 올라간 시간 [1,2,5,6,7,10]
// 내려간 시간 [5,6,9,10,11,14]

// solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]);

// bridge_length	weight	truck_weights	                    return
// 4	            15	    [7,4,5,6,4,11]	                        8
// 올라간 시간 [1,2,5,6,7,10]
// 내려간 시간 [5,6,9,10,11,14]
// 내 로직     [1,2,6,7,11,15]

// 100	            100	    [10]	                            101
// 100	            100	    [10,10,10,10,10,10,10,10,10,10]	    110
// [1,2,3,4,5,6,7,8,9,10]
// 3                20      [7,4,10,3,16]
// 올라간 시간 [1,2,4,5,7]
// 내려간 시간 [4,5,7,8,10]

// 올라오는 시간? 과 브릿지길이
// 3초에 나오며 올라와
// 3초 4초 6초
// 얘는 101초에 나오며 올라와

// let nextTruck = truck_weights[0];
//     if (inBridgeKg + nextTruck <= weight) {
//       second += 1;
//       upTime.push(second);
//       let inTruck = truck_weights.shift();
//       inBridgeArr.push(inTruck);
//       inBridgeKg += inTruck;
//     } else {
//       let outTruck = inBridgeArr.shift();
//       inBridgeKg -= outTruck;

//       second += bridge_length;
//       upTime.push(second);
//       let inTruck = truck_weights.shift();
//       inBridgeArr.push(inTruck);
//     }

//  let nextTruck = truck_weights[0];
//   if (inBridgeKg + nextTruck <= weight) {
//     second += 1;
//     upTime.push(second);
//     downTime.push(second + bridge_length);

//     let inTruck = truck_weights.shift();
//     // 트럭을 자르고
//     inBridgeArr.push(inTruck);
//     // 다리에 올리고
//     inBridgeKg += inTruck;
//     // 무게를 더하고
//   } else {
//     //두마리 다 나가야될수도있어
//     upTime.shift();
//     downTime.shift();

//     let outTruck = inBridgeArr.shift();
//     inBridgeKg -= outTruck;

//     second += bridge_length;
//     upTime.push(second);
//     let inTruck = truck_weights.shift();
//     inBridgeArr.push(inTruck);
//   }
// }

// 장렬히 패배

function solution(bridge_length, weight, truck_weights) {
  var timer = 0;
  let weightInBridge = 0;

  let inbridge = [];
  let upTime = [];

  for (truck of truck_weights) {
    // 모든트럭이 지나가야하기 때문에
    if (weight >= weightInBridge + truck) {
      // 만약 트럭이 들어갈 수 있다면
      timer++;
      // 현재시간에서 1추가하고
      weightInBridge += truck;
      // 다리에 올리고
      inbridge.push(truck);
      // 다리배열 추가
      upTime.push(timer);
      // 시간배열 추가 [4]
    } else {
      // 만약 그럴 수 없다면
      let byetruck;
      let byetruckTime;
      while (weight < weightInBridge + truck) {
        // weight이 될때까지
        byetruck = inbridge.shift();
        // 제일앞에 자르고
        byetruckTime = upTime.shift();
        // 제일 앞 uptime 자르고 1 이겠지

        weightInBridge -= byetruck;
        // 무게에서 빼줘
      }
      let newTimer = byetruckTime + bridge_length;
      if (upTime[upTime.length - 1] >= newTimer) newTimer = upTime[upTime.length - 1] + 1;

      timer = newTimer;

      weightInBridge += truck;
      inbridge.push(truck);
      // 이트럭은
      upTime.push(timer);
      // 3에 올라간거야
    }
  }

  let last = upTime.pop();
  console.log(last + bridge_length);
  return last + bridge_length;
}
solution(10, 100, [50, 30, 10, 10, 30, 10, 40]);

// up down
// 1  11  참 [1]    총 무게: 50
// 2  12  참 [1, 2]   총 무게: 80
// 3  13  참 [1, 2, 3]    총 무게: 90
// 4  14  참 [1, 2, 3, 4]   총 무게: 100
// 11 21  거짓 [2, 3, 4, 11]  총 무게: 80
// 12 22  참 [2, 3, 4, 11, 12]  총 무게: 90
// 12 22  거짓 [4, 11, 12, 13]  총 무게: 100

// up down
// 1  101
// 2  102
// ...
// 10 110

// 다리길이만큼 시간이 걸린다
// weight이 딸리면 올리면 안된다
