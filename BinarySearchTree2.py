# BST

class node:
    def __init__(self, value):
        self.value = value
        self.rightchild = None
        self.leftchild = None
        
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(self.root, value)
            
    def _insert(self, cur_node, value):
        if cur_node.value == value:
            print("Value already exists")
        elif cur_node.value > value:
            if cur_node.leftchild is None:
                cur_node.leftchild = node(value)
            else:
                self._insert(cur_node.leftchild, value)
        elif cur_node.value < value:
            if cur_node.rightchild is None:
                cur_node.rightchild = node(value)
            else:
                self._insert(cur_node.rightchild, value)
                
    def find_item(self, value):
        if self.root is None:
            print("Tree is Empty. Item not found")
        else:
            self._find_item(self.root, value)
    
    def _find_item(self, cur_node, value):
        if cur_node.value == value:
            print("Item Found")
            return True
        elif cur_node.value > value:
            if cur_node.leftchild is not None:
                self._find_item(cur_node.leftchild, value)
            else:
                print("Item Not Found")
                return False
        elif cur_node.value < value:
            if cur_node.rightchild is not None:
                self._find_item(cur_node.rightchild, value)
            else:
                print("Item Not Found")
                return False
            
    # Delete Node from BST
    # 1. find_min -
    def num_child(self, cur_node):
        count = 0
        if cur_node.leftchild is not None:
            count = count + 1
        if cur_node.rightchild is not None:
            count = count + 1
        return count
        
    def delete(self, value):
        if self.root is None:
            print("Tree is Empty.")
        else:
            self._delete(self.root, value, par_node = None)
                      
            
    def _delete(self, cur_node, value, par_node = None):
        if cur_node.value == value:
            if par_node is None: # Root
                cur_node.value = None
                
            else:                # Not a Root node
                #Delete Operation
                if self.num_child(cur_node) == 0:
                #Ops
                    print("Parent Node : " + str(par_node.value))
                    print(" Not Root Node")
                    print("Num Child = 0")
                    
                    if par_node.value > value:
                        par_node.leftchild = None
                    else:
                        par_node.rightchild = None
                        
                if self.num_child(cur_node) == 1:
                #ops
                    print(" Not Root Node")
                    print("Num Child = 1")
                    
                    if cur_node.leftchild is not None:
                        cur_node.value = cur_node.leftchild.value
                        cur_node.leftchild = cur_node.leftchild.leftchild
                        curnode.rightchild = cur_node.leftchild.rightchild
                    else:
                        cur_node.value = cur_node.rightchild.value
                        cur_node.leftchild = cur_node.rightchild.leftchild
                        curnode.rightchild = cur_node.rightchild.rightchild
                    
                if self.num_child(cur_node) == 2:
                #ops
                    print(" Not Root Node")
                    print("Num Child = 2")
                    
                    while 
        elif cur_node.value > value:
            if cur_node.leftchild is not None:
                self._delete(cur_node.leftchild, value, cur_node)
            else:
                print("Node doesnot Exist")
        elif cur_node.value < value:
            if cur_node.rightchild is not None:
                self._delete(cur_node.rightchild, value, cur_node)
            else:
                print("Node doesnot Exist")
        
        
            
                
    def preorder(self): # Root LC RC
        if self.root is not None:
            self._preorder(self.root)
        else:
            print("Tree is Empty")
    
    def _preorder(self, cur_node):
        print(str(cur_node.value))
        if cur_node.leftchild is not None:
            self._preorder(cur_node.leftchild)
        if cur_node.rightchild is not None:
            self._preorder(cur_node.rightchild)
            
    def inorder(self): # LC Root RC # prints in ascenting order acending order
        if self.root is not None:
            self._inorder(self.root)
        else:
            print("Tree is Empty")
            
    def _inorder(self, cur_node):
        if cur_node.leftchild is not None:
            self._inorder(cur_node.leftchild)
        print(str(cur_node.value))
        if cur_node.rightchild is not None:
            self._inorder(cur_node.rightchild)
            
    def postorder(self): # LC RC Root
        if self.root is not None:
            self._postorder(self.root)
        else:
            print("Tree is Empty")
            
    def _postorder(self, cur_node):
        if cur_node.leftchild is not None:
            self._postorder(cur_node.leftchild)
        if cur_node.rightchild is not None:
            self._postorder(cur_node.rightchild)
        print(str(cur_node.value))
            
            
        
        
        
                
            
                        
            
            
tree = BinarySearchTree()            
            