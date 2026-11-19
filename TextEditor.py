
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self._size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError

        if index == self._size:
            self.append(data)
            return

        node = Node(data)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            node.next = current.next
            current.next = node

        self._size += 1

    def delete_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError

        if index == 0:
            deleted = self.head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            deleted = current.next
            current.next = deleted.next

            if deleted == self.tail:
                self.tail = current

        if self.head is None:
            self.tail = None

        self._size -= 1
        return deleted.data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


class TextEditor:
    def __init__(self):
        self.lines = SinglyLinkedList()
        self.undo_stack = []
        self.redo_stack = []

    def add_line(self, text):
        self.insert_line(self.lines._size, text)

    def insert_line(self, index, text):
        self.lines.insert_at(index, text)
        self.undo_stack.append(("insert", index, text))
        self.redo_stack.clear()

    def delete_line(self, index):
        text = self.lines.delete_at(index)
        self.undo_stack.append(("delete", index, text))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return

        action, index, text = self.undo_stack.pop()

        if action == "insert":
            self.lines.delete_at(index)
        else:
            self.lines.insert_at(index, text)

        self.redo_stack.append((action, index, text))

    def redo(self):
        if not self.redo_stack:
            return

        action, index, text = self.redo_stack.pop()

        if action == "insert":
            self.lines.insert_at(index, text)
        else:
            self.lines.delete_at(index)

        self.undo_stack.append((action, index, text))

    def show(self):
        for i, line in enumerate(self.lines, 1):
            print(f"{i}: {line}")

ed = TextEditor()

ed.add_line("A")
ed.add_line("B")
ed.add_line("C")

ed.delete_line(1)
ed.undo()
ed.undo()
ed.redo()

ed.add_line("D")
ed.redo()

ed.show()