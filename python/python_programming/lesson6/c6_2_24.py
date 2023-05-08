"""クラス変数の初期化"""

class T(object):
    words = []

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')

print(d.words)