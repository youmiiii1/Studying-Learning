class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            new_node.next = self.root               # Замыкаем на самого себя (так как Noda'а единственная в списке)
            return
        else:
            current_node = self.root
            while current_node.next != self.root:   # Пока следующая Node'а НЕ РАВНА (self.root)
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.root               # Замыкаем (new_node) Node'у с самой первой / заглавной (self.root)

    def output(self):
        current_node = self.root
        while True:                                 # Пока True цикл шагает бесконечно по Node'ам в списке
            print(current_node.value, end=" -> ")
            current_node = current_node.next
            if current_node == self.root:           # Если Noda'а на которой мы стоим (current_node) РАВНА (self.root)
                break                               # То выходим из цикла
        return current_node.value

    def search(self, target) -> bool:
        current_node = self.root
        while True:                                 # Пока True цикл шагает бесконечно по Node'ам в списке
            if current_node.value == target:
                return True
            current_node = current_node.next

            if current_node == self.root:           # Если Noda'а на которой мы стоим (current_node) РАВНА (self.root)
                break                               # То выходим из цикла
        return False

    def pop(self):
        if not self.root:
            return None

        if self.root.next == self.root:               # Если в списке одна / заглавная Node'а (self.root)
            pop_node = self.root.value
            self.root = None
            return pop_node

        current_node = self.root

        while current_node.next.next != self.root:   # Если у следующей Node'ы её (self.next) НЕ РАВЕН (self.root)
            current_node = current_node.next
                                                     # Если у следующей Node'ы её (self.next) РАВЕН (self.root)
        pop_node = current_node.next.value           # У следующей Node'ы её (self.next) значение (self.value) помещаем в переменную (pop_node)
        current_node.next = self.root                # У следующей Node'ы её (self.next) перенаправляем на (self.root)
        return pop_node

    def is_empty(self):
        if self.root:
            return False
        return True

    def qsize(self):
        counter_node = 0

        if not self.root:
            return counter_node

        current_node = self.root
        while True:                             # Пока True цикл шагает бесконечно по Node'ам в списке
            counter_node += 1
            current_node = current_node.next

            if current_node == self.root:       # Если Noda'а на которой мы стоим (current_node) РАВНА (self.root)
                break                           # То выходим из цикла
        return counter_node

    def index(self, target):
        if not self.root:
            return None

        node_counter = 0
        current_node = self.root

        while True:                             # Пока True цикл шагает бесконечно по Node'ам в списке
            if target == current_node.value:
                return node_counter
            current_node = current_node.next
            node_counter += 1

            if current_node == self.root:       # Если Noda'а на которой мы стоим (current_node) РАВНА (self.root)
                break                           # То выходим из цикла
        return None

    def slice(self, start: int, stop: int):
        counter = 0
        temp = []
        current_node = self.root

        while counter < stop:                       # Двигаемся по списку пока (counter) меньше чем значение (stop)
            if counter >= start:
                temp.append(current_node.value)
            current_node = current_node.next
            counter += 1

            if current_node == self.root:           # Если Noda'а на которой мы стоим (current_node) РАВНА (self.root)
                break                               # То выходим из цикла
        return temp

    def insert(self, index: int, value):
        new_node = Node(value)
        current_node = self.root
        counter = 0

        if not self.root:
            self.root = new_node                       # Создаем Node'у и говорим списку, что она (self.root)
            self.root.next = self.root                 # Замыкаем на самого себя (так как Noda'а единственная в списке)
            return

        if index == 0:
            while current_node.next != self.root:      # Пока не дойдем до последней Node'ы шагаем к ней
                current_node = current_node.next

            new_node.next = self.root                  # Новую Node'у (new_node) ставим в самое начало списка
            current_node.next = new_node               # Циклим последнюю Node'у (current_node) с самой первой
            self.root = new_node                       # Говорим списку, что первая Node'а теперь (self.root)
            return

        while current_node.next != self.root and counter < index - 1: # Шагаем пока не найдем узел, который стоит ПЕРЕД позицией index (то есть с индексом index - 1)
            current_node = current_node.next
            counter += 1

            if current_node == self.root:
                break
                                                                      # Когда дошли до Node'ы, именно после неё мы вставим (new_node)
        new_node.next = current_node.next                             # Ставим Node'у (new_node) после index'а до которого дошли и связываем со следующей Node'ой
        current_node.next = new_node                                  # Node'у (current_node) по index'у, связываем с той которую добавили перед ней (new_node)


ls = LinkedList()

ls.append(10)
ls.append(20)
ls.append(30)
ls.append(40)
ls.append(50)
ls.append(60)
ls.append(70)
ls.append(80)
ls.append(90)
ls.append(100)

print(ls.slice(0,11))
