# Task using linked list
# 1 Insert element at start
# 2 Insert element at end
# 3 Insert element at index
# 3 Remove element

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node
    
    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        lststr =''
        while itr:
            lststr += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print("\n\n\n<<<<lststr", lststr)
    
    def insert_at_end(self, data):
        # node = Node(data=data, next=)
        if self.head is None:
            self.head = Node(data=data, next=self.head)
            return
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data=data)
                return
            itr = itr.next
    
    def get_length(self):
        itr = self.head
        cnt = 0
        while itr:
            cnt += 1
            itr = itr.next
        print("\n\n::::cnt::::", cnt)
        return cnt
    
    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Exception")
        if index == 0:
            self.insert_at_beginning(data=data)
        
        itr = self.head
        cnt = 0
        while itr:
            cnt += 1
            if cnt == index - 1:
                itr.next = Node(data=data, next=itr.next)
                return
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Exception")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        cnt = 0
        while itr:
            cnt += 1
            if cnt == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            
    def insert_value_list(self, data):
        for i in data:
            self.insert_at_end(data=i)  

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_end(10)
    l1.insert_at_end(20)
    l1.insert_at_end(30)
    l1.insert_at_beginning(5)
    l1.get_length()
    l1.insert_at(9, 4)
    l1.print_linked_list()
    l1.remove_at(4)
    l1.insert_value_list(data=['Apple', 'banana', 'orange', 'grapes'])
    l1.print_linked_list()