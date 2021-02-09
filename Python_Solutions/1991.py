def preorder(tree, root):
    answer = root
    if tree[root][0] != ".":
        answer += preorder(tree, tree[root][0])
    if tree[root][1] != ".":
        answer += preorder(tree, tree[root][1])
    return answer

def inorder(tree, root):
    answer = ""
    if tree[root][0] != ".":
        answer += inorder(tree, tree[root][0])
    answer += root
    if tree[root][1] != ".":
        answer += inorder(tree, tree[root][1])
    return answer

def postorder(tree, root):
    answer = ""
    if tree[root][0] != ".":
        answer += postorder(tree, tree[root][0])
    if tree[root][1] != ".":
        answer += postorder(tree, tree[root][1])
    answer += root
    return answer


N = int(input())

tree = {}
for i in range(N):
    tree[chr(65 + i)] = []

for i in range(N):
    p, l, r = input().split()
    tree[p] = [l, r]

print(preorder(tree, "A"))
print(inorder(tree, "A"))
print(postorder(tree, "A"))
