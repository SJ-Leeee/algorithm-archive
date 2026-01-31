const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  HeadingLevel,
  BorderStyle,
  WidthType,
  ShadingType,
  AlignmentType,
  LevelFormat,
  PageBreak,
} = require("docx");
const fs = require("fs");

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

const categories = [
  {
    title: "1. 구현/시뮬레이션",
    concept:
      "문제에서 요구하는 대로 정확히 구현. 격자 이동, 조건 분기, 상태 관리가 핵심.",
    keyPoints: [
      "dx, dy 방향 배열: [(0,1), (1,0), (0,-1), (-1,0)]",
      "범위 체크: 0 <= nx < N and 0 <= ny < M",
      "상태 관리: visited, 현재 위치, 방향 등",
    ],
    template: `dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(4):
nx, ny = x + dx[i], y + dy[i]
if 0 <= nx < N and 0 <= ny < M:
    # 처리`,
    problems: [
      "3190_뱀.py - 방향전환 + 큐로 뱀 몸통 관리",
      "1065_한수.py - 조건에 맞는 수 카운팅",
    ],
  },
  {
    title: "2. BFS/DFS",
    concept:
      "그래프 탐색의 기본. BFS는 최단거리 보장(무가중치), DFS는 경로 탐색/백트래킹에 활용.",
    keyPoints: [
      "BFS: deque 사용, 방문 체크는 큐에 넣을 때",
      "DFS: 재귀 or 스택, 방문 체크는 함수 진입 시",
      "연결 요소: 모든 노드에서 탐색 시작 시도",
    ],
    template: `# BFS
from collections import deque
def bfs(start):
dq = deque([start])
visited = {start}
while dq:
    cur = dq.popleft()
    for next in graph[cur]:
        if next not in visited:
            visited.add(next)
            dq.append(next)

# DFS (재귀)
def dfs(node, visited):
visited.add(node)
for next in graph[node]:
    if next not in visited:
        dfs(next, visited)`,
    problems: [
      "2178_미로탐색.py - BFS 최단거리",
      "1260_DFS와BFS.py - 기본 탐색 구현",
    ],
  },
  {
    title: "3. DP (동적 프로그래밍)",
    concept: "중복 부분 문제를 메모이제이션으로 해결. 점화식 세우기가 핵심.",
    keyPoints: [
      "Top-down: 재귀 + 메모이제이션",
      "Bottom-up: 반복문 + 테이블 채우기",
      "점화식: dp[i] = f(dp[i-1], dp[i-2], ...)",
    ],
    template: `# Bottom-up 기본형
dp = [0] * (n + 1)
dp[0], dp[1] = base_case
for i in range(2, n + 1):
dp[i] = dp[i-1] + dp[i-2]  # 점화식

# 2차원 DP (냅색)
dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(1, N+1):
for w in range(W+1):
    if weight[i] > w:
        dp[i][w] = dp[i-1][w]
    else:
        dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])`,
    problems: [
      "12865_평범한배낭.py - 0/1 냅색",
      "2579_계단오르기.py - 1차원 DP",
    ],
  },
  {
    title: "4. 이분탐색 / 파라메트릭 서치",
    concept:
      "정렬된 데이터에서 O(log N) 탐색. 파라메트릭은 '조건을 만족하는 최소/최대' 문제.",
    keyPoints: [
      "left, right = 0, len(arr) (반열린 구간)",
      "Lower Bound: arr[mid] < target → left = mid + 1",
      "Upper Bound: arr[mid] <= target → left = mid + 1",
    ],
    template: `# Lower Bound (target 이상인 첫 위치)
def lower_bound(arr, target):
left, right = 0, len(arr)
while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid
return left

# 파라메트릭 서치 (조건 만족하는 최대값)
left, right = min_val, max_val + 1
while left < right:
mid = (left + right) // 2
if check(mid):  # 조건 만족
    left = mid + 1  # 더 큰 값 시도
else:
    right = mid
answer = left - 1`,
    problems: [
      "2805_나무자르기.py - 파라메트릭 서치",
      "2110_공유기설치.py - 최대 거리 찾기",
    ],
  },
  {
    title: "5. 그리디",
    concept: "현재 상황에서 최선의 선택을 반복. 정렬 후 순회가 기본 패턴.",
    keyPoints: [
      "정렬 기준이 핵심 (끝나는 시간, 비율 등)",
      "선택/배제 조건 명확히",
      "반례 확인 필수",
    ],
    template: `# 회의실 배정 패턴
data.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 기준
end_time = 0
count = 0
for start, end in data:
if start >= end_time:
    count += 1
    end_time = end`,
    problems: [
      "1931_회의실배정.py - 끝나는 시간 기준 정렬",
      "11047_동전.py - 큰 단위부터",
    ],
  },
  {
    title: "6. 투포인터 / 슬라이딩 윈도우",
    concept: "정렬된 배열에서 두 포인터로 O(N) 탐색. 합, 구간 문제에 활용.",
    keyPoints: [
      "양끝 시작: left = 0, right = n-1",
      "한쪽 시작: left = right = 0",
      "조건에 따라 포인터 이동",
    ],
    template: `# 두 수의 합 (양끝 시작)
left, right = 0, len(arr) - 1
while left < right:
total = arr[left] + arr[right]
if total == target:
    # 찾음
elif total < target:
    left += 1
else:
    right -= 1`,
    problems: ["2470_두용액.py - 0에 가까운 두 수 찾기"],
  },
  {
    title: "7. 스택 / 큐",
    concept: "스택: LIFO (괄호, 히스토그램). 큐: FIFO (BFS, 시뮬레이션).",
    keyPoints: [
      "스택: 이전 상태 저장, 짝 맞추기",
      "큐: deque 사용, popleft()로 O(1)",
      "모노톤 스택: 오큰수, 히스토그램",
    ],
    template: `# 스택 - 괄호 매칭
stack = []
for char in s:
if char == '(':
    stack.append(char)
else:
    if not stack:
        return False
    stack.pop()
return len(stack) == 0

# 모노톤 스택 - 오큰수
stack = []
for i, val in enumerate(arr):
while stack and arr[stack[-1]] < val:
    result[stack.pop()] = val
stack.append(i)`,
    problems: ["2493_탑.py - 모노톤 스택", "9012_괄호.py - 괄호 매칭"],
  },
  {
    title: "8. 힙 / 우선순위큐",
    concept: "최소/최대값을 O(log N)에 추출. 중앙값, 정렬, 다익스트라에 활용.",
    keyPoints: [
      "heapq는 최소힙 (최대힙은 -값 사용)",
      "heappush, heappop 모두 O(log N)",
      "중앙값: 최대힙 + 최소힙 조합",
    ],
    template: `import heapq
# 기본 사용
heap = []
heapq.heappush(heap, value)
min_val = heapq.heappop(heap)

# 최대힙
heapq.heappush(heap, -value)
max_val = -heapq.heappop(heap)

# 중앙값 (좌: 최대힙, 우: 최소힙)
if len(left) == len(right):
heapq.heappush(left, -num)
else:
heapq.heappush(right, num)
# 밸런싱 후 -left[0]이 중앙값`,
    problems: [
      "1655_가운데를말해요.py - 중앙값 유지",
      "11279_최대힙.py - 기본 힙",
    ],
  },
  {
    title: "9. 최단경로 (다익스트라 / 플로이드)",
    concept:
      "다익스트라: 한 점 → 모든 점 O((V+E)logV). 플로이드: 모든 점 → 모든 점 O(V³).",
    keyPoints: [
      "다익스트라: 힙 + 방문 체크, 음수 가중치 불가",
      "플로이드: 3중 반복문, k가 바깥 루프",
      "0-1 BFS: 가중치 0,1만 있으면 deque로 O(V+E)",
    ],
    template: `# 다익스트라
import heapq
def dijkstra(start):
dist = [INF] * (V + 1)
dist[start] = 0
pq = [(0, start)]
while pq:
    cost, cur = heapq.heappop(pq)
    if cost > dist[cur]: continue
    for next_cost, next_node in graph[cur]:
        new_cost = cost + next_cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
return dist

# 플로이드
for k in range(n):
for i in range(n):
    for j in range(n):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`,
    problems: [
      "1916_최소비용구하기.py - 다익스트라",
      "플로이드워셜.py - 모든 쌍 최단거리",
    ],
  },
  {
    title: "10. 위상정렬",
    concept: "DAG에서 선후관계에 따른 정렬. 진입차수 0인 노드부터 처리.",
    keyPoints: [
      "진입차수(indegree) 배열 관리",
      "BFS/Kahn: 큐로 진입차수 0인 노드 처리",
      "DFS: 후위순회 역순",
    ],
    template: `from collections import deque
def topological_sort():
indegree = [0] * (V + 1)
for u in graph:
    for v in graph[u]:
        indegree[v] += 1

dq = deque([i for i in range(1, V+1) if indegree[i] == 0])
result = []
while dq:
    cur = dq.popleft()
    result.append(cur)
    for next in graph[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            dq.append(next)
return result`,
    problems: [
      "2252_줄세우기.py - 기본 위상정렬",
      "2637_장난감조립.py - 위상정렬 + DP",
    ],
  },
  {
    title: "11. 트리",
    concept:
      "사이클 없는 연결 그래프. 순회(전위/중위/후위), 부모 찾기, LCA 등.",
    keyPoints: [
      "전위: 루트 → 왼쪽 → 오른쪽",
      "중위: 왼쪽 → 루트 → 오른쪽",
      "후위: 왼쪽 → 오른쪽 → 루트",
    ],
    template: `class TreeNode:
def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def preorder(node):
if not node: return
print(node.val)
preorder(node.left)
preorder(node.right)

def inorder(node):
if not node: return
inorder(node.left)
print(node.val)
inorder(node.right)

def postorder(node):
if not node: return
postorder(node.left)
postorder(node.right)
print(node.val)`,
    problems: [
      "1991_트리순회.py - 전위/중위/후위",
      "5639_이진검색트리.py - BST 후위순회",
    ],
  },
  {
    title: "12. 백트래킹",
    concept: "가지치기를 통한 완전탐색. 유망하지 않으면 즉시 되돌아감.",
    keyPoints: [
      "재귀 + 상태 복구 (선택 → 재귀 → 취소)",
      "가지치기 조건으로 탐색 공간 축소",
      "순열/조합의 기반",
    ],
    template: `# N-Queen 패턴
def backtrack(row):
if row == N:
    count += 1
    return
for col in range(N):
    if is_safe(row, col):
        board[row] = col
        backtrack(row + 1)
        board[row] = -1  # 복구

def is_safe(row, col):
for r in range(row):
    if board[r] == col:  # 같은 열
        return False
    if abs(board[r] - col) == abs(r - row):  # 대각선
        return False
return True`,
    problems: [
      "9663_N-Queen.py - 대각선 체크",
      "10971_외판원순회2.py - 모든 경로 탐색",
    ],
  },
  {
    title: "13. 분할정복",
    concept: "문제를 작은 부분으로 나누어 해결 후 합침. 병합정렬, 쿼드트리 등.",
    keyPoints: [
      "분할: 문제를 작은 단위로 나눔",
      "정복: 기저 조건에서 직접 해결",
      "병합: 부분 해를 합쳐서 전체 해 도출",
    ],
    template: `def divide_conquer(start, end):
# 기저 조건
if start == end:
    return base_case

mid = (start + end) // 2
left = divide_conquer(start, mid)
right = divide_conquer(mid + 1, end)

# 병합
return merge(left, right)`,
    problems: ["2630_색종이만들기.py - 쿼드트리", "1074_z.py - 재귀적 분할"],
  },
  {
    title: "14. LIS (최장 증가 수열)",
    concept:
      "가장 긴 증가하는 부분 수열 찾기. DP는 O(N²), 이분탐색은 O(N log N).",
    keyPoints: [
      "DP: dp[i] = max(dp[j] + 1) for j < i and arr[j] < arr[i]",
      "이분탐색: LIS 배열 유지, lower_bound로 위치 찾기",
      "길이만 구할 때 이분탐색 활용",
    ],
    template: `# 이분탐색 O(N log N)
def lis_binary(arr):
lis = []
for num in arr:
    if not lis or lis[-1] < num:
        lis.append(num)
    else:
        # lower_bound
        left, right = 0, len(lis)
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < num:
                left = mid + 1
            else:
                right = mid
        lis[left] = num
return len(lis)`,
    problems: ["11503_가장긴증가하는부분수열.py - 이분탐색 LIS"],
  },
  {
    title: "15. LCS (최장 공통 부분수열)",
    concept: "두 문자열의 공통 부분수열 중 가장 긴 것. 2차원 DP로 해결.",
    keyPoints: [
      "dp[i][j] = 길이 i, j까지의 LCS 길이",
      "같으면: dp[i-1][j-1] + 1",
      "다르면: max(dp[i-1][j], dp[i][j-1])",
    ],
    template: `def lcs(s1, s2):
m, n = len(s1), len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

return dp[m][n]`,
    problems: ["9251_LCS.py - LCS 길이", "9252_LCS2.py - LCS 문자열 복원"],
  },
];

