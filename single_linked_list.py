class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.length = 0
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def print_list(self):
        cur_node = self.head
        while cur_node:
            self.length+=1
            print(cur_node.data)
            cur_node = cur_node.next
        print(self.length)
    def add_list(self,prev_node,data):
        if not prev_node:
            print('Prev node not in list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_node(self,node):
        curnode = self.head
        while curnode.next!=node and curnode.next!=None:
            curnode = curnode.next
        if curnode.next == node:
            curnode.next = node.next
            node.next = None
        else:
            print('There is no such node')
    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

llist = Linkedlist()
llist.append('A')
llist.append('B')
llist.append('C')
llist.add_list(llist.head.next,'D')
llist.append('E')
llist.delete_node(llist.head.next.next)
llist.print_list()

