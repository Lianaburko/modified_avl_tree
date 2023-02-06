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

        print('HELLO L ', Node.value)

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

        print('val = ', a.value, 'size = ', a.size)
        print('val = ', Node.value, 'size = ', Node.size)
        
        return a


    def rotate_right(self, Node):

        print('HELLO R ', Node.value)
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
        elif v <= root.value:
            root.size += 1
            root.left = self.insert(v, root.left)
           
        elif v > root.value: ########################################
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

        return root


    def m_request(self,root, k):
        if root.left is None:
            r_l = 0
        else:
            r_l = root.left.size + 1

        if r_l > k:
            return(self.m_request(root.left, k))
        elif r_l < k:
            return(self.m_request(root.right,k -  r_l - 1))
        else:
            #print('r_v = ', root.value)
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
            return

        print('value is ',root.value)
        print('size is ',root.size) 
        self.preorder(root.left)
        print('----------------')

        self.preorder(root.right)
    
