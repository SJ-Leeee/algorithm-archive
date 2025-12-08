from collections import deque


class Node:
    def __init__(self, value):
        self.vaule = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def BFS():
        data = [], queue = []

    def DFSPreOrder(self):
        data = []
        current = self.root
        self.travers(current)
        return data

    def travers(self, node, data):
        data.push(node)
        if node.left:
            self.travers(node.left, data)
        if node.right:
            self.travers(node.right, data)

    def DFSPostOrder(self):
        data = []
        current = self.root
        self.travers_post(current)
        return data

    def travers_post(self, node, data):
        if node.left:
            self.travers(node.left, data)
        if node.right:
            self.travers(node.right, data)
        data.push(node)  # 마지막에 데이터에 삽입


class PriorityQueue:

    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):  # 데이터 삽입
        new_node = PQNode(value, priority)
        self.values.append(new_node)
        self.bubble_up(new_node)  # 새로운 노드를 삽입 후 위치 조정

    def bubble_up(self, node):
        idx = len(self.values) - 1
        cur_node = self.values[idx]  # 현재 추가된 노드
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent_node = self.values[parent_idx]
            if parent_node.priority <= cur_node.priority:
                # 만약 현재 노드가 우선순위가 높다면
                # 우선 순위가 낮을수록 먼저처리
                break

        self.values[parent_idx] = cur_node
        self.values[idx] = parent_node
        idx = parent_idx

    # 자리를 바꾼 후 인덱스는 이전 부모인덱스로 대치

    def dequeue(self):  # 루트 노드 추출
        priority_node = self.values[0]
        end_node = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end_node
            self.sinkdown()  # 마지막 노드를 상단으로 올려 히피다운

        return priority_node

    def sinkdown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]

        while True:
            left_child_idx = idx * 2 + 1
            right_child_idx = idx * 2 + 2
            left_child = None
            right_child = None

            swap = None
            if left_child_idx < length:  # 좌측노드가 존재하고 우선순위 비교
                left_child = self.values[left_child_idx]
                if left_child.priority < element.priority:
                    swap = left_child_idx
            if right_child_idx < length:
                # 좌측노드가 존재하고 우선순위 비교 + 요소, 좌측과 비교 후 대치
                # 우측노드가 우선이 되야한다.(배열의 마지막)
                right_child = self.values[right_child_idx]
                if (swap == None and right_child.priority < element.priority) or (
                    swap != None and right_child.priority < left_child.priority
                ):
                    swap = right_child_idx
            if swap == None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


class PQNode:

    def __init__(self, value, priority):
        self.val = value
        self.priority = priority


ER = PriorityQueue()

ER.enqueue("aa", 1)
ER.enqueue("bb", 2)
ER.enqueue("cc", 3)
ER.enqueue("dd", 4)
ER.enqueue("ee", 5)
ER.dequeue()
ER.enqueue("emergency", 0)
pass
