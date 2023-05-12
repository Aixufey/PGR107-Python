# AVL BST


class Node(object):
    """
    When Node is instantiated the height is 1
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL(object):
    def __init__(self):
        self.root = None

    # Step 1 - insert BST
    def insert(self, key):
        self.root = self.put(self.root, key)

    # Helper recursively put new node into tree
    def put(self, node, key):
        if not node:
            new_node = Node(key)
            self.root = new_node
            return new_node
        elif key < node.value:
            node.left = self.put(node.left, key)
        else:
            node.right = self.put(node.right, key)

        # Step 2 Update the height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Step 3 Calculate balance factor {-1, 0, 1}
        bf = self.get_balance(node)
        print(f"bf: %s " % bf)

        """
            Step 4 if -1 right aligned, 0 is balanced, 1 is left aligned tree 
            node is now acting as the root of current subtree after performing insertion from parent root
            
            LL case:     5   insert(2)                      3
                        /    height = 3                    / \
                       3     BF     > 1                   2   5
                      /      key < node.left = true
                     2   
                     
            RR case: 
                     5       insert(7)                      6
                      \      height = 3                    / \
                       6     BF     > -1                  5   7
                        \    key > node.right = true
                         7
                         
            LR case:
                     5       insert(3)                         5         3
                    /        height = 3                       /         / \
                   2         BF     > 1                      3         2   5
                    \        key > node.left = true         /
                     3                                     2
                     
            RL case: 
                     5       insert(6)                     5             6
                      \      height = 3                     \           / \
                       8     BF     > -1                     6         5   8
                      /      key < node.right = true          \
                     6                                         8
        """
        if bf > 1 and key < node.left.value:
            print("LL")
            return self.right_rotate(node)

        if bf < -1 and key > node.right.value:
            print("RR")
            return self.left_rotate(node)

        if bf > 1 and key > node.left.value:
            print("LR")
            """
                       X
                      /
                     Y
                      \
                       Z
            """
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if bf < -1 and key < node.right.value:
            print("RL")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        self.root = node

        return self.root

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    """
               X                 Y      <- calculate height again on this root again, BF should be 0 after rotation.
              / \              /   \
             Y   Xr           Z     X   <- calculate height again on this root after rotation, then back track to parent
            / \              / \   / \
           Z   Yr           Zl Zr Yr  Xr
          / \
         Zl  Zr 
    """

    def right_rotate(self, x):
        # Prepare Y to be new root, and store Y's right child
        y = x.left
        yr = y.right

        # Rotate
        y.right = x
        x.left = yr

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    """
                X                      Y
               / \                   /   \
              Xl  Y                 X     Z
                 / \               / \   / \
                Yl  Z             Xl Yl Zl Zr
                   / \
                  Zl  Zr 
    """

    def left_rotate(self, x):
        # Prepare Y as the new root, store Y's left child
        y = x.right
        yl = y.left

        y.left = x
        x.right = yl

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def pre_order(self, root):
        # Pre: Root, Left, Right
        if not root:
            return

        print(f"%s " % root.value, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        # In: Left, Root, Right
        if not root:
            return
        self.in_order(root.left)
        print(f"%s " % root.value, end=" ")
        self.in_order(root.right)

    def post_order(self, root):
        # Post: Left, Right, Root
        if not root:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(f"%s " % root.value, end=" ")


avl = AVL()
avl.insert(5)
avl.insert(2)
avl.insert(3)
avl.insert(8)
avl.insert(9)

avl.pre_order(avl.root)