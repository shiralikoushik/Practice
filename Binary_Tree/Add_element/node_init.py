class Node():
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return f'<Node {self.value}>'

    