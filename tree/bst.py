class bst_tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
    
    def number_of_nodes(self, root):
        queue = []
        queue.append(root)
        count = 1
        while len(queue) > 0:
            if root.left != None and root.right != None:
                count = count+1
            if root.left != None:
                queue.append(root.left)
                
            if root.right != None:
                queue.append(root.right)

            root = queue.pop(0)
        return count

    def inorder(self, root):

        # inorder traversal
        if root:
            self.display(root.left)
            print(root.data)
            self.display(root.right)

        # prints all the leaf nodes
        # if root:
        #     self.display(root.left)
        #     if root.left == None and root.right == None:
        #         print(root.data)
        #     self.display(root.right)



if __name__ == "__main__":

    root = bst_tree(5)
    root.insert(root, bst_tree(3))
    root.insert(root, bst_tree(2))
    root.insert(root, bst_tree(4))
    root.insert(root, bst_tree(8))
    root.insert(root, bst_tree(7))
    root.insert(root, bst_tree(9))
    root.inorder(root)
    print(root.number_of_nodes(root))