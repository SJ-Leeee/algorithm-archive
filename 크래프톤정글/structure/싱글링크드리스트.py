class Node:
    # 생성자 (constructor)
    def __init__(self, val):
        # 인스턴스 속성 (instance attribute)
        self.val = val
        self.next = None


"""
메소드
1. push
    input val
    output: 리스트
2. pop
    input
    output: 리스트 
3. unshift
    input val
    output: 리스트 
4. shift
    input
    output: 리스트 
5. get
    input: index
    output: list[index] 
6. set
    input: index, value
    output: True or False
7. insert
    input: index, val
    output: True or False
8. remove
    input: index
    output: removed
9. reverse
    input
    output: 리스트

"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    """
        1. 새로운 노드를 생성
        2. 기존 꼬리의 next를 새로운 노드에 연결
        3. 새로운 노드를 꼬리로 지정
        O(1)
    """

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode  # 여기서 같은객체를 가르키므로 다음 코드에서는 헤드는 이 객체를 계속 가르키고 있다.
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    """
        1. 이전거에 현재노드를 저장
        2. next = null 이면 이전 것이 꼬리
        3. 이전 것.next = null
        O(n)
    """

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

    """
    O(1)
    """

    def unshift(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            cur_head = self.head
            self.head = new_node
            self.head.next = cur_head
        self.length += 1
        return self

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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        count = 0

        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail

        cur_node = self.head
        while count < index:  # index == 3
            cur_node = cur_node.next
            count += 1  # count == 3이 되었을때

        return cur_node

    def set_value(self, index, value):
        found_node = self.get(index)
        if found_node:
            found_node.val = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return True if self.unshift(value) else False
        if index == self.length:
            return True if self.push(value) else False

        new_node = Node(value)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return True if self.shift() else False
        if index == self.length - 1:
            return True if self.pop() else False

        prev_node = self.get(index - 1)
        remove_node = prev_node.next
        prev_node.next = remove_node.next

        self.length -= 1
        return remove_node

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node

        next_node = None
        prev_node = None

        for _ in range(self.length):
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return self

    def __str__(self):
        """print() 함수용"""
        if self.length == 0:
            return "빈 리스트"

        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


# s_l_list = SinglyLinkedList()

# s_l_list.push("push1")
# s_l_list.push("push2")
# s_l_list.push("push3")
# s_l_list.push("push4")
# pass
# s_l_list.pop()
# pass
# s_l_list.unshift("unshift1")
# s_l_list.unshift("unshift2")
# pass
# s_l_list.shift()
# pass
# s_l_list.get(0)
# s_l_list.get(2)

# pass
# s_l_list.set_value(2, "set1")
# s_l_list.set_value(6, "enable set")

# pass


# a = s_l_list.get(1)
# print(a)


# pass
