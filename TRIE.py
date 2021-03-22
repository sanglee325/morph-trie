class Node:
    def __init__(self, key=None, pos=None, string=None, end=False):
        self.key = key # 한글자
        self.string = string # 단어의 끝인지 아닌지
        self.pos = pos
        self.end = end
        self.children = {} # 자식 노드 저장


class TRIE:
    def __init__(self):
        self.head = Node()

    def insert(self, word, pos):
        curr = self.head

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.string = word
        curr.pos = pos.split(',')
        curr.end = True

    def search(self, word):
        curr = self.head

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        
        return curr.end

    def pos(self, word):
        curr = self.head
        
        for char in word[0]:
            if char in curr.children:
                curr = curr.children[char]

            else:
                return False
        
        return curr.pos