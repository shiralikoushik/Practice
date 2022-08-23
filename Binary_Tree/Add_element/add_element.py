from node_init import Node


class BinaryTree:
    def __ini__(self, head):
        self.head = head

    def add(self, newnode):
        current_node = self.head
        while current_node:
            if newnode.value == current_node.value:
                raise ValueError("Same")
            elif current_node.value > newnode.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = newnode
                    break
            elif current_node.value < newnode.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = newnode
                    break
