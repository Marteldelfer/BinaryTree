class Node:

    def __init__(self, value) -> None:
        self.__value = value
        self.__left = None
        self.__right = None

    @property
    def _value(self):
        return self.__value

    @_value.setter
    def _value(self, value):
        self.__value = value

    @property
    def _left(self):
        return self.__left

    @_left.setter
    def _left(self, value):
        self.__left = value

    @property
    def _right(self):
        return self.__right

    @_right.setter
    def _right(self, value):
        self.__right = value




class BinaryTree:

    def __init__(self) -> None:
        self.__root = None
        self.len = 0

    @property
    def _root(self):
        return self.__root
    
    @_root.setter
    def _root(self, value):
        self.__root = value
        
    def insert(self, value) -> None:

        node = Node(value)

        if self._root == None:
            self._root = node
            return None
        
        dadNode = None
        currentNode: Node = self._root

        #Finds where node should be
        while currentNode != None:

            dadNode: Node = currentNode
                
            if node._value < currentNode._value:
                currentNode = currentNode._left

            else:
                currentNode = currentNode._right


        #Sets the node on the tree
        if node._value < dadNode._value:
            dadNode._left = node
        
        else:
            dadNode._right = node

        self.len += 1

    def show(self, currentNode: Node = 'root') -> None:

        if currentNode == 'root':
            currentNode = self._root
        if currentNode != None:
            print(currentNode._value)
            self.show(currentNode._left)
            self.show(currentNode._right)

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        return False

    def delete(self, value) -> None:

        if self._root == None:
            raise ValueError('Binary Tree is empty')

        dadNode = None
        currentNode: Node = self._root

        #Search for the value in the tree
        while currentNode != None:

            if currentNode._value == value:
                break

            dadNode: Node = currentNode
            
            if currentNode._value > value:
                currentNode = currentNode._left

            else:
                currentNode = currentNode._right 

        #If value is not in tree, raise error
        if currentNode == None:
            raise ValueError('Binary Tree does not contain value')
        
        #Checking if current node has no child nodes
        if currentNode._left == None and currentNode._right == None:
            
            #Checks if current node is from left or right of dadNode
            if dadNode._left == currentNode:
                dadNode._left = None

            else:
                dadNode._right = None

        #Checking if current node has one child node
        elif currentNode._left == None or currentNode._right == None:

            #Check if current node is from left or right
            if dadNode._left == currentNode:

                #Checking if child node is the left or right one
                if currentNode._left == None:
                    dadNode._left = currentNode._right
                else:
                    dadNode._left = currentNode._left

            #Current node is the right node
            else:

                #Checking if child node is the left or right one
                if currentNode._left == None:
                    dadNode._right = currentNode._right
                else:
                    dadNode._right = currentNode._left
                        
        #Current node has two child nodes   
        else:

            if currentNode != self._root:
                newDadNode: Node = currentNode
                newCurrentNode: Node = currentNode._right

                #Find the smaller node that is bigger than current node
                while newCurrentNode._left != None:
                    newDadNode = newCurrentNode
                    newCurrentNode = newCurrentNode._left

                #Set new current node to replace current node
                newCurrentNode._left = currentNode._left
                if newCurrentNode != currentNode._right:
                    newCurrentNode._right = currentNode._right

                #Replace current node with new current node
                if dadNode._left == currentNode:
                    dadNode._left = newCurrentNode
                else:
                    dadNode._right = newCurrentNode
                newDadNode._left = None

            #The to be deleted node is the root
            else:
                newCurrentNode: Node = currentNode._right

                #Finds the smaller node that is bigger than newCurrentNode
                while newCurrentNode._left != None:
                    newCurrentNode = newCurrentNode._left
                
                #Set new current node to replace current node
                newCurrentNode._left = currentNode._left
                if newCurrentNode != currentNode._right:
                    newCurrentNode._right = currentNode._right

                #Replace current node with new current node
                self._root = newCurrentNode


arvore = BinaryTree()
arvore.show()
arvore.insert(10)
arvore.insert(5)
arvore.insert(7)
arvore.insert(3)
arvore.insert(15)
arvore.insert(18)
arvore.insert(13)
arvore.delete(10)
arvore.show()