// 문서 생성
const children = [];

// 제목
children.push(
  new Paragraph({
    heading: HeadingLevel.TITLE,
    alignment: AlignmentType.CENTER,
    children: [
      new TextRun({ text: "코딩테스트 유형별 정리", bold: true, size: 48 }),
    ],
  })
);

children.push(
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [
      new TextRun({
        text: "24시간 벼락치기용 - 웅노의 풀이 문제 기반",
        size: 24,
        color: "666666",
      }),
    ],
  })
);

children.push(new Paragraph({ children: [] }));

// 빠른 참조 테이블
children.push(
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "Quick Reference", bold: true })],
  })
);

const quickRefRows = [
  new TableRow({
    children: [
      new TableCell({
        borders,
        shading: { fill: "2C3E50", type: ShadingType.CLEAR },
        width: { size: 3000, type: WidthType.DXA },
        children: [
          new Paragraph({
            children: [
              new TextRun({ text: "유형", bold: true, color: "FFFFFF" }),
            ],
          }),
        ],
      }),
      new TableCell({
        borders,
        shading: { fill: "2C3E50", type: ShadingType.CLEAR },
        width: { size: 6360, type: WidthType.DXA },
        children: [
          new Paragraph({
            children: [
              new TextRun({ text: "핵심 키워드", bold: true, color: "FFFFFF" }),
            ],
          }),
        ],
      }),
    ],
  }),
];

