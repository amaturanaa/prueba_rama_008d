class node:
    def _init_(self, char):
        self.char = char
        links = []

class tree:
    def _init_(self):
        self.links = []
    
    def AddWord(self, word):
        if len(word) > 0:
            for link in self.links:
                if link.char == word[0]:
                    return
            self.links.append(node(word[0]))

MyTree = tree()

MyTree.AddWord("reshiram")
MyTree.AddWord("zekrom")
MyTree.AddWord("gaismagorm")

for i in MyTree.links:
    print(i.char)