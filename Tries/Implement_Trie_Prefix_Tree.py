from trie import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                cur_node.children[c] = TrieNode()
                cur_node = cur_node.children[c]
        cur_node.is_word = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]

        return cur_node.is_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return True


if __name__ == "__main__":
    cmds = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    words = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    print(f"Input: commands: {cmds}\nwords: {words}")
    sol = None
    res = []
    for i, cmd in enumerate(cmds):
        output = None
        if cmd == "Trie":
            sol = Trie()
        elif cmd == "insert":
            sol.insert(words[i])
        elif cmd == "search":
            output = sol.search(words[i])
        elif cmd == "startsWith":
            output = sol.startsWith(words[i])
        res.append(output)

    print(f"Output: {res}")
