

class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
         self.__head = None

    def add(self,data):
        node = Node(data)
        if self.__head == None:
            self.__head = node
        else:
            temp = self.__head
            while(temp.next != None):
                temp = temp.next

            temp.next = node

    def search(self, data) -> bool:
        temp = self.__head
        while(temp != None):
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def remove(self, data):
        temp = Node(0,self.__head)
        prev = temp
        curr = self.__head
        while(curr != None):
            if curr.data == data:
                prev.next = curr.next
                break
            
            prev = curr
            curr = curr.next
        
        self.__head = temp.next

    def __repr__(self) -> str:
        output = ""
        temp = self.__head
        while(temp != None):
            output += f"{temp.data}->"
            temp = temp.next
        output += "NONE"
        return output
