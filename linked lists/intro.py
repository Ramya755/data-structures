class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def insertAtBeginning(self,head, data):
        newNode = Node(data)
        newNode.next = head
        return newNode
    def printlist(self,head):
        temp=head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def insertAtEnd(self,head,data):
        newNode=Node(data)
        temp=head
        if head is None:
            return newNode
        while temp.next:
            temp=temp.next
        temp.next=newNode
        return head
sol=LinkedList()
head=None
head=sol.insertAtBeginning(head,10)
head=sol.insertAtBeginning(head,20)
head=sol.insertAtBeginning(head,30)
head=sol.insertAtEnd(head,70)
sol.printlist(head)

        

        