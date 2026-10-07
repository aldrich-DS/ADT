class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, value):
        """Ajoute au début : O(1)"""
        self.head = Node(value, self.head)
        if self.tail is None:              
            self.tail = self.head

    def add_back(self, value):
        """Ajoute à la fin sans utiliser tail : O(n)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node
        self.tail = new_node               

    def add_back_optimiser(self, value):
        """Ajoute à la fin en utilisant tail : O(1)"""
        new_node = Node(value)
        if self.tail is None:              
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_node = new_node     # l'ancien dernier pointe vers le nouveau
        self.tail = new_node               # tail avance sur le nouveau

    def search(self, target):
        """Retourne True si target est dans la liste : O(n)"""
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next_node
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next_node
        print("None")


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add_front(10)
    my_list.add_front(20)
    my_list.add_front(30)
    my_list.add_back(5)
    my_list.add_back_optimiser(1)

    my_list.display()                     
    print("Trouvée" if my_list.search(5) else "RAS")
    print("Trouvée" if my_list.search(99) else "RAS")
