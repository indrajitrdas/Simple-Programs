
class node:
    def __init__(self, value, next_node = None):
        self.data = value
        self.next = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, value): # Insert front at head
        new_node = node(value, self.head)
        self.head = new_node
        
    def insert_end(self, value):
        if self.head is None:
            new_node = node(value, self.head)
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            new_node = node(value, cur_node.next)
            cur_node.next = new_node
            
    def search_iterative(self, value):
        if self.head is None:
            print("List is Empty")
        else:
            cur_node = self.head
            index = 1
            while cur_node:
                if cur_node.data == value:
                    print("value found at index " + str(index))
                    return
                else:
                    cur_node = cur_node.next
                    index = index + 1
                    
    def search_recursive(self, value):
        if self.head is None:
            print("List is Empty")
        else:
            cur_node = self.head
            index = 1
            self._search_recursive(cur_node, value, index)
    
    def _search_recursive(self, cur_node, value, index):
        if cur_node and cur_node.data == value:
            print("value found at index " + str(index))
            return
        else:
            cur_node = cur_node.next
            index = index + 1
            self._search_recursive(cur_node, value, index)
            
    def delete_node(self, value):
        if self.head is None:
            print("List is Empty")
            return
        else:
            cur_node = self.head
            if cur_node.data == value:
                self.head = cur_node.next
            else:
                self._delete(cur_node, value)
                
    def _delete(self, cur_node, value):
        next_node = cur_node.next
        if next_node and next_node.data == value:
            cur_node.next = next_node.next
            return
        else:
            cur_node = cur_node.next
            self._delete(cur_node, value)
            
    def reverse_ll(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            cur_node = self.head
            prev_node = None
            while cur_node:
                next_node = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = next_node
        self.head = prev_node
        
        
    def cycle_detect(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            slow_pointer = fast_pointer = self.head
            while slow_pointer and fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                if slow_pointer == fast_pointer:
                    print("Loop Found")
                    return
                
    def cycle_detect_remove(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            slow_p = fast_p = self.head
            while slow_p and fast_p and fast_p.next:
                slow_p = slow_p.next
                fast_p = fast_p.next.next
                if slow_p == fast_p:
                    self._remove_loop(slow_p)
    
    def _remove_loop(self, p_node):
        pt1 = pt2 = p_node
        count_loopLength = 1
        while pt1.next != pt2:
            pt1 = pt1.next
            count_loopLength += 1
        pt1 = pt_2 = self.head
        for i in range(count_loopLength):
            pt2 = pt2.next
        while(pt1 != pt2):
            pt1 = pt1.next
            pt2 = pt2.next
        while(pt2.next != pt1):
            pt2 = pt2.next
        pt2.next = None                
                        
    
    def find_nth_nodeFromEnd(self, n):
        if self.head is None:
            return
        else:
            prev_node = self.head
            cur_node = self.head
            for i in range(0,n-1):
                if cur_node:
                    cur_node = cur_node.next
                else:
                    return
            while cur_node:
                if cur_node.next is None:
                    print(prev_node.data)
                    return
                else:
                    cur_node = cur_node.next
                    prev_node = prev_node.next
    
               
    def printLL(self):
        if self.head is None:
            print("Empty linked list")
        else:
            cur_node = self.head
            while cur_node:
                print(cur_node.data)
                cur_node = cur_node.next
                

ll = LinkedList()
ll.insert(4)
ll.insert(66)
ll.insert(5)
ll.insert(83)
ll.insert(23)
ll.insert(67)
ll.insert(79)
ll.insert(45)
ll.insert(36)
#ll.printLL()

#Loop
#ll.head.next.next.next.next.next.next.next.next.next = ll.head.next.next.next.next.next
ll.find_nth_nodeFromEnd(1)