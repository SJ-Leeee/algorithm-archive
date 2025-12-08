import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 루트 -> 왼쪽 자식 -> 오른쪽 자식
def preorder_traversal(node, p_list):
    p_list.append(node.val)
    if node.left:
        preorder_traversal(node.left, p_list)
    if node.right:
        preorder_traversal(node.right, p_list)

    return p_list


# 왼쪽 자식 -> 루트 -> 오른쪽 자식
def inorder_traversal(node, p_list):
    if node.left:
        inorder_traversal(node.left, p_list)

    p_list.append(node.val)

    if node.right:
        inorder_traversal(node.right, p_list)

    return p_list


# 왼쪽 자식 -> 오른쪽 자식 -> 루트
def postorder_traversal(node, p_list):
    if node.left:
        postorder_traversal(node.left, p_list)

    if node.right:
        postorder_traversal(node.right, p_list)

    p_list.append(node.val)

    return p_list


"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""
nodes = {}


def get_node(name):
    if name in nodes:
        return nodes[name]

    node = TreeNode(name)
    nodes[name] = node
    return node


N = int(sys.stdin.readline())

result_node = None

for i in range(N):

    root, left, right = sys.stdin.readline().split()
    root_node = get_node(root)

    if i == 0:
        result_node = root_node

    if left != ".":
        left_node = get_node(left)
        root_node.left = left_node

    if right != ".":
        right_node = get_node(right)
        root_node.right = right_node

a = preorder_traversal(result_node, [])
b = inorder_traversal(result_node, [])
c = postorder_traversal(result_node, [])

print("".join(a))
print("".join(b))
print("".join(c))


# gpt

# 방법 1: 클래스 기반 (상태 관리가 깔끔함)
import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def get_or_create_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = TreeNode(name)
        return self.nodes[name]

    def build_tree(self, n):
        for i in range(n):
            root_name, left_name, right_name = sys.stdin.readline().split()
            root_node = self.get_or_create_node(root_name)

            if i == 0:
                self.root = root_node

            if left_name != ".":
                root_node.left = self.get_or_create_node(left_name)

            if right_name != ".":
                root_node.right = self.get_or_create_node(right_name)

    def preorder(self, node=None):
        if node is None:
            node = self.root

        result = [node.val]
        if node.left:
            result.extend(self.preorder(node.left))
        if node.right:
            result.extend(self.preorder(node.right))
        return result

    def inorder(self, node=None):
        if node is None:
            node = self.root

        result = []
        if node.left:
            result.extend(self.inorder(node.left))
        result.append(node.val)
        if node.right:
            result.extend(self.inorder(node.right))
        return result

    def postorder(self, node=None):
        if node is None:
            node = self.root

        result = []
        if node.left:
            result.extend(self.postorder(node.left))
        if node.right:
            result.extend(self.postorder(node.right))
        result.append(node.val)
        return result


"""

--- gpt
"""

import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_traversal(node):
    """한 번의 순회로 전위, 중위, 후위 결과를 모두 구하기"""
    if not node:
        return [], [], []

    pre_result = [node.val]
    in_result = []
    post_result = []

    # 왼쪽 서브트리 순회
    left_pre, left_in, left_post = tree_traversal(node.left)

    # 오른쪽 서브트리 순회
    right_pre, right_in, right_post = tree_traversal(node.right)

    # 결과 조합
    pre_result.extend(left_pre)
    pre_result.extend(right_pre)

    in_result.extend(left_in)
    in_result.append(node.val)
    in_result.extend(right_in)

    post_result.extend(left_post)
    post_result.extend(right_post)
    post_result.append(node.val)

    return pre_result, in_result, post_result


N = int(sys.stdin.readline())
nodes = {}

for _ in range(N):
    p, l, r = sys.stdin.readline().strip().split()

    # 부모 노드 생성 또는 가져오기
    if p not in nodes:
        nodes[p] = TreeNode(p)
    parent = nodes[p]

    # 왼쪽 자식 처리
    if l != ".":
        if l not in nodes:
            nodes[l] = TreeNode(l)
        parent.left = nodes[l]

    # 오른쪽 자식 처리
    if r != ".":
        if r not in nodes:
            nodes[r] = TreeNode(r)
        parent.right = nodes[r]

# 한 번의 순회로 모든 결과 획득
pre_result, in_result, post_result = tree_traversal(nodes["A"])

print("".join(pre_result))
print("".join(in_result))
print("".join(post_result))
