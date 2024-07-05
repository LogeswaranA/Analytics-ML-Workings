class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head == None:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count

    def insert_at_specific(self,data,pointer):
        if pointer <0 or pointer>=self.get_length():
            raise Exception("Invalid pointer")

        if pointer==0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        count=0
        while itr:
            if count==pointer-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1


    def remove_at_specific(self,pointer):
        if pointer <0 or pointer>=self.get_length():
            raise Exception("Invalid pointer")

        if pointer==0:
            self.head = self.head.next
            return
        
        itr = self.head
        count=0
        while itr:
            if count==pointer-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        
        itr = self.head
        liststr = " "
        while itr:
            liststr += str(itr.data) + "--->"
            itr = itr.next
        print(liststr)

if __name__ == "__main__":
    lList = LinkedList()
    lList.insert_at_begining(45)
    lList.insert_at_begining(4)
    lList.insert_at_begining(3)
    lList.print()
    lList.insert_at_end(50)
    lList.print()
    lList.insert_at_specific(70,2)
    lList.print()
    lList.remove_at_specific(2)
    lList.print()