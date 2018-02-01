# A program with mutliple function in linked list

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

	# Inserts new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data) # Allocate the node and put data into it.
		new_node.next = self.head
		self.head = new_node

	# Inserts new node after a given previous node
	def insertAfter(self, prev_node, new_data):
	 	if prev_node is None:
	 		print "The given previous node must be n the linked list"
	 		return
	 	new_node = Node(new_data)
	 	new_node.next = prev_node.next
	 	prev_node.next = new_node 

	# Inserts new node at the end!
	def append(self,new_data):
	 	new_node = Node(new_data)

	 	if self.head == None:
	 		self.head = new_node
	 		return
	 	last = self.head
	 	while(last.next):
	 		last = last.next

	 	last.next = new_node

	# delete the node with matching value
	def deleteNode(self, key):
		temp = self.head
		# if the head node itself hold the key to be deleted
		if(temp is not None):
			if temp.data == key:
				self.head = temp.next
				temp = None
				return
		#Search for the key to be deleted, keep track of the
        #previous node as we need to change 'prev.next'
		while (temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# if the key is absent in the list 
		if temp == None:
			return

		prev.next = temp.next
		temp = None
	# delete the node at specific position
	def deletePos(self, pos):

		if self.head == None:
			return
		temp = self.head

		if (pos == 0):
			self.head = temp.next
			temp = None
		for i in xrange(pos-1):
			temp = temp.next
			if (temp == None):
				break
		# If position is more than number of nodes
		if temp is None:
			return
		if temp.next is None:
			return
		# Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
		next = temp.next.next
		temp.next = None
		temp.next = next
	
	# Find Length of a Linked List (Iterative and Recursive)
	# iterative
	def iterativeCount(self):
		temp = self.head
		count = 0
		while temp is not None:
			temp = temp.next
			count += 1
		return count
	# recursive
	def recCount_i(self, node):
		if not node:
			return 0
		else:
			return 1 + recursiveCount(self, node.next)
		pass
	def recuCount(self):
		recCount_i(self,self.head)

	# Search an element in a Linked List (Iterative and Recursive)
	#iterative
	def searchIter(self,key):
		current = self.head
		while current != None:
			if current.data == key:
				return True
			current = current.next
		return False
	#recursive
	def searchRec_i(node, key):
		if (node != None):
			if node.data == key:
				return True
			else:
				searchRec_i(node.next, key)
		return False
	def searchRec(self,key):
		searchRec_i(self.head,key)
	# Swap nodes in a linked list without swapping data
	def swapNodes(self, x, y):
		# Nothing to do if x and y are same
		if x == y:
			return

		# search for x and keep track of previous and current x
		prevX = None
		currX = self.head
		while currX != None and currX.data != x:
			prevX = currX
			currX = currX.next

		# search for y amd keep track of previous and current y
		prevY = None
		currY = self.head
		while currY != None and currY.data != y:
			prevY = currY
			currY = currY.next

		# check if x and y are present
		if currX == None or currY == None:
			return
		# If x is not the head of the linked list
		if prevX != None: 
			prevX.next = currY # assign the next pinter of previous X element to current Y element
		else:# make x new head
			self.head = currY
		# If y is not the head of the linked list
		if prevY != None:
			prevY.next = currX # assign the next pinter of previous y element to current x element
		else:#make y new head
			self.head = currX

		# Swap next pointer of current element
		temp = currX.next
		currX.next = currY.next
		currY.next = temp
	# Utility function to print the linked list.
	def printList(self):
	  	temp = self.head
	  	while(temp):
	  		print temp.data
	  		temp = temp.next

# Code execution start here.
if __name__ == '__main__':
	llist = LinkedList()
	#llist.append(4)
	llist.push(2)
	llist.push(7)
	llist.push(3)
	llist.push(9)
	llist.push(1)
	llist.push(5)
	llist.append(10)
	llist.append(12)
	llist.insertAfter(llist.head.next.next,16)
	llist.deleteNode(10)
	llist.deletePos(3)
	print "Created Linked List is:"
	llist.printList()
	print "The length of linked list is:", llist.iterativeCount()
	print llist.searchIter(9)
	llist.swapNodes(2, 1)
	llist.printList()

	














