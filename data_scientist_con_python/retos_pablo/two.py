import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node =  SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def printLinkedList(head):
    if not head.data :
        print('the list is empty. To execute this funcion,  you most insert nodes in list')
    else:
        while True:
            print(head.data)
            head = head.next
            if head == None:
                break

def insertNodeAtPosition(head, data, position):
    i = 0
    for _ in range(position+1):
        if position == i:
            head= SinglyLinkedList()
            head.insert_node(5)
            for _ in range(2):
                print('hola')
                #head = head.next
            head.next.data = head.data       
            head.data = data 
            print(head.data)
            print(head.next.data)
            #print(head.next.next.data)
        head = head.next
        i += 1 

        
   
    
           
if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    #printLinkedList(llist.head)

    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(llist.head, data, position)
   