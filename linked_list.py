from itertools import cycle
from re import S
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,data):
        # this is to add the very first element
        if not self.head:
            # Node is having 'next' as 'None' because it's the only element in the list
            self.head = Node(data,None)
            return
        # this variable is referring to the current element while traversing the list
        curr = self.head # first element
        while curr.next:
            curr = curr.next
        # we have reached to the last element in the list
        curr.next = Node(data,None)
    
    def remove_first(self):
        curr = self.head
        self.head = curr.next
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end="-> ")
            curr = curr.next