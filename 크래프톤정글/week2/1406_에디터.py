# 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

# 푸쉬 삽입 삭제만 있는 링크드리스트 만들기


import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return

    def unshift(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.unshift(value)
            return
        if index == self.length:
            self.push(value)
            return

        new_node = Node(value)

        prev_node = self.get(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1
        return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            if self.length == 1:
                removed = self.head
                self.head = None
                self.tail = None
                self.length = 0
                return removed
            else:
                removed = self.head
                self.head = self.head.next
                self.length -= 1
                return removed

        prev_node = self.get(index - 1)
        remove_node = prev_node.next

        # 🔧 수정: tail 제거시 tail 업데이트
        if remove_node == self.tail:
            self.tail = prev_node
        prev_node.next = remove_node.next

        self.length -= 1
        return remove_node

    def get(self, index):
        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail

        cur_node = self.head

        for _ in range(index):
            cur_node = cur_node.next

        return cur_node

    def display(self):
        if self.length == 0:
            print("빈 리스트")
            return

        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        print(" -> ".join(values))

    def to_string(self):
        """리스트를 문자열로 변환"""
        if self.length == 0:
            return ""

        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return "".join(result)

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed

        cur_node = self.head
        prev = cur_node
        while cur_node.next:
            prev = cur_node
            cur_node = cur_node.next
        # 루프를 빠져나오면 prev에는 꼬리-1
        # current_node= tail 이 위치
        self.tail = prev
        self.tail.next = None
        self.length -= 1

        return cur_node

    def shift(self):
        if self.length == 0:
            return None

        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed

        removed = self.head
        next_head = self.head.next
        self.head = next_head
        self.length -= 1
        return removed


def action(char, index):

    if char == "L" and index > 0:
        index -= 1
        return index

    if char == "D" and index < linked_list.length:
        index += 1
        return index

    if char == "B" and 0 <= index <= linked_list.length:
        linked_list.remove(index - 1)
        if index != 0:
            index -= 1

    return index


linked_list = LinkedList()


word = input()
N = int(input())

for i in word:
    linked_list.push(i)

index = linked_list.length  # index 0~4
for i in range(N):
    command = sys.stdin.readline().split()

    if len(command) >= 2:
        cmd, char = command[0], command[1]
    else:
        cmd, no = command[0], None

    ## 생각해보자 index가 0이면 L,B 무시 // D면 index+=1 , P면 shift
    ##         index가 list.length랑 같으면 D무시 //  P면 push B면 pop L이면 쩔수

    if index == 0:
        if cmd == "P":
            linked_list.shift(char)
            index += 1

        if cmd == "D":
            index += 1
    if index == linked_list.length:
        if cmd == "P":
            linked_list.push(char)
            index += 1
        if cmd == "B":
            linked_list.pop()
            index -= 1
        if cmd == "L":
            index -= 1

    if index == 1 and cmd == "B":
        linked_list.shift()

    # if 0 < index < linked_list:


result = linked_list.to_string()

print(result)
