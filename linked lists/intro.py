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
    def deleteatbegineing(self,head):
        if head is None:
            return None 
        head=head.next
        return head
    def deleteatEnd(self,head):
        temp=head
        if head is None:
            return None
        if head.next is None:
            return None
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        return head
sol=LinkedList()
head=None
head=sol.insertAtBeginning(head,10)
head=sol.insertAtBeginning(head,20)
head=sol.insertAtBeginning(head,30)
head=sol.insertAtEnd(head,70)
head=sol.insertAtEnd(head,40)
head=sol.insertAtEnd(head,60)
head=sol.deleteatbegineing(head)
head=sol.deleteatEnd(head)
sol.printlist(head)

        

        