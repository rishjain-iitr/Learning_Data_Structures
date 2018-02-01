# A simple program to introduce a linked list

# Node class
class Node:

	# Function to initialize node object
	def __init__(self, data):
		self.data = data # assigns data
		self.next = None # Inotialize next as null

#Linked List class
class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while(temp):
			print temp.data
			temp = temp.next

# Code execution start here.
if __name__ == '__main__':

	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third
	llist.printList()
	
