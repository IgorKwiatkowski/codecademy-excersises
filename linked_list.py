# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Add your insert_beginning and stringify_list methods below:

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        stack = [self.get_head_node()]
        while stack:
            current_node = stack.pop()
            if current_node is not None:
                string_list += str(current_node.get_value()) + "\n"
                stack.append(current_node.get_next_node())
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()

        else:
            while current_node.get_next_node().get_value() != value_to_remove:
                current_node = current_node.get_next_node()

            current_node.set_next_node(current_node.next_node.get_next_node())
            current_node = None

    def remove_all_nodes(self, value_to_remove):
        current_node = self.get_head_node()

        while True:
            if current_node.get_value() == value_to_remove:
                self.remove_node(value_to_remove)
            current_node = current_node.get_next_node()
            if current_node is None:
                break


ll = LinkedList(1)
ll.insert_beginning(20)
ll.insert_beginning(20)
ll.insert_beginning(20)
ll.insert_beginning(-5)
ll.remove_all_nodes(20)
print(ll.stringify_list())
print(str(ll.get_head_node().get_value()))
