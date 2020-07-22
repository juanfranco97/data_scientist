class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root        
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def preOrder(root):
    print(root.info)
    if root.left : 
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def postOrder(root):
    if root.left : 
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
    print(root.info)

def inOrder(root):
    if root.left : 
        preOrder(root.left)
    print(root.info)
    if root.right:
        preOrder(root.right)


def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left),height(root.right))

from collections import deque
def levelOrder(root):
    if not root: return
    q= deque()
    q.append(root)
    while len(q) > 0: 
        node = q.popleft()
        print(node.info, end = ' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert_node_r(self, node, val):
        if node is None:
            return Node(val)
        if node.info >val:
            node.left= insert_node_r(node.left,val)
        else:
            node.right = insert_node_r(node.right,val)
        
    def insert_r(self, val):
        self.root = insert_node_r(self.root,val)
    
    def insert(self,val):
        parent= None
        node = self.root
        #!1 Traverse the tree in the correct direction, updating the parent
        while node:
            parent = node 
            if node.info > val:
                node= node.left
            else:
                node = node.right
                
        #check if parent is NI, if  so , set the root the new node
        if not parent:
            self.root = Node(val)
            return
        # check for correct position in the parent, and add child node.
        if parent.info > val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)
    
def lca(node, v1, v2):
    if not node: return None
    if node.info > v1 and node.info> v2:
        return lca(node.left, v1, v2)
    if node.info < v1 and node.info< v2:
        return lca(node.right, v1, v2)
    return node

def lca(node, v1, v2):
    while True:
        if node.info > v1 and node.info> v2:
            node = node.left
        if node.info < v1 and node.info< v2:
            node = node.right
        else:
            return node

if __name__ == "__main__":
    tree = BinarySearchTree()
    t = 6

    #arr = list(map(int, input().split()))
    arr=[1,2,5,3,6,4]
    for i in range(t):
        tree.create(arr[i])
    preOrder(tree.root)

