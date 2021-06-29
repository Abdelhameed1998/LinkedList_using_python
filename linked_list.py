class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, headnode=None):
        self.headnode = headnode
        self.count = 0
        if headnode:
            self.count = 1

    def append(self, new_node):
        current = self.headnode
        if self.headnode:  ## check if head node not Nont
            while current.next:  # start from head node until reach last node
                current = current.next
            current.next = new_node
        else:
            self.headnode = new_node
        self.count += 1

    def get_position(self, position):
       if position  <  0 or position - self.count > 1 :
           print("Mot valid position")
       else:
           if position == 1:
               if self.headnode:
                    return self.headnode.value
               else:
                   return None
           else:
               current = self.headnode
               counter = 1
               while counter <= position and current.next:
                   if position == counter:
                       return current.value
                   current=current.next
                   counter = counter +1
               return None

    def print_linked_list(self):
        current= self.headnode
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

    def insert(self, new_node,position):
        current = self.headnode
        counter = 1
        if position == 1:
            new_node.next = self.headnode
            self.headnode = new_node
        else:
            while counter < position and current:
                if counter == position -1 :
                    new_node.next=current.next
                    current.next = new_node
                current = current.next
                counter +=1


    def insert_first(self, new_element):
        self.insert(new_element,1)
        ## or
        # new_element.next = self.headnode
        # self.headnode = new_element

    def delete_first(self):
        self.delete(self.headnode.value)
        # or
        # if self.headnode:
        #     deleted_element = self.headnode
        #     temp = deleted_element.next
        #     self.headnode = temp
        #     return deleted_element
        # else:
        #     return None

    def delete(self,value):
        current = self.headnode
        previous = None
        while current.next and not (current.value ==value):
            previous = current
            current = current.next
        if current.value == value:
            self.count -=1
            if previous:
                previous.next = current.next
            else:
                self.headnode = current.next
            del current

    #### functions to handle
    # delete multiple elements that would have same value to be deleted
    # handle exceptions and wrong inputs
