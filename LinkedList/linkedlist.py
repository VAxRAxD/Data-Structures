class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, *args):
        self.head = None
        for data in args:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
    
    def remove_last(self):
        if self.head is None:
            return
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

    def search(self,data):
        index=0
        if self.head is None:
            print("Linked list is Empty")
            return
        itr=self.head
        while itr is not None:
            if itr.data==data:
                print("Found element "+str(data)+" at "+str(index+1)+" position")
                return
            index+=1
            itr=itr.next

    def reverse_list(self):
        dummy=None
        itr=self.head
        while itr:
            next_node=itr.next
            itr.next=dummy
            dummy=itr
            itr=next_node
        self.head=dummy
        self.print()

    def n_node_from_last(self,index):
        if index==0:
            return
        n=self.get_length()-index
        itr=self.head
        i=0
        while i<n:
            itr=itr.next
            i+=1
        print(f"{index} node from the last is "+str(itr.data))

    def palindrome(self):
        if self.head==None:
            return
        string=""
        itr=self.head
        while itr is not None:
            string+=str(itr.data)
            itr=itr.next
        if string==string[::-1]:
            print("Linked List is a palindrome")
        else:
            print("Linked List is not a palindrome")
