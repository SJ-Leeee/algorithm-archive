// https://school.programmers.co.kr/learn/courses/30/lessons/42883

function solution(number, k) {

    let numArr = number.split('').map((i) => Number(i))

    let firstNum = 0
    let firstNumIdx = 0
    for (let i = 0; i <= k; i++) {
        if (numArr[i] > firstNum) {
            firstNum = numArr[i]
            firstNumIdx = i
        }
    }

    k -= firstNumIdx
    let step1 = numArr.slice(firstNumIdx)

    if (k == 0) return String(step1.join(''))
    let previousNum;
    for (let i = 1; i < step1.length - 1; i++) {
        if (k > 0) {
            // k가 0 이상이고
            let pre = step1[i - 1] === false ? previousNum : step1[i - 1]
            if (pre > step1[i] && step1[i + 1] > step1[i]) {
                // 앞보다 작으면
                previousNum = step1[i]
                step1[i] = false
                k--
            } else if (step1[i] === 0) {
                previousNum = step1[i]
                step1[i] = false
                k--
            }
        }
    }

    let step2 = String(step1.filter(element => element !== false).join(''))

    if (k > 0) step2 = step2.slice(0, step2.length - k);

    return step2;
}


function solution2(number, k) {

    let numArr = number.split('').map((i) => Number(i))
    let firstNum = 0
    let firstNumIdx = 0
    for (let i = 0; i <= k; i++) {
        if (numArr[i] > firstNum) {
            firstNum = numArr[i]
            firstNumIdx = i
        }
    }

    k -= firstNumIdx
    let step1 = numArr.slice(firstNumIdx)

    console.log(step1)
    let previousNum;
    for (let i = 1; i < step1.length - 1; i++) {
        if (k > 0) {
            // k가 0 이상이고
            let pre = step1[i - 1] === false ? previousNum : step1[i - 1]
            if (pre > step1[i] && step1[i + 1] > step1[i]) {
                // 앞보다 작으면
                previousNum = step1[i]
                step1[i] = false
                k--
            } else if (step1[i] === 0) {
                previousNum = step1[i]
                step1[i] = false
                k--
            }
        }
    }

    let step2 = String(step1.filter(element => element !== false).join(''))
    if (k > 0) step2 = step2.slice(0, step2.length - k);
    console.log(step2)

    return step2;
}

// 1. 일단 앞은 제일 큰 게 좋다.
// 2. 앞에서부터 자를것+1 까지 제일큰것이 앞에다.
// 3. 내기준으로 앞에있는것보다작고 뒤에있는것보다 작으면 탈락
// 4. k가 남으면 뒤에서부터 아웃

// solution2('190000002', 3)

solution2('654312', 2)
// 9298
// 9f9f
// 99

// solution("720378", 2)
//     ("928857", 3); //988
// ("99991", 3); // 99
// ("10001", 3); // 11













// else if (step1[i - 1] === false && step1[i + 1] > step1[i]) {
//     // 앞이 false면
//     step1[i] = false
//     k--
// }
// } else if (step1[i] === 0) {
//     step1[i] = false
//     k--
// }