const quickRefData = [
  ["BFS/DFS", "연결, 경로, 방문, 최단거리(BFS)"],
  ["DP", "점화식, 최적해, 중복 부분문제"],
  ["이분탐색", "정렬된 데이터, O(log N), 파라메트릭"],
  ["그리디", "정렬 후 선택, 현재 최선"],
  ["스택/큐", "괄호, LIFO/FIFO, 모노톤"],
  ["힙", "최소/최대, 중앙값, 다익스트라"],
  ["위상정렬", "선후관계, DAG, 진입차수"],
  ["백트래킹", "가지치기, 순열/조합, N-Queen"],
];

quickRefData.forEach(([type, keywords], idx) => {
  quickRefRows.push(
    new TableRow({
      children: [
        new TableCell({
          borders,
          shading: {
            fill: idx % 2 === 0 ? "F8F9FA" : "FFFFFF",
            type: ShadingType.CLEAR,
          },
          width: { size: 3000, type: WidthType.DXA },
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [
            new Paragraph({
              children: [new TextRun({ text: type, bold: true })],
            }),
          ],
        }),
        new TableCell({
          borders,
          shading: {
            fill: idx % 2 === 0 ? "F8F9FA" : "FFFFFF",
            type: ShadingType.CLEAR,
          },
          width: { size: 6360, type: WidthType.DXA },
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [
            new Paragraph({ children: [new TextRun({ text: keywords })] }),
          ],
        }),
      ],
    })
  );
});

