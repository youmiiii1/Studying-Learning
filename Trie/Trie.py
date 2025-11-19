class TrieNode:
    def __init__(self):
        self.children = {}                              # Здесь хранятся буквы[ключи] и их пути к другим буквам[значение].
        self.is_end = False                             # Флаг, если "True", значит конец слова.

class Trie:
    def __init__(self):
        self.root = TrieNode()                          # Это корень дерева — стартовая точка, откуда начинаются все слова.

    def insert(self, word: str):                        # Метод для добавления слова в дерево, и каждой буквы в (self.children).
        node = self.root                                # Начальный узел (root), от которого будем добавлять узлы(буквы) в словарь children.
        for char in word:                               # Для каждой буквы в слове.
            if char not in node.children:               # Если буква не находится в children[root], то -->
                node.children[char] = TrieNode()        # То добавляем новый узел от корня root.
            node = node.children[char]                  # Иначе, проверяем следующую букву(узел) на наличие (children).
        node.is_end = True                              # Помечаем конец слова.

    def search(self, word: str):                        # Метод для проверки: есть ли полное слово в дереве?
        node = self._find_node(word)                    # Ищем узел последней буквы слова.
        return node is not None and node.is_end         # Слово найдено, если узел существует и это конец слова.

    def _find_node(self, word: str):                    # Вспомогательный метод: ищет путь по дереву до конца слова.
        node = self.root                                # Начинаем с корня дерева.
        for char in word:                               # Для каждой буквы в слове.
            if char not in node.children:               # Если перехода по этой букве нет —
                return None                             # — значит, слово не найдено.
            node = node.children[char]                  # Иначе, проверяем следующую букву(узел) на наличие (children).
        return node                                     # Возвращаем узел, на котором остановились (последняя буква слова).




le_trie = Trie()
le_trie.insert("Cat")
print(le_trie.search("Cat"))
print(le_trie.search("Ca"))



