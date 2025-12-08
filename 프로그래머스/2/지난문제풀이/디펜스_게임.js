// https://school.programmers.co.kr/learn/courses/30/lessons/142085

// function solution(n, k, enemy) {
//   if (k >= enemy.length) return enemy.length;
//   // 무적권이 많으면 바로 퇴출
//   let round = 0;
//   let canEnemy = [];
//   for (let i = 0; i < enemy.length; i++) {
//     canEnemy.push(enemy[i]);
//     // 현재꺼 넣었다.
//     if (n >= enemy[i]) {
//       // 현재거보다 내게 더 크면
//       n -= enemy[i];
//       // 내거에서 지금을 빼
//       round++;
//       // 그리고 라운드 추가
//       continue;
//     } else if (k) {
//       // 현재거가 커 그리고 무적권이 있어
//       let big = canEnemy.sort((a, b) => b - a).shift();
//       n = big >= enemy[i] ? n + big : n + enemy[i];
//       // 있던놈이 크던 현재놈이 크던
//       k--;
//       n -= enemy[i];
//       // 현재 애를 빼준다
//       round++;
//       continue;
//     } else {
//       console.log(`3`);
//       break;
//     }
//   }

//   return round;
// }
// solution(100, 2, [10, 10, 10, 10, 1000, 1000, 10, 1000]);

// 그냥 내 라운드에 일단 무적권 써
// 그리고 다음놈이 커 그럼 무적권 취소하고 얘한테 무적권써 그럼무조건 한놈한테만 쓰잖아

// 5 2 [99,2,99]

// 힙
class MinHeap {
  constructor() {
    this.heap = [];
  }

  getLeftChildIndex(parentIndex) {
    return 2 * parentIndex + 1;
  }

  getRightChildIndex(parentIndex) {
    return 2 * parentIndex + 2;
  }

  getParentIndex(childIndex) {
    return Math.floor((childIndex - 1) / 2);
  }

  swap(index1, index2) {
    const temp = this.heap[index1];
    this.heap[index1] = this.heap[index2];
    this.heap[index2] = temp;
  }

  peek() {
    return this.heap[0];
  }

  insert(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = this.getParentIndex(index);
      if (this.heap[parentIndex] <= this.heap[index]) {
        break;
      }
      this.swap(parentIndex, index);
      index = parentIndex;
    }
  }

  remove() {
    if (this.heap.length === 0) {
      return null;
    }
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return value;
  }

  heapifyDown() {
    let index = 0;
    while (this.getLeftChildIndex(index) < this.heap.length) {
      const leftChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);
      const smallerChildIndex = rightChildIndex < this.heap.length && this.heap[rightChildIndex] < this.heap[leftChildIndex] ? rightChildIndex : leftChildIndex;
      if (this.heap[index] <= this.heap[smallerChildIndex]) {
        break;
      }
      this.swap(index, smallerChildIndex);
      index = smallerChildIndex;
    }
  }
}

function solution(n, k, enemy) {
  var answer = 0;
  const minHeap = new MinHeap();

  return answer;
}
// 테스트