children.push(
  new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    columnWidths: [3000, 6360],
    rows: quickRefRows,
  })
);

children.push(new Paragraph({ children: [new PageBreak()] }));

// 각 카테고리 섹션
categories.forEach((cat, index) => {
  // 제목
  children.push(
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 400, after: 200 },
      children: [new TextRun({ text: cat.title, bold: true, size: 32 })],
    })
  );

  // 개념
  children.push(
    new Paragraph({
      spacing: { after: 120 },
      children: [
        new TextRun({ text: "개념: ", bold: true }),
        new TextRun({ text: cat.concept }),
      ],
    })
  );

  // 핵심 포인트
  children.push(
    new Paragraph({
      spacing: { before: 120, after: 80 },
      children: [
        new TextRun({ text: "핵심 포인트", bold: true, color: "E74C3C" }),
      ],
    })
  );

  cat.keyPoints.forEach((point) => {
    children.push(
      new Paragraph({
        indent: { left: 360 },
        children: [new TextRun({ text: "• " + point })],
      })
    );
  });

  // 템플릿 코드
  children.push(
    new Paragraph({
      spacing: { before: 200, after: 80 },
      children: [
        new TextRun({ text: "템플릿 코드", bold: true, color: "3498DB" }),
      ],
    })
  );

  children.push(
    new Table({
      width: { size: 100, type: WidthType.PERCENTAGE },
      columnWidths: [9360],
      rows: [
        new TableRow({
          children: [
            new TableCell({
              borders,
              shading: { fill: "F5F5F5", type: ShadingType.CLEAR },
              width: { size: 9360, type: WidthType.DXA },
              margins: { top: 100, bottom: 100, left: 150, right: 150 },
              children: cat.template.split("\n").map(
                (line) =>
                  new Paragraph({
                    children: [
                      new TextRun({ text: line, font: "Consolas", size: 18 }),
                    ],
                  })
              ),
            }),
          ],
        }),
      ],
    })
  );

  // 복습할 문제
  children.push(
    new Paragraph({
      spacing: { before: 200, after: 80 },
      children: [
        new TextRun({ text: "복습할 문제", bold: true, color: "27AE60" }),
      ],
    })
  );

  cat.problems.forEach((prob) => {
    children.push(
      new Paragraph({
        indent: { left: 360 },
        spacing: { after: 40 },
        children: [new TextRun({ text: "✓ " + prob })],
      })
    );
  });

  // 페이지 구분 (마지막 제외)
  if (index < categories.length - 1 && (index + 1) % 2 === 0) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
  } else {
    children.push(new Paragraph({ spacing: { after: 300 }, children: [] }));
  }
});

