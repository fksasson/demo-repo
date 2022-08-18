class treeNode:
    '''
    Node class for a binary tree
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildBinaryTree():
    '''
    Build a binary tree with wanted values.
    Works in PREORDER form(value, left, right)
    Works with recursion.
    Works globaly.
    Returns root node.
    '''

    value = input('choose value (- to exit): ')
    if value == '-':
        return None

    print(f'value chosen: {value}')
    node = treeNode(int(value))

    left = input(f'left node?(y,n): ')
    if left == 'y':
        node.left = buildBinaryTree()

    right = input(f'right node?(y,n): ')
    if right == 'y':
        node.right = buildBinaryTree()

    return node
