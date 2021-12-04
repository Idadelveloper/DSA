class Trie:
    def __init__(self, val:str):
        self.char = val
        self.children = []
        self.word_finished = False

    def add(self, word:str):
        node = self

        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = Trie(char)
                new_node.char = char
                node.children.append(new_node)

                node = new_node

        node.word_finished = True

    def find(self, word:str):

        node = self
        word_found = False

        for char in word:
            for child in node.children:
                if child.char == char:
                    node = char
                    break
                else:
                    word_found = False

        if node.word_finished:
            word_found = True

        return word_found


root = Trie("*")
root.add("car")
root.add("cat")
print(root.find("cat"))
