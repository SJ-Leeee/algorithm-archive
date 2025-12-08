const charRegex = /^[SDT]+$/;
const bonusRegex = /^[*#]+$/;

function sdt(char, num) {
    num = Number(num)
    if (char === 'S') {
        num = num ** 1
    }
    if (char === 'D') {
        num = num ** 2

    }
    if (char === 'T') {
        num = num ** 3

    }
    return num
}

function solution(dartChar) {
    const queue = []
    let preChar = -1
    for (let i = 1; i < dartChar.length; i++) {
        if (charRegex.test(dartChar[i]) || bonusRegex.test(dartChar[i])) {
            // 문자일때만 실행되는 로직
            let number;
            if (preChar !== i) {
                // 숫자가 나왔을 때만 실행되는 로직
                number = dartChar.slice(preChar + 1, i)
                if (charRegex.test(dartChar[i])) {
                    queue.push(sdt(dartChar[i], number))
                } else if (dartChar[i] === '*') {
                    if (queue.length > 1) {
                        queue[queue.length - 1] *= 2
                        queue[queue.length - 2] *= 2
                    } else queue[queue.length - 1] *= 2
                } else if (dartChar[i] === '#') {
                    queue[queue.length - 1] = -queue[queue.length - 1]
                }
            }
            preChar = i
        }
    }
    // 1. 숫자를 뽑아낸다.
    // 1-1 10일 경우가 있어. 가장 최근 문자와 현재까지를 분리한다.
    // 2. SDT 일 경우 계산하여 큐에 적재한다.
    // 3. *# 일경우 가장 최근, 최근 전 숫자를 조작한다.

    var answer = 0;
    answer = queue.reduce((acc, cur) => acc + cur, 0)
    return answer;
}

solution('1S2D*3T')
solution('1D2S#10S')
solution('1D2S0T')
solution('1S*2T*3S')
solution('1D#2S*3S')
solution('1T2D3D#')
solution('1D2S3T*')
