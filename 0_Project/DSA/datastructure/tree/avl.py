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

    def delete(self, key):
        deleted = self.remove(self.root, key)
        # print(f"%s is deleted" % deleted.value)

    def remove(self, current, key):
        if not current:
            return current

        # Here we recursively go left or right depends on the Node value we compare.
        if key < current.value:
            current.left = self.remove(current.left, key)

        elif key > current.value:
            current.right = self.remove(current.right, key)

        else:
            """
                - Eventually if deletion key is found we are here.
                - 3 edge cases for deletion node.
                - is a leaf node | has one child | has two children 
            """
            # Last node
            if self.root.left is None and self.root.right is None:
                temp = self.root
                self.root = None
                return temp

            # If deletion node has one child
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            successor = self.find_current_subTree_min(current.right)
            current.value = successor.value
            # recursive call for removing the duplicate after successor is found and in place.
            current.right = self.remove(current.right, successor.value)

            if current is None:
                return current
            """
                If deletion node has two children
                
                         X
                        /  
                       Xl  <-- Current has two children, find it's successor.
                      / \      It will always on right subtree(Z)'s left(Zl).
                     Y   Z     However, if Zl is None, Z will be successor.
                        / \
                       Zl  Zr
                       
                         X
                        /  
                       Zl  <-- Zl is successor
                      / \
                     Y   Z
                          \
                           Zr
                           
                         X
                        /  
                       Z   <-- If Zl is None, Z is successor
                      / \
                     Y   Zr
            """

            # After deletion - Check height and re-balance if necessary
            current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
            # Check BF
            balance = self.get_balance(current)

            # Case 1 - Left Left
            if balance > 1 and self.get_balance(current.left) >= 0:
                return self.right_rotate(current)

            # Case 2 - Right Right
            if balance < -1 and self.get_balance(current.right) <= 0:
                return self.left_rotate(current)

            # Case 3 - Left Right
            if balance > 1 and self.get_balance(current.left) < 0:
                current.left = self.left_rotate(current.left)
                return self.right_rotate(current)

            # Case 4 - Right Left
            if balance < -1 and self.get_balance(current.right) > 0:
                current.right = self.right_rotate(current.right)
                return self.left_rotate(current)

        return current

    def find_current_subTree_min(self, node):
        if node is None or node.left is None:
            return node

        return self.find_current_subTree_min(node.left)

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
avl.insert(0)
avl.insert(1)
avl.insert(50)
avl.insert(15)
avl.insert(22)

avl.pre_order(avl.root)

print()
avl.delete(15)

avl.pre_order(avl.root)

"""
             3     Pre order: 3, 1, 0, 2, 22, 8, 5, 9, 50 before deletion
           /   \
          1     15
         / \    / \
        0   2  8   50
              / \   \
             5   9   22


             3     Pre order: 3, 1, 0, 2, 22, 8, 5, 9, 50 after deletion
           /   \
          1     22
         / \    / \
        0   2  8   50
              / \
             5   9
"""
