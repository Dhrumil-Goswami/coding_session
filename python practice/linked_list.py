# Task Below list
# 1 Insert element in list

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
        print("\n\n\n<<<<", lststr)
    
    def inser_at_end(self, data):
        # node = Node(data=data, next=)
        if self.head is None:
            self.head = Node(data=data, next=self.head)
            return
        itr = self.head
        print("\n\n\n<<<<<head", self.head.data)
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
        return cnt + 1 
    
if __name__ == '__main__':
    l1 = LinkedList()
    l1.inser_at_end(10)
    l1.inser_at_end(20)
    l1.inser_at_end(30)
    l1.insert_at_beginning(5)
    l1.print_linked_list()
    l1.get_length()