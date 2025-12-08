## 노드로 트리 만들어서.. 그냥 순회


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def set_node(self, node):
        if self.root == None:
            self.root = node
        else:
            prev_node = None
            cur_node = self.root
            while cur_node != None:
                if cur_node.val < node.val:
                    prev_node = cur_node
                    cur_node = cur_node.right
                else:
                    prev_node = cur_node
                    cur_node = cur_node.left
            if prev_node.val < node.val:
                prev_node.right = node
            else:
                prev_node.left = node

    def post_order(self, node):
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)

        print(node.val)
        return

    def get_root(self):
        return self.root

    def sayhi():
        print("sayhi")


import sys

sys.setrecursionlimit(10000)
tree = Tree()

while True:
    value = sys.stdin.readline().strip()

    if not value:
        break
    # 처리 로직
    value = int(value)
    node = TreeNode(value)
    tree.set_node(node)

root_node = tree.get_root()
tree.post_order(root_node)


# import sys

# def build_and_postorder():
#     """
#     입력을 받으면서 바로 BST를 구성하고 후위 순회 결과를 출력
#     별도의 트리 자료구조 없이 재귀적으로 처리
#     """
#     def insert_and_traverse(values, start, end):
#         if start > end:
#             return

#         root_val = values[start]

#         # 오른쪽 서브트리의 시작점 찾기 (root보다 큰 첫 번째 값)
#         right_start = start + 1
#         while right_start <= end and values[right_start] < root_val:
#             right_start += 1

#         # 왼쪽 서브트리 순회 (start+1 ~ right_start-1)
#         insert_and_traverse(values, start + 1, right_start - 1)

#         # 오른쪽 서브트리 순회 (right_start ~ end)
#         insert_and_traverse(values, right_start, end)

#         # 후위 순회이므로 루트는 마지막에 출력
#         print(root_val)

#     # 모든 입력값을 리스트로 읽기
#     values = []
#     for line in sys.stdin:
#         line = line.strip()
#         if line:
#             values.append(int(line))

#     # BST의 전위 순회 입력으로부터 후위 순회 출력
#     if values:
#         insert_and_traverse(values, 0, len(values) - 1)

# build_and_postorder()
