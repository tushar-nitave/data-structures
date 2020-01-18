class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, root, node):
        
        if root == None:
           root = node
        if node.data <= root.data:
            if root.left == None:
                root.left = node
            else:
                self.insert(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                self.insert(root.right, node)
                
    def get_count(self, root):
        count = 1
        if root:
            if root.left:
                count += self.get_count(root.left)
            if root.right:
                count += self.get_count(root.right)
        return count

    def delete_node(self, root, node):
        if root.data == node:
            
            if root.left == None and root.right == None:
                root = None
                return root
            elif root.left != None:
                temp = root
                root = root.left
                temp = None
                return root
            elif root.right != None:
                temp = root
                root = root.right
                temp = None
                return root
                
        elif node <= root.data:
            root.left = self.delete_node(root.left, node)

        elif node >= root.data:
            root.right = self.delete_node(root.right, node)

        return root
  
    def _min(self, root):
        if root == None:
           return "Tree is empty"

        if root.left == None:
            return root.data

        current = root
        while current.left:
            current = current.left
        return current.data

    def _max(self, root):
        if root == None:
            return "Tree is empty"
        if root.right == None:
            return root.data
        current = root
        while current.right:
            current = current.right
        return current.data

    def in_tree(self, root, value):
        if root:
            if value == root.data:
                return True
            if value > root.data:
                return self.in_tree(root.right, value)
            if value < root.data:
                return self.in_tree(root.left, value)
        return False

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data," ", end=" ")
            self.inorder(root.right)


if __name__ == "__main__":
    root = Tree(5)

    root.insert(root, Tree(4))
    root.insert(root, Tree(6))
    root.insert(root, Tree(88))
    root.insert(root, Tree(7))
    root.insert(root, Tree(3))

    root.inorder(root)

    print("\nCount: ", root.get_count(root))

    root = root.delete_node(root, 4)

    root.inorder(root)
    print("\nCount: ", root.get_count(root))

    print("Min: ", root._min(root))
    print("Max: ", root._max(root))
    print(root.in_tree(root, 100))
