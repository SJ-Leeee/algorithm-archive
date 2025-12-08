class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

        """
        테일의 넥스트 새로운노드
        새로운 노드 프리뷰 원래테일
        그리고 테일을 마지막 노드로 설정
        """

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    """
    리무브노드 = 지금테일
    지금테일.prev = 
    """

    def pop(self):
        if self.length == 0:
            return None
        remove_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = remove_node.prev
            self.tail.next = None
            remove_node.prev = None
        self.length -= 1
        return remove_node

    def shift(self):
        if self.length == 0:
            return None

        remove_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = remove_node.next
            self.head.prev = None
            remove_node.next = None
        self.length -= 1
        return remove_node

    def unshift(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return False

        if index > (self.length // 2):
            count = self.length - 1
            cur_node = self.tail
            while count != index:
                cur_node = cur_node.prev
                count -= 1
            return cur_node
        else:
            count = 0
            cur_node = self.head
            while count != index:
                cur_node = cur_node.next
                count += 1
            return cur_node

    def set_value(self, index, value):
        found_node = self.get(index)
        if not found_node:
            return False

        found_node.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.unshift(value)
        if index == self.length - 1:
            self.push(value)
        new_node = Node(value)
        prev_node = self.get(index - 1)
        after_node = prev_node.next

        new_node.next = after_node, new_node.prev = prev_node
        after_node.prev = new_node, prev_node.next = new_node

        self.length += 1

        return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.shift()
        if index == self.length - 1:
            self.pop()
        found_node = self.get(index)
        prev_node = found_node.prev
        next_node = found_node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        
        found_node.next =None, found_node.prev = None

        self.length -= 1
        return True
