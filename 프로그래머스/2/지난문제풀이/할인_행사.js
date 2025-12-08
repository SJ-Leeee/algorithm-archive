// https://school.programmers.co.kr/learn/courses/30/lessons/131127

function solution(want, number, discount) {
    let answer = 0

    let wantDict = {}
    // dict만들기
    for (let i = 0; i < want.length; i++) {
        wantDict[want[i]] = number[i]
    }

    // 들어온 것을 기억하는 queue
    let checkQueue = []

    // discout순회
    for (let i = 0; i < discount.length; i++) {

        checkQueue.push(discount[i])
        if (discount[i] in wantDict) wantDict[discount[i]] -= 1

        // queue의 길이가 10이라면 검증
        if (checkQueue.length === 10) {
            // console.log(wantDict)
            let wantDictValues = Object.values(wantDict).filter((i) => i !== 0)
            if (wantDictValues.length === 0) answer++
            let outItem = checkQueue.shift()
            if (outItem in wantDict) wantDict[outItem] += 1
        }
    }

    return answer;
}

solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])

// dict를 만들고
// for문을 돌리면서
// object.keys가 0이 아닌게 있으면 카운팅하지 않고,