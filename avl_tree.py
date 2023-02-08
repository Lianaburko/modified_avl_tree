def max(a, b):
    if a >= b:
        return a
    else:
        return b


class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.height = 1
        self.size = 0


class AVL_tree: 
    def __init__(self, *args):
        self.root = None
        if args != None:
            for i in args:
                self.root = self.insert(i, self.root)
        

    def get_height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    
    def checking_balance(self, Node):
        if Node is None:
            return 0
        else:
            balance = self.get_height(Node.left) - self.get_height(Node.right)
            return balance


    def rotate_left(self, Node):
        a = Node.right
        b = a.left

        koef = 0
        k_b = 0
        if b is None:
            b_size = 0
        else: 
            b_size = b.size
            koef += 1
            k_b += 1

        if a.right is None:
            c_size = 0
        else:
            c_size = a.right.size
            koef += 1

        if Node.left is None:
            d_size = 0
        else:
            d_size = Node.left.size
            koef += 1

        a_size = a.size
        node_size = Node.size
        
        a.left = Node
        Node.right = b
        
        Node.height = 1 + max(self.get_height(Node.left), self.get_height(Node.right))
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))

        a.size = c_size + b_size + d_size + 1 + koef
        Node.size = node_size - a_size  - 1 + b_size + k_b


        return a


    def rotate_right(self, Node):
        a = Node.left
        b = a.right

        koef = 0
        k_b = 0
        if b is None:
            b_size = 0
        else: 
            b_size = b.size
            koef += 1
            k_b += 1

        if a.left is None:
            c_size = 0
        else:
            c_size = a.left.size
            koef += 1

        if Node.right is None:
            d_size = 0
        else:
            d_size = Node.right.size
            koef += 1
        
        a_size = a.size
        node_size = Node.size
        
        a.right = Node 
        Node.left = b

        Node.height = 1 + max(self.get_height(Node.left), self.get_height(Node.right))
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))

        a.size = c_size + b_size + d_size + 1 + koef
        Node.size = node_size - a_size  - 1 + b_size + k_b


        return a


    def insert(self, v, root):
        if root is None:
            return Node(v)

        elif v == root.value: 
            pass

        elif v < root.value:
            root.size += 1
            root.left = self.insert(v, root.left)
           
        elif v > root.value: 
            root.size += 1
            root.right = self.insert(v, root.right)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.checking_balance(root)

        if balance > 1:
            if root.left.value > v:
                return self.rotate_right(root)
            elif root.left.value < v:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        elif balance < -1:
            if root.right.value < v:
                return self.rotate_left(root)  
            elif root.right.value > v:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)


        self.root = root
        return root


    def m_request(self,root, k):
        if root.left is None:
            r_l = 0
        else:
            r_l = root.left.size + 1

        if r_l > k:
            try:
                req = self.m_request(root.left, k)
            except AttributeError:
                req = "This request has mistake. The first position is 1. And it is " + str(root.value)
            return req
        elif r_l < k:
            try: 
                req = self.m_request(root.right, k -  r_l - 1)
            except AttributeError:   
                req = "This request has mistake. There are less amount of numbers. Last number is " + str(root.value)
            return(req)
        else:
            return root.value

        
    def n_request(self, root, j, n):
        if root.value < j:
            if root.right is None:
                return n + 1
            else:
                if root.left is None:
                    r_l_s = 1
                else: 
                    r_l_s = root.left.size + 2
                return(self.n_request(root.right, j, n + r_l_s))
        elif root.value > j:
            if root.left is None:
                return n
            else:
                return(self.n_request(root.left, j, n))
        elif root.value == j:
            if root.left is None:
                return n 
            else:
                return n + root.left.size + 1
            


    def preorder(self, root):
        if root is None:
            return "Tree is empty"
        print('value is ',root.value)
        self.preorder(root.left)
        self.preorder(root.right)
    

    def _inorder(self, root):
        if root.left:
            yield from self._inorder(root.left)
        yield root.value
        if root.right:
            yield from self._inorder(root.right)

    def __iter__(self):
        for i in self._inorder(self.root):
            yield i


    def __del__(self):
        return 'Tree destroyed'


def main(text_data):
    data = text_data.split(' ') 
    Tree = AVL_tree()
    res = []
    rt = None
    i = 0
    while i <= len(data) - 1:
        if data[i] == 'k':
            i += 1
            rt = Tree.insert(int(data[i]), rt)
        elif data[i] == 'm':
            i += 1
            m = Tree.m_request(rt, int(data[i]) - 1)
            res.append(m)

        elif data[i] == 'n':
            i += 1
            n = Tree.n_request(rt, int(data[i]),0)
            res.append(n)
        i += 1

    result = ''
    for i in res:
        result += ' ' + str(i) 


    return result[1::]


#Tree = AVL_tree(1, 2, 3, 4, 5, 6, 4, 4, 6)
#Tree.preorder(Tree.root)