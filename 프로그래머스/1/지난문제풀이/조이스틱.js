// https://school.programmers.co.kr/learn/courses/30/lessons/42860


function findLongestASequence(s) {
    let maxLength = 0; // 최대 'A' 연속 길이
    let maxStartIndex = -1; // 최대 'A' 연속 구간의 시작 인덱스
    let maxEndIndex = -1; // 최대 'A' 연속 구간의 끝 인덱스

    let currentStartIndex = -1; // 현재 'A' 연속 구간의 시작 인덱스
    let currentLength = 0; // 현재 'A' 연속 길이

    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'A') {
            if (currentLength === 0) {
                currentStartIndex = i; // 새로운 'A' 구간의 시작
            }
            currentLength++;
        } else {
            if (currentLength > maxLength) {
                maxLength = currentLength;
                maxStartIndex = currentStartIndex;
                maxEndIndex = i - 1;
            }
            currentLength = 0; // 'A' 구간이 끝났으므로 초기화
        }
    }

    // 마지막 구간이 최대일 수도 있으므로 체크
    if (currentLength > maxLength) {
        maxLength = currentLength;
        maxStartIndex = currentStartIndex;
        maxEndIndex = s.length - 1;
    }

    return [maxStartIndex - 1, maxEndIndex + 1];
}

function solution(name) {
    let answer = 0
    const alphabat = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    const dict = {}
    const nameArr = name.split('').map(String)

    // dict 만들기
    for (let i = 0; i < alphabat.length; i++) dict[alphabat[i]] = i

    // 알파벳만들기
    for (let i = 0; i < nameArr.length; i++) {
        let test = Math.min(dict[nameArr[i]], 26 - dict[nameArr[i]])
        answer += test
    }

    // console.log(answer)
    // new
    const firstAndLast = Array.from(name).map(char => char === 'A');
    if (firstAndLast.indexOf(false) === -1) return 0
    firstAndLast[0] = true
    let notAFromStart = firstAndLast.indexOf(false)
    let notAFromEnd = firstAndLast.lastIndexOf(false)

    const [start, end] = findLongestASequence(name);

    let forward = 1000000
    let reverse = 1000000
    let forRev = 1000000
    let revFor = 1000000

    forward = notAFromEnd
    reverse = name.length - notAFromStart

    if (start >= 0) {
        forRev = start + start + name.length - end
        revFor = name.length - end + name.length - end + start
    }

    const moveCnt = Math.min(forward, reverse, forRev, revFor)


    console.log(answer + moveCnt)

    return answer + moveCnt;
}

solution('BAAAAABAA')
solution('BBBABAABABABB')
solution('BBABAAAAAAB')
solution('BABBAABB')
solution('BBAAAAAAABAB')
solution('BAABBAAA')
solution('ABBAAABAAAABB')
solution('AAAAAAAAAAAAAAAAA')
// solution('BAABAABAABAAB')

// 그럼 가장 긴 A를 구하고
// 마지막 false 위치를 구하고
// 시작 false 위치를 구하고
// 가장 긴 AA 가 시작이라면 정, 역만 하자

// 정 = 마지막 false idx
// 역 = length - 첫번째 false idx
// 정+역 = [시작 idx] + [시작 idx + length - 끝 index]
// 역+정 = [length - 끝 index] + [length - 끝 index] + 시작 index
// solution('AABBAABBB')