// 마지막: 실수 방지 체크리스트
children.push(new Paragraph({ children: [new PageBreak()] }));

children.push(
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "시험 전 체크리스트", bold: true })],
  })
);

const checklist = [
  "입출력: import sys; input = sys.stdin.readline",
  "재귀 깊이: sys.setrecursionlimit(10**6)",
  "0-indexed vs 1-indexed 확인",
  "visited 체크 타이밍 (BFS: 큐에 넣을 때)",
  "양방향 간선 추가 빼먹지 않기",
  "int 오버플로우 (Python은 괜찮음)",
  "모듈러 연산 위치 확인",
  "빈 입력, 경계값 테스트",
];

checklist.forEach((item) => {
  children.push(
    new Paragraph({
      spacing: { after: 80 },
      children: [new TextRun({ text: "☐ " + item })],
    })
  );
});

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Arial", size: 22 } },
    },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 32, bold: true, font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 } },
      },
      {
        id: "Title",
        name: "Title",
        basedOn: "Normal",
        quickFormat: true,
        run: { size: 48, bold: true, font: "Arial" },
        paragraph: { alignment: AlignmentType.CENTER, spacing: { after: 200 } },
      },
    ],
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 },
        },
      },
      children: children,
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("/mnt/user-data/outputs/코딩테스트_유형별정리.docx", buffer);
  console.log("문서 생성 완료!");
});
