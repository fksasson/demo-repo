class linkNode:
    '''
    Node class for a linked list
    '''
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def buildLinkedList():
    val = input("Choose value(- to exit):")
    if val == '-':
        return None

    node = linkNode(int(val))
    next = input('next?(y/n):')
    if next == 'y':
        node.next = buildLinkedList()

    return node
